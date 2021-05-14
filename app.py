from flask import Flask
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import  ObjectId
from flask import jsonify,request

app = Flask(__name__)
app.secret_key='key'
app.config['MONGO_URI']="mongodb://localhost:27017/audioserver"
mongo = PyMongo(app)


@app.errorhandler(404)
def not_found(error=None):
    message={
        'status':404,
        'message':'Not Found'+request.url
    }
    resp=jsonify(message)
    resp.status_code = 404
    return resp

#CRUD for Songs Collection
#CREATE

@app.route('/add',methods=['POST'])
def add_song():
    _json=request.json
    _name=_json['name']
    _duration=_json['duration']
    _uplodeddate=_json['uplodeddate']

    if _name and _duration and _uplodeddate and request.method=='POST':
        id=mongo.db.songs.insert({'name':_name,'duration':_duration,'uplodeddate':_uplodeddate})

        resp = jsonify("Song added successfully !")
        resp.status_code = 200
        return resp
    else:
        return not_found()

#DISPLAY

@app.route('/songs')
def Display_songs():
    songs = mongo.db.songs.find()
    resp=dumps(songs)
    return resp
#READ

@app.route('/song/<id>')
def find_song(id):
    song=mongo.db.songs.find_one({'_id':ObjectId(id)})
    resp =dumps(song)
    return resp

#DELETE

@app.route('/delete/<id>',methods=['DELETE'])
def delete_song(id):
    mongo.db.songs.delete_one({'_id':ObjectId(id)})
    resp = jsonify("Song deleted successfully")

    resp.status_code=200
    return resp

#UPDATE

@app.route('/update/<id>',methods=['PUT'])
def update_song(id):
    _id=id
    _json=request.json
    _name=_json['name']
    _duration=_json['duration']
    _uplodeddate=_json['uplodeddate']

    if _name and _duration and _uplodeddate and request.method=='PUT':
        mongo.db.songs.update_one({'_id':ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)},{'$set':{'name':_name,'duration':_duration,'uplodeddate':_uplodeddate}})
        resp = jsonify("song updated successfully !")
        resp.status_code=200
        return resp
    else:
        return not_found()





if __name__=='__main__':
    app.run(debug=True)