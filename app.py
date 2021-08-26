"""
DESCRIPTION OF APP
Lets you add/remove/delete/update friends
"""

# Import Built-In Modules
import requests     # Does API calls to other APIS
import traceback    # Lets you print the error stack trace
import random       # Lets you get a random number
import sys          # Lets you use operating system functions
import os           # Lets you get information of the os Ex. os.path | Ex. os.environ

# Import Framework Modules
from flask import Flask             # Main Flask Class
from flask import jsonify           # Lets flask deliver json data
from flask import render_template   # Lets flask serve the htmml page
from flask import request           # Lets you view the requester info (HEADERS, Data, Status Code, etc.)


# Import Other Modules/Data in the App
from data import friends_list

# Gives all the powers of flask to app
# __name__ is a special method in python that refers to the file that is running
app = Flask(__name__)


# REST API

# VERB: GET - To retreive information | Can send data in the url | Insecure way of sending data | Normal use case: Search
# Response for a GET Request HAS TO RETURN DATA OR HTML

# Example of serving html
@app.route('/', methods=['GET'])
def home():
    return render_template('jHome.html')

# Example of serving json Data
@app.route('/getFriendsList', methods=['GET'])
def getFriendsList():
    try:
        user_name = 'Rakin'
        response = {'msg':'Successfully found friends list', 'data': friends_list, 'err':'', 'status': 'Success'}
    except Exception as e:
        print(str(e))
        print(traceback.format_exc())
        response = {'msg':'Failed to retrieve friends list!', 'data':'', 'err':str(e), 'status': 'Fail'}

    return jsonify(response)

# Example of serving json Data
@app.route('/getUserName', methods=['GET'])
def getUserName():
    try:
        user_name = 'Rakin'
        response = {'msg':'Successfully found user name', 'data': {'name': user_name}, 'err':'', 'status': 'Success'}
    except Exception as e:
        print(str(e))
        print(traceback.format_exc())
        response = {'msg':'Failed to retrieve user name!', 'data':'', 'err':str(e), 'status': 'Fail'}

    return jsonify(response)

# VERB: POST - To securely send data | Typically used to save a new data | Requires requester to send data in body
# Response for a POST Request HAS TO RETURN DATA

# Exampole of a basic POST Request
@app.route('/addFriend', methods=['POST'])
def newFriend():
    try:
        # Retrieve data from body of request
        data = request.json
        print('THIS IS WHERE YOU CHECK THAT DATA!')
        print(data)

        # Save data to DB

        # Create a nice consistent data format for what your api sends back
        response = {'msg':'Successfully added new friend', 'err':'', 'status': 'Success'}
    except Exception as e:
        print(str(e))
        print(traceback.format.exc())
        response = {'msg':'Failed to save new friend!', 'err':str(e), 'status': 'Fail'}

    return jsonify(response)

    
#--------------------------------------------------------------------
# Examples of Different Logic usecases


# Example of how to use Jinja2 to use Python logic in HTML
@app.route('/pyHome', methods=['GET'])
def pyHome():
    try:
        user_name = 'Faraz'
        # Render Template can pass in variables from python as extra arugments
        return render_template('pyHome.html', name=user_name, friends=friends_list['friends'])
    except Exception as e:
        print(str(e))
        print(traceback.format_exc())
        return render_template('404.html')

        

# Example of a basic Search
# Ex. 127.0.0.1/getFriendInfo?name=Faraz 
@app.route('/getFriendInfo', methods=['GET'])
def getFriendInfo():
    try:
        # Gets data from the URL arguments of the GET Request
        data = request.args.get('name')
        friendInfo = ''
        
        # Perform Search Operation inside friernds list for friend name
        for i in range(0, len(friends_list['friends'])):
            # Compare friend name to a name in the list
            if data == friends_list['friends'][i]['username']:
                friendInfo = friends_list['friends'][i]

        response = {'msg':'Successfully found friend info!', 'data': friendInfo , 'err':'', 'status': 'Success'}
    except Exception as e:
        print(str(e))
        print(traceback.format_exc())
        response = {'msg':'Failed to find friend"s info!', 'data':'', 'err':str(e), 'status': 'Fail'}
    
    return jsonify(response)


# Examples of API requests to other APIs
@app.route('/randomPicture', methods=['GET'])
def getPicture():
    try:
        # Gets data from the URL arguments of the GET Request
        searchItem = request.args.get('searchItem')

        # Do an api request to pexels api to get a set 5 weather picture data
        headers = {'Authorization': '563492ad6f91700001000001b1fa1bfe1439432aa3ae3a3519b786b0'}
        r = requests.get(f'https://api.pexels.com/v1/search?query={searchItem}&per_page=5', headers=headers)
        print(r.json(), file=sys.stderr)
        data = r.json()

        # Loop through weatherData to get the 5 pictures
        pics = []
        for i in range(0, len(data['photos'])):
            currentPic = data['photos'][i]['src']['original']
            pics.append(currentPic)
        
        # Generate random number to get a random pic out of pics
        rand = random.randint(0, 4)
        randomPic = pics[rand]
    
        response = {'msg':'Successfully found pictures!', 'data': randomPic , 'err':'', 'status': 'Success'}
    except Exception as e:
        print(str(e))
        print(traceback.format_exc())
        response = {'msg':'Failed to find pictures!', 'data':'', 'err':str(e), 'status': 'Fail'}
    
    return jsonify(response)



# The code below will only run if the person is running this file directly
# In other words if this file gets run by another file, the below won't run
if __name__ == '__main__':

    # Debug=True lets the app restart over and over | 
    # Custom Port allows for the app to be on a non conflicting port
    app.run(debug=True, port=7001)     
