from flask import Blueprint

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return "<h1>Home Page</h>"

@views.route('/home')
def hello():
    return "<h1>hello Flask </h1>"