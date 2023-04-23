from flask import current_app, render_template,jsonify
from flask.globals import request
from passlib.hash import pbkdf2_sha256 as hasher

def take_data():
    addData_json = request.get_json()
    data = addData_json.get('data')
    db = current_app.config['db']
    result = db.delete_data(data[0])
    return(jsonify(result))


def take_list():
    addData_json = request.get_json()
    username = addData_json.get('user')
    db = current_app.config['db']
    list = db.get_list(username)
    return (jsonify(list))

def get_user():
    addData_json = request.get_json()
    username = addData_json.get('username')
    password_ = addData_json.get('password')
    db = current_app.config['db']
    user_password = db.get_user(username)
    if(user_password):
        success = hasher.verify(password_, user_password[0][2])
        return jsonify(success)  
    else:
        return jsonify(False)

def add_user():
    addData_json = request.get_json()
    username = addData_json.get('username')
    password_ = addData_json.get('password')
    hashed = hasher.hash(password_)
    db = current_app.config['db']
    success = db.add_user(username, hashed)
    return jsonify(success)


def add_data():
    addData_json = request.get_json()
    username = addData_json.get('username')
    password = addData_json.get('password')
    application = addData_json.get('application')
    user = addData_json.get('user')
    db = current_app.config['db']
    db.addData(username, password, application,user)
    return jsonify(True)

def index():
    return current_app.send_static_file('index.html')