from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello,Flask!"

@app.route("/about")
def about():
    return "This is my flask application"

@app.route("/contact")
def contact():
    return "This is contact page of my flask application"


if __name__== "__main__":
    app.run(debug=True)


