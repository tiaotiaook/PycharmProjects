# client sever database

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="text-align:center">Hello, World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://media2.giphy.com/media/YRVP7mapl24G6RNkwJ/giphy.gif?cid=ecf05e474erpefiw9cduks3jqhjmqwr2btm0415dagp31my8&rid=giphy.gif&ct=g">'


@app.route('/bye')


def say_bye():
    return 'bye'

# add variable sections to a URL by marking sections with <variable_name>

@app.route('/username/<name>/<int:number>')
def greet(name,number):
    return f"Hello {name}, you are {number} years old!"


if __name__ == "__main__":
    app.run(port =7000 ,debug=True)