import random
import json
import os
from flask import Flask, jsonify, render_template


def load_json_quote():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, 'database', 'quotes.json')
    all_quotes = []

    try:
        with open(db_path, 'r', encoding="utf-8") as f:
            all_quotes = json.load(f)
            f.close()
    except FileNotFoundError:
        print(f"Error: Could not find file at {db_path}")
        all_quotes = [{"author": "System", "quote": "Could not load quotes. Check path."}]

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