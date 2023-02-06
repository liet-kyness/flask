# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route('/math/<op>')
def get_math(op):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operators[op](a,b)
    return str(result)

