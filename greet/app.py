from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return "welcome"

@app.route('/welcome/<where>')
def welcome_where(where):
    return f"welcome {where}"

