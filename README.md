# Api
API created in Flask, applies the CRUD method, created to work with data downloaded using a scraper to the online MongoDB Database. To use it, please fill in the code following sections with your MongoDB Atlas database credentials:

client = MongoClient("your MongoDB connection string")

DB = client["your database name"]

collection = db["your collection name"]

All of the fields above require quotation marks.

Packages used in code: from bson - ObjectId, Flask, request, jsonify, from pymongo MongoClient, DateTime, JSON

Routes available:

/Scrapy_get_all

/Scrapy_get_many

/Scrapy_get_one

/Scrapy_write_one

/Scrapy_update_one

/Scrapy_delete_one

-Route /Scrapy_get_all uses the "Get" method, allowing to get all data in the specified collection. A request does not need any data.

-Route /Scrapy_get_many uses the "Get" method, which allows getting a couple of documents, filtered by city or page. A request needs to include parameters in JSON format and can include only one out of two parameters, x is standing for the city and y for the page name, examples below:

{ "x": "Sopot" }

another request:

{ "y": "onewave.pl" }

List of available cities: Gdańsk, Sopot, Gdynia, Hel, Jastarnia, Kuźnica, Jurata, Chałupy, Puck, Krynica Morska, Wicko List of available pages: sopotsurf.com, onewave.pl, aloha.pl, bssurf.pl, okonska.pl, kitecrew.pl, polsporty.pl, easy-surfcenter.pl, szkola.abcsurf.pl, e-surfing.pl

-Route /Scrapy_get_one uses the "Get" method and allows to get one document by its id, request must be in JSON format, must have the "x" parameter standing for ID, and look like the following example:

{ "x": "600d9b9865c7643436dfa294" }

-Route /Scrapy_write_one uses the "Post" method and allows the creation of, one extra document in collection, data in the request must be in JSON format.

-Route /Scrapy_update_one uses the "Put" method and allows to update or add a field or multiple fields in the existing document, request must include "x" and "y" parameters and be in the following JSON format:

{ "x": "600d9b9865c7643436dfa294", "y": { "name of field_to_update or add": "new data" } } in this example, x stands for object ID.

-Route /Scrapy_delete_one uses the "Delete" method and allows to deletion of the specified document by its ID, request must be in JSON format and must include the "x" parameter standing for object ID. Example:

{ "x": "600d9b9865c7643436dfa294" }

Status codes: 200 - request executed successfully 300 - not enough or too many arguments, please check input 301 - data in the wrong format, please check if the input is in JSON format or if an ID is correct 400 - bad request, make sure data in the request are correct 405 - Method Not Allowed, choose correct request method 501 - internal server error, check if flask server is running and parameters in the request are correct, request data must be in JSON format

If API returns an empty string, it means searched document has not been found, make a sure document with specified ID or parameters exists, and small and capital letters matter

