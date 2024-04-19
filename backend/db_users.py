from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))
print("db_users sys_path is", sys.path)

import pymysql
import requests
import endpoints.auth as auth
import endpoints.tags as tags
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/getAllUsers', methods=['GET'])
def control_all_users():
    return auth.getAllUsers()


@app.route('/auth/<path:subpath>', methods=['GET', 'POST'])
def control_auth(subpath):
    if subpath == "checkToken":
        token = request.json['token']
        return auth.checkToken(token)
    
    # returns a dictionary with 'token' and 'username' keys
    elif subpath == "login":
        print("in auth/login with request", request)
        print("request.form is", request.form)
        print("user", request.form['username'])
        print("password", request.form['password'])
        username = request.form["username"]
        password = request.form["password"]
        return auth.login(username, password)
    else:
        return "Found no endpoint in auth"
    
@app.route('/tags/', methods=['GET'])
def control_tags():
    return tags.getAllTags()


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