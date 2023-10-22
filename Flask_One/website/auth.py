from flask import Blueprint
from.model import UserModel
import json
from flask import make_response
auth = Blueprint('auth', __name__)
obj = UserModel()

@auth.route('/login')
def login():
    "sddsd"
    return "<h1>Login Here</h1>"



@auth.route('/logout')
def logout():
    return "<h1>Logout Here</h1>"



@auth.route('/signup')
def signup():
    
    return obj.Regestration()

@auth.route('/details')
def user_details():
    return  obj.users_details()

@auth.route('/profile')
def profile():
    return "Profile"



