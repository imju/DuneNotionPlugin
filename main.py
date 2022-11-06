from flask import Flask, render_template, request, redirect, url_for
from dune import execute_query
from dune import get_query_results
from dune import get_query_status
import time


app = Flask(__name__)

@app.route('/get_db/<string:pageID>', methods=["GET"])
def get_query(pageID:str):
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

@app.route('/get_db', methods =["POST", "GET"])
def web_page_interactions():
    if request.method == "POST":
        ID = request.form["pageID"]
        redirect(url_for("pageID", pageID=ID))
    else: 
        return render_template('template1.html')

if __name__ == '__main__':
    app.run()


