from flask import Blueprint
from model.user_model import User_Model
from flask import request
obj = User_Model()

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/user/getall')
def user_get_all():
    return obj.user_get_all_model()

@user_bp.route('/user/add', methods=['POST'])
def add_users():
    print(request.form)
    return obj.user_add_model(request.form)

