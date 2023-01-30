#!/usr/bin/python3
'''A minimal Flask Application'''
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''home'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Display hbnb'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    '''Display C <text>'''
    text = text.replace("_", " ")
    return 'C {}'.format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    '''Display Python <text> or Python is cool'''
    text = text.replace("_", " ")
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    '''Display an integer <n>'''
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    '''Render a HTML template'''
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    '''Render a HTML template'''
    body = 'odd'
    if n % 2 == 0:
        body = 'even'
    return render_template('6-number_odd_or_even.html', number=n, body=body)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
