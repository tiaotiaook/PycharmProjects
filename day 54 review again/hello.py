# client sever database

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/bye')
def say_bye():
    return 'bye'


if __name__ == "__main__":
    app.run(port =7000)