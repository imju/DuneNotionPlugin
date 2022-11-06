from flask import Flask, render_template, request, redirect, url_for
from dune import execute_query
from dune import get_query_results
from dune import get_query_status
import time
import os
from pprint import pprint
import json
import notion





app = Flask(__name__)

@app.route('/query', methods=["GET"])
def get_query():
    execution_id = execute_query(1530879)
    while True:
        response = get_query_status(execution_id)
    
       
        response_status = response.json()['state']
        
        if response_status == 'QUERY_STATE_COMPLETED':
            data = get_query_results(execution_id).json()
            
            return data
        elif response_status == 'QUERY_STATE_EXECUTING':
            time.sleep(.25)
        else: 
            return response_status


@app.route('/', methods=["GET"])
def hello():
    return "Let's get whale data"

@app.route('/create_db/<string:parent_id>', methods=["GET"])
def create_db(parent_id:str):
    return notion.create_db(parent_id)

@app.route('/load_mock_data/<string:database_id>',  methods=["GET"])
def get_mock_data(database_id:str):
    data = {}
    with open('data.json') as json_file:
        data = json.load(json_file)
    notion.add_trx_rows(database_id, data)
    return "Transaction data is loaded"

@app.route('/cr_load_mock_db/<string:parent_id>', methods=["GET"])
def create_load_mock_db(parent_id:str):
    db = notion.create_db(parent_id)
    print("DB created:"+db["id"])

    with open('data.json') as json_file:
        data = json.load(json_file)
    notion.add_trx_rows(db["id"], data)
    return "DB created and Transaction data is loaded"

@app.route('/create_whale_db/<string:parent_id>', methods=["GET"])
def create_whale_db(parent_id:str):
    db = notion.create_db(parent_id)

    data=get_query()
 
    notion.add_trx_rows(db["id"], data)
    return "DB created, Dune data is returned and Transaction data is loaded"


@app.route('/query_db/<string:database_id>', methods=["GET"])
def query_db(database_id:str):
    return notion.query(database_id)

if __name__ == '__main__':
    app.run()


