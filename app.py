from flask import Flask
from user_controller import user_bp

app = Flask(__name__)
app.register_blueprint(user_bp)

@app.route('/home')
def home():
    return "This is Home Page"


if __name__ == "__main__":
    app.run(debug=True)
