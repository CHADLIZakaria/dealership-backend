from flask import Flask
from flask_cors import CORS
from flask import send_from_directory

app = Flask("Product deal check")
CORS(app)


@app.route("/")
def getHomePage():
    return {"data": "work fine"}


if __name__ == "__main__":
    app.run(port=5001, debug=True)
