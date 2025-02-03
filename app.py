from flask import Flask
from controller.user_controller import user_bp
from controller.product_controller import product_bp

app = Flask(__name__)
app.register_blueprint(user_bp)
app.register_blueprint(product_bp)

@app.route('/home')
def home():
    return "This is Home Page"


if __name__ == "__main__":
    app.run(debug=True)
