from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))
print(sys.path)

from backend.endpoints.connector import connect
from flask import jsonify

def getAllConvoIds(user_id):
    connection = connect()
    result = "GOT NOTHING PAL"
    with connection:
        with connection.cursor() as cursor:
        # Create a new record
            cursor.execute("SELECT c.*, u.username as host_user, u.fname as host_fname, u.lname as host_lname, u.computing_id as host_cid, u2.username as cust_user, u2.fname as cust_fname, u2.lname as cust_lname, u2.computing_id as cust_cid, l.title, l.price, l.status_id , s.status_name FROM Conversation c join `User` u on c.host_id = u.uid join `User` u2 on c.customer_id =u2.uid join Listings l on c.listing_id = l.listing_id  join Status s on l.status_id = s.status_id WHERE host_id = %s OR customer_id = %s;", (user_id, user_id, ))
            result = cursor.fetchall()
    return result
    # print(type(result))
    # for value in result:
    #     print("value is", value)
    # response = jsonify(result)
    # response.headers.add('Access-Control-Allow-Origin', '*')
    # return response

def getAllConversations(user_id):
    convo_arr = getAllConvoIds(user_id)
    
    connection = connect()
    with connection:
        with connection.cursor() as cursor:
            # Create a new record
            for i in range(len(convo_arr)):
                cursor.execute("select * from Message m where convo_id = %s", (convo_arr[i]["convo_id"], ))
                message_arr = cursor.fetchall()
                convo_arr[i]["message_array"] = message_arr
                
    response = jsonify(convo_arr)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

def addNewMessage(convo_id, user_id, text):
    connection = connect()
    result = "GOT NOTHING PAL"
    with connection:
        with connection.cursor() as cursor:
        # Create a new record
            cursor.execute("INSERT INTO Message (`time`, `text`, convo_id, author_id) VALUES (NOW(), %s, %s, %s)", (text, convo_id, user_id))
            connection.commit()
            result = cursor.fetchall()
      
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response