from datetime import datetime
from operator import itemgetter

from flask import Flask, jsonify, request, render_template
from pymongo.mongo_client import MongoClient
import os
from dotenv import load_dotenv



load_dotenv()
uri =os.getenv('uri')

client = MongoClient(uri)
db=client.practice
collections=db['flask-practice']


app = Flask(__name__)


@app.route('/signup', methods=["POST"])
def signup():
    # name=request.json['user']
    # return render_template('signup.html',name=name)
    form_data= request.get_json()
    result = collections.insert_one(form_data)
    form_data["_id"] = str(result.inserted_id)
    return jsonify(form_data)

@app.route('/view')                 #print data documents in db
def view():
    data =list(collections.find())
    print(data)
    for doc in data:
        doc["_id"] =str(doc["_id"])


    # for _id  in data :
    #     #del id["_id"]
    #     print(_id)
    return jsonify(data)

if __name__ == '__main__' :
    app.run(debug = True , port=8000,host='127.0.0.1')
