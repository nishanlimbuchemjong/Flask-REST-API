from flask import Blueprint

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/user/signup')
def signup():
    return "This is SignUp Page"
