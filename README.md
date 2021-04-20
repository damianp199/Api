# Api
API created in Flask applies CRUD method, created to work with data downloaded using scraper to online MongoDB Database. To use it, please fill in code following sections with your MongoDB Atlas database credentials:

client = MongoClient("your MongoDB connection string")

db = client["your database name"]

collection = db["your collection name"]

All of the fields above require quotation marks.

Packages used in code: from bson - ObjectId, Flask, request, jsonify, from pymongo MongoClient, datetime, json

Routes available:

/Scrapy_get_all

/Scrapy_get_many

/Scrapy_get_one

/Scrapy_write_one

/Scrapy_update_one

/Scrapy_delete_one

-Route /Scrapy_get_all uses "Get" method, allows to get all data in specified collection. Request does not need any data.

-Route /Scrapy_get_many uses "Get" method, allows to get couple of documents, filtered by city or page. Request needs to include parameters in JSON format and can include only one out of two parameters, x standing for the city and y for the page name, examples below:

{ "x": "Sopot" }

another request:

{ "y": "onewave.pl" }

List of available cities: Gdańsk, Sopot, Gdynia, Hel, Jastarnia, Kuźnica, Jurata, Chałupy, Puck, Krynica Morska, Wicko List of available pages: sopotsurf.com, onewave.pl, aloha.pl, bssurf.pl, okonska.pl, kitecrew.pl, polsporty.pl, easy-surfcenter.pl, szkola.abcsurf.pl, e-surfing.pl

-Route /Scrapy_get_one uses "Get" method and allows to get one document by its id, request must be in JSON format, must have "x" parameter standing for ID, and look like following example:

{ "x": "600d9b9865c7643436dfa294" }

-Route /Scrapy_write_one uses "Post" method and allows to create one extra document in collection, data in request must be in JSON format.

-Route /Scrapy_update_one uses "Put" method and allows to update or add field or multiple fields in existing document, request must include "x" and "y" parameters and be in following JSON format:

{ "x": "600d9b9865c7643436dfa294", "y": { "name of field_to_update or add": "new data" } } in this example, x stands for object ID.

-Route /Scrapy_delete_one uses "Delete" method and allows to delete specified document by its ID, request must be in JSON format and must include "x" parameter standing for object ID. Example:

{ "x": "600d9b9865c7643436dfa294" }

Status codes: 200 - request executed successfully 300 - not enought or too much arguments, please check input 301 - data in wrong format, please check if input is in JSON format or if ID is correct 400 - bad request, make sure data in request are correct 405 - Method Not Allowed, choose correct request method 501 - internal server error, check if flask server is running and parameters in request are correct, request data must be in JSON format

If API returns an empty string, it means searched document have not been found, make sure document with specified ID or parameters exist, small and capital letters matter

