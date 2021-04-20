from bson import ObjectId
from flask import Flask, request, jsonify
from pymongo import MongoClient
import datetime
import json

app = Flask(__name__)

client = MongoClient("mongodb+srv://user:asdzx@scrapycluster.3ojmw.mongodb.net/test")
db = client["Scrapy"]
collection = db["Scrap"]


def check_request(parametry, method):
    if method == "get_many":
        if not parametry:
            return 300
        else:
            parametry = "\"" + str(parametry) + "\""
            try:
                json.loads(parametry)
                if "x" in parametry and "y" in parametry:
                    return 300
                elif "x" in parametry or "y" in parametry:
                    return 200
                else:
                    return 300
            except:
                return 300


def answer(status):
    answer = {
        "Error": status,
        "Message": "missing or too much arguments, plesae fill request with x or y variables in JSON format, "
                   "x stands for city, y page name, you can only fill one, "
                   "available cities: Gdańsk, Sopot, Gdynia, Hel, Jastarnia, Kuźnica, Jurata, Chałupy, Puck,"
                   "Krynica Morska, Wicko, "
                   "available pages: http://sopotsurf.com,  onewave.pl, aloha.pl, bssurf.pl, okonska.pl, "
                   "kitecrew.pl, polsporty.pl, easy-surfcenter.pl, "
                   "szkola.abcsurf.pl, e-surfing.pl "
                   "example:"
                   "{'y': 'Wicko'},"
    }
    return answer


@app.route('/Scrapy_get_all', methods=['GET'])
def get_all():
    # no parameters, print all
    wynik = {}
    wynik2 = {}
    result = collection.find({})

    for i, x in enumerate(result):
        for z in x:
            if z != "_id":
                wynik.update({z: x[z]})
        wynik2.update({str(i): wynik})
    return wynik2


@app.route('/Scrapy_get_many', methods=['GET'])
def get_many():
    # takes only one argument, "x" or "y", read "answer" method

    parametry = request.get_json()

    status = check_request(parametry, "get_one")

    if status == 300:
        return answer(status)
    else:
        if "x" in parametry:
            wynik = {}
            wynik2 = {}
            x = parametry["x"]
            result = collection.find({"Miejscowość": x})
            for i, x in enumerate(result):
                for z in x:
                    if z != "_id":
                        wynik.update({z: x[z]})
                wynik2.update({str(i): wynik})
            return wynik2
        else:
            wynik = {}
            wynik2 = {}
            y = parametry["y"]
            result = collection.find({"Oferta strony": y})
            for i, x in enumerate(result):
                for z in x:
                    if z != "_id":
                        wynik.update({z: x[z]})
                wynik2.update({str(i): wynik})
            return wynik2


@app.route('/Scrapy_get_one', methods=['GET'])
def get_one():
    # It takes one argument, ID as "x"

    dane = str(request.get_json())
    dane = "\"" + dane + "\""

    try:
        json.loads(dane)
        dane = request.get_json()
        wynik = {}
        objid = dane["x"]
        result = collection.find({"_id": ObjectId(objid)})
        for res in result:
            for r in res:
                if r != "_id":
                    wynik.update({r: res[r]})

        return wynik

    except:
        return "Status code: 301"


@app.route('/Scrapy_write_one', methods=['POST'])
def post():
    """Data inserted to database by method "Post" must be in JSON format,
    otherwise there would be "null" added to database"""

    data = str(datetime.datetime.now())[0:19]
    str2 = ("data added manually throught API " + data)
    dane = str(request.get_json())
    dane = "\"" + dane + "\""

    try:
        json.loads(dane)
        dane = request.get_json()
        dane3 = {
            str2: dane}
        collection.insert_one(dane3)
        return "data inserted to database"
    except:
        return "Status code 301"


@app.route('/Scrapy_update_one', methods=['PUT'])
def put():
    # takes 2 parameters,
    # x = object id, y  = new data {"x" : "600d9b9865c7643436dfa294", "y": {"field_to_update or add":"asd"}}

    dane = str(request.get_json())
    dane = "\"" + dane + "\""

    try:
        json.loads(dane)
        dane = request.get_json()
        objid = dane["x"]
        newdata = dane["y"]
        wynik1 = {}
        wynik2 = {}
        stat = {"_id": ObjectId(objid)}
        pri = collection.find({"_id": ObjectId(objid)})

        for pr in pri:
            for p in pr:
                if p != "_id":
                    wynik1.update({p: pr[p]})

        collection.update_one(stat, {"$set": newdata})
        pas = collection.find({"_id": ObjectId(objid)})

        for pa in pas:
            for p2 in pa:
                if p2 != "_id":
                    wynik2.update({p2: pa[p2]})

        ret = {"data after update:": wynik2,
               "data before update:": wynik1}

        return ret

    except:
        return "Status code: 301"


@app.route('/Scrapy_delete_one', methods=['DELETE'])
def delete():
    # delete after ID, takes only "x" argument in json format
    dane = str(request.get_json())
    dane = "\"" + dane + "\""

    try:
        json.loads(dane)
        dane = request.get_json()
        objid = dane["x"]
        collection.delete_one({"_id": ObjectId(objid)})
        ret = "Object " + objid + " deleted successfully"
        return ret
    except:
        return "Status code: 301"


if __name__ == "__main__":
    app.run(debug=True)
