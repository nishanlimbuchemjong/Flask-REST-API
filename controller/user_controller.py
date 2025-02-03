from flask import Blueprint
from model.user_model import User_Model

obj = User_Model()

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/user/signup')
def signup():
    return obj.user_signup_model()
