from flask import Flask, jsonify, request, render_template
import random

app = Flask(__name__)

quotes = [
    {"id": 0, "quote": "We don't live alone. We are responsible for each other.", "character": "Inspector", "act": 3},
    {"id": 1, "quote": "I don't play golf.", "character": "Inspector", "act": 1}
]

def getQuoteNum():
    return random.randint(0, len(quotes) - 1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quote', methods=['GET'])
def getQuote():
    filter = request.args.get('filter')
    if not filter:
        number = getQuoteNum()
        quote_select = quotes[number]
        quote = quote_select['quote']
        character = quote_select['character']
        act = quote_select['act']
        return jsonify({"quote": quote, "character": character, "act": act})

    if filter == 'character':
        character = request.args.get('character')
        find_quotes = [quote for quote in quotes if quote['character'] == character]
        num_quote_select = random.randint(0, len(find_quotes) - 1)
        quote_select = find_quotes[num_quote_select]
        quote = quote_select['quote']
        character = quote_select['character']
        act = quote_select['act']
        return jsonify({"quote": quote, "character": character, "act": act})
    elif filter == 'act':
        act = request.args.get('act')
        find_quotes = [quote for quote in quotes if quote['act'] == int(act)]
        num_quote_select = random.randint(0, len(find_quotes) - 1)
        quote_select = find_quotes[num_quote_select]
        quote = quote_select['quote']
        character = quote_select['character']
        act = quote_select['act']
        return jsonify({"quote": quote, "character": character, "act": act})
    else:
        return jsonify({"quote": "Invalid filter. Quote not found.", "character": "Invalid filter. Character not found.", "act": "Invalid filter. Act not found."})
    

if __name__ == '__main__':
    app.run(port=1234)