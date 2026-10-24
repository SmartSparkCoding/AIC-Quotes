from flask import Flask, jsonify, request, render_template
import random

app = Flask(__name__)

quotes = [
    {"id": 0, "quote": "We don't live alone. We are responsible for each other.", "character": "inspector", "act": 3},
    {"id": 1, "quote": "I don't play golf.", "character": "inspector", "act": 1},
    {"id": 2, "quote": "A man has to mind his own business and look after himself and his own.", "character": "arthur", "act": 1},
    {"id": 3, "quote": "When you're married you'll realise that men with important work to do sometimes have to spend nearly all their time and energy on their business", "character": "sybil", "act": 1},
    {"id": 4, "quote": "But these girls aren't cheap labour - they're people.", "character": "sheila", "act": 1},
    {"id": 5, "quote": "Why shouldn't they try to higher wages? We try for the highest possible prices.", "character": "eric", "act": 1},
    {"id": 6, "quote": "I'm rather more - upset - by this business than I probably appear to be.", "character": "gerald", "act": 1},
    {"id": 7, "quote": "I'm a public man.", "character": "arthur", "act": 2},
    {"id": 8, "quote": "Girls of that class.", "character": "sybil", "act": 2},
    {"id": 9, "quote": "You and I aren't the same people who sat down to dinner here.", "character": "sheila", "act": 2},
    {"id": 10, "quote": "You're begiinning to pretend now that nothing's really happened at all.", "character": "eric", "act": 2},
    {"id": 11, "quote": "I didn't feel about her as she felt about me.", "character": "gerald", "act": 2},
    {"id": 12, "quote": "Public men, Mr Birling, have responsibilites as well as privileges.", "character": "inspector", "act": 3},
    {"id": 13, "quote": "The famous younger generation who know it all. And they can't even take a joke.", "character": "arthur", "act": 3},
    {"id": 14, "quote": "I was the only one of you who didn't give in to him.", "character": "sybil", "act": 3},
    {"id": 15, "quote": "The point is, you don't seem to have learnt anything.", "character": "sheila", "act": 3},
    {"id": 16, "quote": "You're not the kind of father a chap could go to when he's in trouble.", "character": "eric", "act": 3},
    {"id": 17, "quote": "Everything's all right now, Sheila. What about this ring?", "character": "gerald", "act": 3}
]

def errorResponse():
    return jsonify({"quote": "Something went wrong. Check your request and try again.", "character": "Something went wrong. Check your request and try again.", "act": "Something went wrong. Check your request and try again."})

def getQuoteNum():
    return random.randint(0, len(quotes) - 1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/docs')
def docs():
    return render_template('docs.html')

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
        if not find_quotes:
            return errorResponse()
        num_quote_select = random.randint(0, len(find_quotes) - 1)
        quote_select = find_quotes[num_quote_select]
        quote = quote_select['quote']
        character = quote_select['character']
        act = quote_select['act']
        return jsonify({"quote": quote, "character": character, "act": act})
    elif filter == 'act':
        act = request.args.get('act')
        find_quotes = [quote for quote in quotes if quote['act'] == int(act)]
        if not find_quotes: 
            return errorResponse()
        num_quote_select = random.randint(0, len(find_quotes) - 1)
        quote_select = find_quotes[num_quote_select]
        quote = quote_select['quote']
        character = quote_select['character']
        act = quote_select['act']
        return jsonify({"quote": quote, "character": character, "act": act})
    else:
        return errorResponse()


if __name__ == '__main__':
    app.run(port=1234)