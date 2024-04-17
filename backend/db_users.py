import json
import pymysql
import requests
import bcrypt
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

@app.route('/getPostToken', methods=['GET'])
def send_post_token():
    dictToSend = {"token": "bad"}
    res = requests.post("http://127.0.0.1:5000/postToken", json=dictToSend)
    print("response from server", res.text)
    result = res.json()
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    
@app.route('/postToken', methods=['POST'])
def postToken():
    token = request.form
    connection = connect()
    result = "GOT NOTHING PAL"
    with connection:
        with connection.cursor() as cursor:
        # Create a new record
            cursor.execute("CALL auth_select(\"" + token + "\")")
            result = cursor.fetchall()
            # print("RESULT is ", result)

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    # connection.commit()
    if not result:
        return abort(401)
    else:
        return "Success", 200

@app.route('/getToken', methods=['GET'])
def getToken():
    connection = connect()
    result = "GOT NOTHING PAL"
    with connection:
        with connection.cursor() as cursor:
        # Create a new record
            cursor.execute("CALL auth_select(\"good\")")
            result = cursor.fetchall()
            # print("RESULT is ", result)

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    # connection.commit()
    if not result:
        return abort(401)
    else:
        return "Success", 200
    

def getUser(username):
    connection = connect()
    result = "GOT NOTHING PAL"
    with connection:
        with connection.cursor() as cursor:
        # Create a new record
            sql = f"SELECT * FROM `User` where username = \"{username}\""
            cursor.execute(sql)
            result = cursor.fetchone()
    return result

@app.route('/login', methods=['POST'])
def login():
    user = getUser(request.form['username'])
    print(user['password'])
    print(request.form["password"])
    if not bcrypt.checkpw(str.encode(request.form["password"]),str.encode(user['password'])):
        abort(401,"FUCK YOU DEVANG")


# ISSUE A TOKEN
    response = {
        "username" : user['username'],
        "token" : "PROOF OF CONCEPT"

    }
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response


if __name__ == '__main__':
   app.run(port=5000)
#    print("IN MAIN")
#    connection = connect()
#    getRecord(connection)