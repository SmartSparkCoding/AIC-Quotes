from flask import Flask, jsonify, request, render_template
import random

app = Flask(__name__)

quotes = [
    {"id": 1, "quote": "We don't live alone. We are responsible for each other.", "character": "Inspector Goole", "act": 3},
    {"id": 2, "quote": "I don't play golf.", "character": "Inspector Goole", "act": 1}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quotes', methods=['GET'])
def get_quotes():
    