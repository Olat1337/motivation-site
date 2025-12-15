import random
import json
from flask import Flask, jsonify, render_template


def load_json_quote():
    json_file = open('quotes.json', 'r', encoding="utf-8")
    all_quotes = json.load(json_file)
    json_file.close()

    return all_quotes

def get_random_quote(all_quotes):
    random_quote = random.choice(all_quotes)
    return random_quote

def flask_app(all_quotes):
    app = Flask(__name__)

    @app.route('/api/ret_quote', methods=['GET'])
    def ret_quote():
        random_quote = get_random_quote(all_quotes)
        return jsonify(author=random_quote["author"], quote=random_quote["quote"])

    @app.route("/")
    def home():
        random_quote = get_random_quote(all_quotes)
        return render_template("home.html", quote = random_quote)

    app.run(debug=True)

def main():
    all_quotes = load_json_quote()
    flask_app(all_quotes)

if __name__ == '__main__':
    main()