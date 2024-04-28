from pathlib import Path
import sys,os
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))
print("PATHROOT  ",path_root)
print(sys.path)

import base64
from backend.endpoints.connector import connect
from flask import jsonify,send_file, make_response

BACKEND_PATH = path_root = Path(__file__).parents[1]
IMG_FOLDER = os.path.join(BACKEND_PATH,"images")

def getImagesByListing(listing_id):
    connection = connect()
    result = "GOT NOTHING PAL"
    with connection:
        with connection.cursor() as cursor:
        # Create a new record
            cursor.execute("SELECT * from Images where listing_id = %s", (listing_id))
            result = cursor.fetchall()
    return result


# CHANGE TO listing_id.imgOrder#
# Only works for JPEG
def getImage(image_id):
    try:
        
        filename = str(image_id)+".jpg"
        file_path = os.path.join(IMG_FOLDER, filename)
        if os.path.isfile(file_path):
            # return send_file(file_path, mimetype='image/jpeg',as_attachment=True)
            with open(file_path, "rb") as f:
                image_binary = f.read()

                response = make_response(base64.b64encode(image_binary))
                response.headers.set('Content-Type', 'image/jpeg')
                response.headers.set('Content-Disposition', 'attachment', filename=filename)
                return response
        else:
            return f'Image not found', 404
    except Exception as e:
        print(str(e))
        return f"Error: {str(e)}", 500
    
    # return null

def uploadImage(request):
    if request.method == 'POST':   
        f = request.files['file'] 
        f.save( os.path.join(IMG_FOLDER,f.filename))   
        return 'Success', 200