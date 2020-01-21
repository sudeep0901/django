from application import app
from flask import request


@app.route('/')
def hello():
    return "Hello from Flask"


@app.route("/login/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "Login request received"
    else:
        return "please provide username and password"


# if __name__ == "__main__":
#     app.run()
