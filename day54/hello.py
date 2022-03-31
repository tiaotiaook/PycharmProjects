from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'



@app.route("/bye")
def bye():
    return "Bye!"


@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}!"


if __name__ == "__main":
    app.run(debug=True)







# from flask import Flask
# app = Flask(__name__)
#
# print(__name__)
#
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
#
#
# if __name__ == "main":
#     app.run()