#from msilib import schema
import psycopg2
import pygsheets as pg
import snowflake.connector as sc
from datetime import datetime
import pandas as pd
import os

def connect_to_snowflake():
    """
    Connects to Snowflake and returns the connection context.
    """
    ctx = sc.connect(
        user='user123',
        password='NJnj1234@@',
        account='su676.ap-south-1.aws',
        warehouse='cxf_wh',
        database='adhoc',
        schema='CXF',
        role='USER'
    )
    return conn

def main():
    # Connect to Snowflake
    snowflake_conn = connect_to_snowflake()
    
    # Further code execution...
    # Add your code here

if __name__ == "__main__":
    main()
