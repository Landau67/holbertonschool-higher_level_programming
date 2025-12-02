#!/usr/bin/python3
"""
Basic Flask App with Jinja Templates
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Home page route"""
    return render_template('index.html')

@app.route('/about')
def about():
    """About page route"""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Contact page route"""
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
