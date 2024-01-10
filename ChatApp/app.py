from flask import Flask
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return 'Hello TeamF!!!'

if __name__ == "__main__":
    app.run(host="0.0.0.0")
