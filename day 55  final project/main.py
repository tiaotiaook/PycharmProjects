from flask import Flask
import random

number = random.randint(0,9)

print(number)


app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>guess a number between 0 and 9 </h1>' \
           '<img src="https://media2.giphy.com/media/YRVP7mapl24G6RNkwJ/giphy.gif?cid=ecf05e474erpefiw9cduks3jqhjmqwr2btm0415dagp31my8&rid=giphy.gif&ct=g">'


@app.route('/<int:guess>')

def guess(guess):
    if guess > number:
        return '<h1>too high</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'

    elif guess < number:
        return '<h1>too low</h1>'\
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif guess == number:
        return '<h1>you are right</h1>'\
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'







if __name__ == "__main__":
    app.run(port =7000 ,debug=True)