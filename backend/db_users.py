import json
import pymysql
import requests
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


def connect():
    connection = pymysql.connect(
        host="34.145.170.154", 
        user="website", 
        password="websitepassword", 
        database= "HoosBuying",
        cursorclass=pymysql.cursors.DictCursor
    )
    if connection:
        return connection
    else:
        return "Connection Error", 404


@app.route('/getAllUsers', methods=['GET'])
def getAllUsers():
    connection = connect()
    result = "GOT NOTHING PAL"
    with connection:
        with connection.cursor() as cursor:
        # Create a sql statement
            sql = "SELECT * FROM `User`"
            cursor.execute(sql)
            result = cursor.fetchall()

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    # connection.commit()
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# TEST FUNCTION ONLY
@app.route('/testPostToken', methods=['GET'])
def testPostToken():
    dictToSend = {"token": "good"}
    res = requests.post("http://127.0.0.1:5000/postToken", json=dictToSend)
    if res.status_code == 200:
        return "Succesfully retrieved token", 200
    elif res.status_code == 401:
        return "Did not retrieve token", 401
    else:
        return "Uncontrolled error, likely a bug"
    
    
@app.route('/postToken', methods=['POST'])
def checkToken():
    token = request.json['token']
    
    connection = connect()
    result = "GOT NOTHING PAL"
    with connection:
        with connection.cursor() as cursor:
        # call a stored procedure
            cursor.callproc('auth_select', [token,])
            result = cursor.fetchall()
        
    if not result:
        return "Error: No Token Found", 401
    else:
        return "Success, Token Found", 200

    
if __name__ == '__main__':
   app.run(port=5000)