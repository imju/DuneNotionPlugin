from flask import Flask
import os
from notion_client import Client
import json
from datetime import datetime



notion = Client(auth=os.getenv('NOTION_API_KEY'))


app = Flask(__name__)

def query(database_id: str):
    my_page = notion.databases.query(
        **{
            "database_id": database_id,
        }                
    )

    # Create a new page
    '''
    your_name = "Hello"
    new_page = {
        "Name": {"title": [{"text": {"content": your_name}}]},
        "Tags": {"type": "multi_select", "multi_select": [{"name": "API"}]},
            }
    notion.pages.create(parent={"database_id": database_id}, properties=new_page)   
    '''
    return my_page

def add_trx_rows(database_id: str, trx_data:dict):
    rows = trx_data['result']['rows']

    for row in rows:
        new_page = {
            "Wallet Address": {"title": [{"text": {"content": row["tx_from"]}, "plain_text":row["tx_from"]}]},
            "Number of Transactions": {"number": row["total_count"]},
            "Total USD Transacted": {"number": row["total_usd_volume"]},
            "Average Value Transacted": {"number": row["avg_trade_volume"]},
            }

        notion.pages.create(parent={"database_id": database_id}, properties=new_page)

       



def create_db(parent_id: str):

    """
    parent_id(str): ID of the parent page
    """
    db_name = "Top 10 Whale Transactions last 4 hours at "+ datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    print(f"\n\nCreate database '{db_name}' in page {parent_id}...")
    properties = {
        "Wallet Address": {"title": {}},  # This is a required property
        "Number of Transactions": {"number": {"format": "number"}},
        "Total USD Transacted": {"number": {"format": "dollar"}},
        "Average Value Transacted": {"number":{"format": "dollar"}},
    }
    title = [{"type": "text", "text": {"content": db_name}}]
    icon = {"type": "emoji", "emoji": "🎉"}
    parent = {"type": "page_id", "page_id": parent_id}
    return notion.databases.create(
        parent=parent, title=title, properties=properties, icon=icon
    )    

