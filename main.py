from flask import Flask
from dune import execute_query
from dune import execute_query_with_params
from dune import get_query_results
from dune import get_query_status
import time
import os
from pprint import pprint
import json





app = Flask(__name__)

@app.route('/', methods=["GET"])
def get_query():
    execution_id = execute_query(1530879)#, params = {"Period" : ["1 hour", "4 hour", "12 hour", "24 hour"], "USD amount per transaction" : [500, 1000, 5000, 10000]})
    #print(execution_id)
    #print(time.time())
    while True:
        response = get_query_status(execution_id)
    
        #print(response)
        response_status = response.json()['state']
        
        if response_status == 'QUERY_STATE_COMPLETED':
            data = get_query_results(execution_id).json()
            #print(time.time())
            return data
        elif response_status == 'QUERY_STATE_EXECUTING':
            time.sleep(.25)
        else: 
            return response_status
if __name__ == '__main__':
    app.run()
