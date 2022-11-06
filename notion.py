from flask import Flask
import os
from notion_client import Client
from pprint import pprint
import json



notion = Client(auth="secret_316i3ulvc65n99gX9WwZcmwlDygapkpIbkW3LgR5WRA")


app = Flask(__name__)

@app.route('/notion', methods=["GET"])
def query():
    database_id = "18e1c8be085940c2a9db59497af63601"
    my_page = notion.databases.query(
        **{
            "database_id": database_id,
            "filter": {
                "property": "Name",
                "rich_text": {
                    "equals": "Imju"
                }
            },
        }                
    )
    print("1st page id:",my_page["results"][0]["id"])

    # Create a new page
    your_name = "Hello"
    new_page = {
        "Name": {"title": [{"text": {"content": your_name}}]},
        "Tags": {"type": "multi_select", "multi_select": [{"name": "API"}]},
            }
    notion.pages.create(parent={"database_id": database_id}, properties=new_page)   
    return my_page