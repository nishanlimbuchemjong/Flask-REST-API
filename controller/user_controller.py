from flask import Blueprint
from model.user_model import User_Model

obj = User_Model()

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/user/getall')
def user_get_all():
    print("Output: ", obj)
    return obj.user_get_all_model()
