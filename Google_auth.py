import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pygsheets as pg

# Define the Google API scopes for Google Drive, Classroom, Gmail, Chat
SCOPES = [
    "https://www.googleapis.com/auth/contacts.readonly",
    "https://www.googleapis.com/auth/chat.spaces.readonly",
    "https://www.googleapis.com/auth/chat",
    "https://www.googleapis.com/auth/chat.messages",
    "https://www.googleapis.com/auth/chat.messages.readonly",
    "https://www.googleapis.com/auth/chat.memberships",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/classroom.announcements",
    "https://www.googleapis.com/auth/classroom.courses",
    "https://www.googleapis.com/auth/classroom.coursework.me",
    "https://www.googleapis.com/auth/classroom.coursework.students",
    "https://www.googleapis.com/auth/classroom.courseworkmaterials",
    "https://www.googleapis.com/auth/classroom.guardianlinks.me.readonly",
    "https://www.googleapis.com/auth/classroom.guardianlinks.students",
    "https://www.googleapis.com/auth/classroom.profile.emails",
    "https://www.googleapis.com/auth/classroom.profile.photos",
    "https://www.googleapis.com/auth/classroom.push-notifications",
    "https://www.googleapis.com/auth/classroom.rosters",
    "https://www.googleapis.com/auth/classroom.student-submissions.me.readonly",
    "https://www.googleapis.com/auth/classroom.student-submissions.students.readonly",
    "https://www.googleapis.com/auth/classroom.topics",
]

# File paths
service_file = "TeacherCommunity.json"
token_file = "tc.json"
current_dir = os.getcwd()
service_key_path = os.path.join(current_dir, service_file)
token_path = os.path.join(current_dir, token_file)

# Authenticate & Refresh Token
def authenticate():
    """
    Authenticates with Google Workspace and returns the credentials.
    """
    # Check if token.json file exists and contains valid credentials.
    creds = None

    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file, SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                service_key_path,
                SCOPES,
            )
            creds = flow.run_local_server(
                port=0, prompt="consent", authorization_prompt_message=""
            )

        # Save the credentials for the next run
        with open(token_file, "w") as token:
            token.write(creds.to_json())
    return creds

# Authenticate and obtain credentials
gkey = authenticate()

# Build Google services
gs = pg.authorize(custom_credentials=gkey)
people = build("people", "v1", credentials=gkey)
chat = build("chat", "v1", credentials=gkey)
gcrm = build("classroom", "v1", credentials=gkey)
