import json
import pymysql
import requests
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


def connect():
    # Please fill in these values.
    # project_id = "cs4750db-413417"
    print("IN CONNECT")
    connection = pymysql.connect(
        host="34.145.170.154", 
        user="website", 
        password="websitepassword", 
        database= "HoosBuying",
        cursorclass=pymysql.cursors.DictCursor
    )
    print("CONNECTION TO RETURN IS", connection)
    return connection


@app.route('/getAllUsers', methods=['GET'])
def getAllUsers():
    connection = connect()
    result = "GOT NOTHING PAL"
    with connection:
        with connection.cursor() as cursor:
        # Create a new record
            sql = "SELECT * FROM `User`"
            cursor.execute(sql)
            result = cursor.fetchall()
            # print("RESULT is ", result)

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    # connection.commit()
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/testPostToken', methods=['GET'])
def testPostToken():
    dictToSend = {"token": "good"}
    res = requests.post("http://127.0.0.1:5000/postToken", json=dictToSend)
    # print("response from server is", res, res.status_code)
    if res.status_code == 200:
        return "successful get token", 200
    else:
        return "bad get token", 401
    
    
@app.route('/postToken', methods=['POST'])
def checkToken():
    token = request.json['token']
    print("token issss", token)
    
    connection = connect()
    result = "GOT NOTHING PAL"
    with connection:
        with connection.cursor() as cursor:
        # Create a new record
            cursor.callproc('auth_select', [token,])
            result = cursor.fetchall()
        
    if not result:
        return "bad post token", 401
    else:
        return "Success post token", 200

    
if __name__ == '__main__':
   app.run(port=5000)
#    print("IN MAIN")
#    connection = connect()
#    getRecord(connection)