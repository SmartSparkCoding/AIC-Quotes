from flask import Flask, jsonify, request, render_template
import random

app = Flask(__name__)

quotes = [
    {"id": 0, "quote": "We don't live alone. We are responsible for each other.", "character": "Inspector Goole", "act": 3},
    {"id": 1, "quote": "I don't play golf.", "character": "Inspector Goole", "act": 1}
]

def getQuoteNum():
    return random.randint(0, len(quotes) - 1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quotes', methods=['GET'])
def get_quotes():
    number = getQuoteNum()
    quote_select = quotes[number]
    quote = quote_select['quote']
    character = quote_select['character']
    act = quote_select['act']
    return jsonify({"quote": quote, "character": character, "act": act})

if __name__ == '__main__':
    app.run(port=1234)