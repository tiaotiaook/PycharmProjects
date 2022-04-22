from flask import Flask
import random

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

    elif guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)







# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route('/')
# def hello_world():
#     return '<h1 style="text-align: center">Hello, World!<h1>' \
#            '<p>This is a paragraph.</p>'\
#            '<img src="https://media4.giphy.com/media/Puc4FZWExJc0E/giphy.gif?cid=ecf05e47j3jude0sqvl7t3i0amsxswgvn0oq9caoddsx733d&rid=giphy.gif&ct=g" width=200>'
#
#
#
# @app.route("/bye")
# @make_bold
# @make_emphasis
# @make_underlined
#
# def say_bye():
#     return "<u><em><b>Bye!</b></em></u>"
#
#
# @app.route("/username/<name>/<int:number>")
# def greet(name,number):
#     return f"Hello there {name}, you are {number} years old!"
#
# if __name__ == "__main__":
#     app.run(debug=True)