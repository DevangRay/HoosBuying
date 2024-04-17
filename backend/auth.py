import pymysql
import bcrypt
from db_users import connect
from flask import Flask, jsonify
from flask_cors import CORS
from markupsafe import escape
app = Flask(__name__)
CORS(app)

def checkToken(token):
    connection = connect()
    result = "GOT NOTHING PAL"
    with connection:
        with connection.cursor() as cursor:
        # call a stored procedure    
            cursor.callproc('auth_select', [token,])
            connection.commit()
            result = cursor.fetchall()
        
    if not result:
        return "Error: No Token Found", 401
    else:
        return "Success, Token Found", 200
    
    
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
    
def login(username, password):
    # check username/password is valid
    user = getUser(username)
    print("auth.py user is", user)
    db_password = user["password"]
    print(db_password)
    
    if not bcrypt.checkpw(str.encode(password),str.encode(db_password)):
        return f'password: {password}, is wrong', 401
    else:
        # ISSUE A TOKEN
        response = {
            "username" : username,
            "token" : "PROOF OF CONCEPT"

        }
        response = jsonify(response)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    return f'you are in login, {username}, {password}', 200
