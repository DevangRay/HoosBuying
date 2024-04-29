from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))
# print(sys.path)

from backend.endpoints.connector import connect
from flask import jsonify


def getAllTags():
    connection = connect()
    result = "GOT NOTHING PAL"
    with connection:
        with connection.cursor() as cursor:
        # Create a new record
            sql = f"SELECT * FROM Tags"
            cursor.execute(sql)
            result = cursor.fetchall()
            
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response