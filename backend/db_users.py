import pymysql
import requests
import auth
from flask import Flask, jsonify, request
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

@app.route('/auth/<path:subpath>', methods=['GET', 'POST'])
def control_auth(subpath):

    if subpath == "checkToken":
        token = request.json['token']
        return auth.checkToken(token)
    
    # returns a dictionary with 'token' and 'username' keys
    elif subpath == "login":
        print(request.json)
        username = request.json["username"]
        password = request.json["password"]
        return auth.login(username, password)
    else:
        return "Found no endpoint in auth"


# TEST FUNCTION ONLY
@app.route('/testPostToken', methods=['GET'])
def testPostToken():
    dictToSend = {"token": "good"}
    print("sending to control function")
    res = requests.post("http://127.0.0.1:5000/auth/checkToken", json=dictToSend)
    print(res)
    if res.status_code == 200 or res.status_code == 401:
        return res.text, res.status_code
    else:
        return "Uncontrolled error, likely a bug", 404
    
@app.route('/testLogin', methods=['GET'])
def testLogin():
    dictToSend = {
        "username": "pony_boy",
        "password": "password"
        }
    
    res = requests.post("http://127.0.0.1:5000/auth/login", json=dictToSend)
    print("testLogin response is", res)
    if res.status_code == 200 or res.status_code == 401:
        return res.text, res.status_code
    else:
        return "Uncontrolled error, likely a bug", 404

  
if __name__ == '__main__':
   app.run(port=5000)