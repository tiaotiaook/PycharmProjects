from flask import Flask, render_template
import random
import datetime

# year = datetime.datetime.now()
# year_1 =year.strftime("%Y")




app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1,10)
    current_year = datetime.datetime.now().year
    return render_template("index.html",num=random_number,t=current_year)


if __name__ == "__main__":
    app.run(port =7001 ,debug=True)