from flask import Blueprint

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/product/add')
def product_add():
    return "This is Product Add Page"
