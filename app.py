from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
from request import call
from trim import trim

app = Flask(__name__)
attr = ["name", "value", "change"]

@app.route("/")
def index():
    response = call()
    soup = BeautifulSoup(response, "html5lib")
    divs = soup.find_all("div", class_="market-data")

    currencies = list()
    items = divs[0].find_all("div", class_="item")

    for item in items:
        spans = item.find_all("span")
        dict = {}
        count = 0
        for attributes in spans:
            attribute_text = attributes.get_text()
            dict[attr[count]] = attribute_text if count != 2 else trim(attribute_text)
            count = count + 1
        currencies.append(dict)
    return jsonify(currencies)
