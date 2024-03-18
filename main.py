import os
import logging
import pandas as pd
import pygsheets as pg
import sys
from Google_auth import gkey
from googleapiclient.discovery import build
from datetime import datetime, timedelta
import pytz
from connection_fn import snowflake_Connect
from snowflake.connector.pandas_tools import write_pandas

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Get current directory
current_dir = os.path.abspath(os.getcwd())

# Print current directory
print(current_dir)

# Define scopes for Google API
SCOPES = [
    "https://www.googleapis.com/auth/contacts.readonly",
    "https://www.googleapis.com/auth/chat.spaces.readonly",
    "https://www.googleapis.com/auth/chat",
    "https://www.googleapis.com/auth/chat.messages",
    "https://www.googleapis.com/auth/chat.messages.readonly",
    "https://www.googleapis.com/auth/chat.memberships",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/spreadsheets",
]

# Authenticate with Google Workspace
credentials = gkey
gs = pg.authorize(custom_credentials=credentials)
shid = "insert sheet ID"
sheet = gs.open_by_url(f"https://docs.google.com/spreadsheets/d/{shid}")
chat_client = build("chat", "v1", credentials=credentials)
people_client = build("people", "v1", credentials=credentials)
gmt = pytz.timezone("Asia/Kolkata")
logging.info("All API Builds Ready...")

# Define space list
spaceList = [
    "spaces/ID1",
    "spaces/ID2",
    "spaces/ID3",
    "spaces/ID4",
    "spaces/ID5",
    "spaces/ID6",
    "spaces/ID7",
    "spaces/ID8",
]

def export_chat_messages():
    names, types, emails, messagesall, message_id1, message_id2, timeData, emo, spaceNames, userIDs = ([] for _ in range(10))

    for spName in spaceList:
        space_id = None
        spaces = chat_client.spaces().list().execute()

        for space in spaces["spaces"]:
            if space["name"] == spName:
                space_id = space["name"]
                SpaceNDisp = space["displayName"]
                logging.info(SpaceNDisp)
                break

        if space_id is None:
            logging.error(f"Space '{spName}' not found.")
            return

        messages = retrieve_all_messages(space_id)

        for message in messages:
            try:
                spaceName = SpaceNDisp
                sender_id = get_sender_id(message)
                is_thread = "threadReply" in message
                emoji_data = get_emoji_data(message)
                message_text = get_message_text(message)
                id1, id2 = get_message_ids(message)
                final_time = convert_to_gmt(message["createTime"])
                message_type = "Thread" if is_thread else "Primary"

                types.append(message_type)
                messagesall.append(message_text)
                message_id1.append(id1)
                message_id2.append(id2)
                timeData.append(final_time)
                emo.append(emoji_data)
                spaceNames.append(spaceName)
                userIDs.append(sender_id)
            except Exception as e:
                logging.error(f"An error occurred: {str(e)}")

    df = pd.DataFrame({
        "Space_Name": spaceNames,
        "User_ID": userIDs,
        "Type": types,
        "Time": timeData,
        "Message_ID1": message_id1,
        "Message_ID2": message_id2,
        "Message": messagesall,
        "Emoji": emo,
    })
    return df

def get_sender_id(message):
    return message["sender"]["name"].split("/")[1]

def get_emoji_data(message):
    if "emojiReactionSummaries" not in message:
        return np.nan
    emoji_counts = []
    for emoji_summary in message["emojiReactionSummaries"]:
        emoji = emoji_summary["emoji"]["unicode"]
        count = emoji_summary["reactionCount"]
        emoji_counts.append(f"{emoji}: {count}")
    return ", ".join(emoji_counts)

def get_message_text(message):
    return message["text"] if "text" in message else np.nan

def get_message_ids(message):
    msg_id = ((message["name"]).split("/")[-1]).split(".")
    id1, id2 = msg_id[0], msg_id[1]
    return id1, id2

def convert_to_gmt(local_time_str):
    local_time = datetime.strptime(local_time_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    gmt_offset = timedelta(hours=5, minutes=30)
    gmt_time = local_time + gmt_offset
    return gmt_time.strftime("%Y-%m-%d %H:%M:%S")

def retrieve_all_messages(chat_space_id):
    service = build('chat', 'v1', credentials=gkey)
    all_messages = []
    next_page_token = None
    while True:
        response = service.spaces().messages().list(
            parent=chat_space_id,
            pageSize=1000,
            pageToken=next_page_token
        ).execute()
        if 'messages' in response:
            all_messages.extend(response['messages'])
        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break
    return all_messages

# Export chat messages and update Google Sheet
newDF = export_chat_messages()
dataSheet = sheet.worksheet("title", "Chat Dump")
dataSheet.clear(start='A', end='H', fields='*')
dataSheet.set_dataframe(newDF, (2, 1), False)
logging.info("Chat Data Sheet Updated...!!!")

now = datetime.now()
now2 = 'Last updated at : ' + str(now.strftime("%d-%m-%y %H:%M:%S"))
dataSheet.update_value('A1', now2)
newDF.to_csv("newDF.csv", index=False)

# Connect to Snowflake and create table
wf1 = newDF.copy()
conn = snowflake_Connect()
wf1 = fix_date_cols(wf1)
logging.info("Shape of Retention Table - {}".format(wf1.shape[0]))

create_tbl_statement = "CREATE OR REPLACE TABLE adhoc_db.cle.google_chat_space_messages ("

for column in wf1.columns:
    if wf1[column].dtype.name == "int" or wf1[column].dtype.name == "int64":
        create_tbl_statement += f"{column} int"
    elif wf1[column].dtype.name == "object":
        create_tbl_statement += f"{column} varchar(16777216)"
    elif wf1[column].dtype.name == "datetime64[ns]":
        create_tbl_statement += f"{column} datetime"
    elif wf1[column].dtype.name == "float64":
        create_tbl_statement += f"{column} float8"
    elif wf1[column].dtype.name == "bool":
        create_tbl_statement += f"{column} boolean"
    else:
        create_tbl_statement += f"{column} varchar(16777216)"

    if wf1[column].name != wf1.columns[-1]:
        create_tbl_statement += ",\n"
    else:
        create_tbl_statement += ")"

conn.cursor().execute(create_tbl_statement)
logging.info("SF Table replaced from the report: 00O5j0000079VGoEAM")

wf1.columns = wf1.columns.str.upper()

# Grant permissions and write DataFrame to Snowflake table
for role in ["REPORTINGUSER", "ORGADMIN", "ACCOUNTADMIN", "CLE_USER"]:
    conn.cursor().execute(f'GRANT SELECT ON ALL TABLES IN SCHEMA "ADHOC_DB"."CLE" TO role {role}')
write_pandas(
    conn=conn,
    df=wf1,
    table_name='GOOGLE_CHAT_SPACE_MESSAGES',
    database='ADHOC_CHATS',
    schema='CKX'
)
conn.close()
logging.info("SF Table Created")

