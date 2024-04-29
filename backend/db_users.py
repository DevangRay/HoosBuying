from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))
print("db_users sys_path is", sys.path)

import requests
import endpoints.auth as auth
import endpoints.tags as tags
import endpoints.listings as listings
import endpoints.conversation as conversation
import endpoints.images as images
from flask import Flask, request
from flask_cors import CORS
from fileinput import filename

app = Flask(__name__)
CORS(app)

@app.route('/getAllUsers', methods=['GET'])
def control_all_users():
    return auth.getAllUsers()


@app.route('/auth/<path:subpath>', methods=['POST'])
def control_auth(subpath):
    if subpath == "checkToken":
        token = request.form['token']
        return auth.checkToken(token)
    
    elif subpath == "getPassword":
        username = request.form["username"]
        return auth.getUserPassword(username)
    
    # returns a dictionary with 'token' and 'username' keys
    elif subpath == "login":
        # print("in auth/login with request", request)
        # print("request.form is", request.form)
        # print("user", request.form['username'])
        # print("password", request.form['password'])
        username = request.form["username"]
        password = request.form["password"]
        return auth.login(username, password)

    # Returns success or failure creating new account
    elif subpath == "register":
        username = request.form["username"]
        password = request.form["password"]
        fname = request.form["fname"]
        lname = request.form["lname"]
        computing_id = request.form["computing_id"]
        address = request.form["address"]
        phone_number = request.form["phone_number"]
        print("in auth register")

        return auth.register(username,password,fname,lname,computing_id,address,phone_number)
    else:
        return "Found no endpoint in auth"
    
@app.route('/tags/', methods=['GET'])
def control_tags():
    return tags.getAllTags()

@app.route('/listings/get/<int:listing_id>', methods=['GET'])
def control_get_one_listing(listing_id):
    return listings.getOneListing(listing_id)

@app.route('/listings/filter/<int:id>', methods=['GET'])
def control_listings_filter(id):
    return listings.filterByTags(id)

@app.route('/listings/filter', methods=['POST'])
def post_control_listings_filter():
    # print("REQUEST.JSON IS FOR FILTER LISTINGS", request.json, request, request.form)
    if (request.json) :
        tag_array = request.json
        return listings.filterByTags(tag_array)    
    else:
        return listings.getAllListings()

@app.route('/listings/<path:subpath>', methods=['GET', 'POST'])
def control_listings(subpath):
    if subpath == "getAll":
        return listings.getAllListings()
    elif subpath == "insert":
        description = request.form["description"]
        status_id = request.form["status_id"]
        delivery_id = request.form["delivery_id"]
        owner_uname = request.form["owner_uname"]
        title = request.form["title"]
        price = request.form["price"]
        tag_id = request.form["tag_id"]
        return listings.insertListing(description, status_id, delivery_id, owner_uname, title, price, tag_id)
    elif subpath == "update":
        listing_id = request.form["listing_id"]
        dict = request.form
        return listings.updateListing(dict, listing_id=listing_id), 200
    else:
        return "Found no endpoint in auth"
    
@app.route('/conversations/<path:subpath>/<int:user_id>', methods=['GET', 'POST'])
def control_get_conversations(subpath, user_id):
    if subpath == "getAll":
        return conversation.getAllConversations(user_id)
    elif subpath == "getOwner":
        return conversation.getOwnerConversations(user_id)
    elif subpath == "getCustomer":
        return conversation.getCustomerConversations(user_id)
    else:
        return "Found no endpoint in auth"
    
@app.route('/conversations/<path:subpath>', methods=['GET', 'POST'])
def control_conversations(subpath):
    if subpath == "insert":
        conversation_id = request.form["conversation_id"]
        user_id=request.form["user_id"]
        message = request.form["message"]
        return conversation.addNewMessage(conversation_id, user_id, message)
    else:
        return "Found no endpoint in auth"



@app.route('/images/<int:listing_id>', methods=['GET'])
def control_get_images_by_listing(listing_id):
    return images.getImagesByListing(listing_id)

@app.route('/images/id/<img_path>', methods=['GET'])
def control_get_image(img_path):
    return images.getImage(img_path)

@app.route('/images/upload', methods=['POST'])
def control_image_post():
     return images.uploadImage(request)
 
@app.route('/user/<path:subpath>', methods=['POST'])
def control_single_user(subpath):
     if subpath == "getUserInfo":
         print("request is", request.form)
         username = request.form["username"]
         print("youre in the right place", username)
         return auth.getUserProfile(username)
     elif subpath == "update":
         print("request is", request.form)
         fname = request.form["fname"]
         lname = request.form["lname"]
         computing_id = request.form["computing_id"]
         phone_number = request.form["phone_number"]
         address = request.form["address"]
         
         return auth.updateUser(fname, lname, computing_id, phone_number, address)
     elif subpath == "updatePassword":
         computing_id = request.form["computing_id"]
         new_hashed_password = request.form["password"]
         
         return auth.updateUserPassword(computing_id, new_hashed_password)
     
     
     
# TEST FUNCTION ONLY
# @app.route('/testPostToken', methods=['GET'])
# def testPostToken():
#     dictToSend = {"token": "good"}
#     print("sending to control function")
#     res = requests.post("http://127.0.0.1:5000/auth/checkToken", json=dictToSend)
#     print(res)
#     if res.status_code == 200 or res.status_code == 401:
#         return res.text, res.status_code
#     else:
#         return "Uncontrolled error, likely a bug", 404
    
# @app.route('/testListingFilter', methods=['GET'])
# def testListingFilter():
#     array = [1, 8]
#     print("sending to control function")
#     res = requests.post("http://127.0.0.1:5000/listings/filter", json=array)
#     print("testListingFilter result is", res)
#     if res.status_code == 200 or res.status_code == 401:
#         return res.text, res.status_code
#     else:
#         return "Uncontrolled error, likely a bug", 404
    
# @app.route('/testLogin', methods=['GET'])
# def testLogin():
#     dictToSend = {
#         "username": "pony_boy",
#         "password": "password"
#         }
    
#     res = requests.post("http://127.0.0.1:5000/auth/login", json=dictToSend)
#     print("testLogin response is", res)
#     if res.status_code == 200 or res.status_code == 401:
#         return res.text, res.status_code
#     else:
#         return "Uncontrolled error, likely a bug", 404

  
if __name__ == '__main__':
   app.run(port=5000)