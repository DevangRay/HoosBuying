import json
import pymysql
import requests
from db_users import connect
from flask import Flask, jsonify, abort, request
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


    
if __name__ == '__main__':
   app.run(port=5000)