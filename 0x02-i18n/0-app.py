#!/usr/bin/env python3
"""
A basic Flask application.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Route for the index page."""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
