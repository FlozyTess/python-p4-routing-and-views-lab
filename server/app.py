#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# a simple homepage route
@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

# route that prints a string in the console and returns it in the browser
@app.route('/print/<string:text>')
def print_string(text):
    print(text)
    return (text ) 

# route that counts numbers up to a given number
@app.route('/count/<int:num>')
def count(num):
    return "\n".join(str(i) for i in range(num)) +"\n"
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation!", 400

    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
