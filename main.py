import random
import json

def main():
    json_file = open('quotes.json', 'r')
    all_quotes = json.load(json_file)
    random_quote = random.choice(all_quotes)
    print("QUOTE FOR TODAY:")
    print(random_quote["quote"]+"\n"+random_quote["author"])
    json_file.close()

if __name__ == '__main__':
    main()