from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from model.Athletics import Athletics
import os
import json
import copy

with open('secret.json') as f:
    SECRET = json.load(f)

DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"])

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

class VirtualAthletics(Athletics, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    athletics_name = db.Column(db.String(32), unique=False)
    stage_duration = db.Column(db.Integer, unique=False)
    number_of_participants = db.Column(db.Integer, unique=False)
    distance_in_meters = db.Column(db.Integer, unique=False)
    creator = db.Column(db.String(32), unique=False)
    memory_require = db.Column(db.Float, unique=False)

    def __init__(self, athletics_name=None, stage_duration=None, number_of_participants=None, distance_in_meters=None,
                 creator=None, memory_require=None):
        super().__init__(athletics_name, stage_duration, number_of_participants, distance_in_meters)
        # new field
        self.creator = creator
        # new field
        self.memory_require = memory_require


class VirtualAthleticsSchema(ma.Schema):
    class Meta:
        fields = ('athletics_name', 'stage_duration', 'number_of_participants', 'distance_in_meters', 'creator', 'memory_require')

virtual_athletic_schema = VirtualAthleticsSchema()
virtual_athletics_schema = VirtualAthleticsSchema(many=True)

@app.route("/virtual_athletics", methods=["POST"])
def add_virtual_athletic():
    virtual_athletic = VirtualAthletics(request.json['athletics_name'],
                                        request.json['stage_duration'],
                                        request.json['number_of_participants'],
                                        request.json['distance_in_meters'],
                                        request.json['creator'],
                                        request.json['memory_require'])
    db.session.add(virtual_athletic)
    db.session.commit()
    return virtual_athletic_schema.jsonify(virtual_athletic)

@app.route("/virtual_athletics", methods=["GET"])
def get_virtual_athletic():
    all_virtual_athletics = VirtualAthletics.query.all()
    result = virtual_athletics_schema.dump(all_virtual_athletics)
    return jsonify({'virtual_athletics': result})

@app.route("/virtual_athletics/<id>", methods=["GET"])
def virtual_athletics_detail(id):
    virtual_athletics = VirtualAthletics.query.get(id)
    if not virtual_athletics:
        abort(404)
    return virtual_athletic_schema.jsonify(virtual_athletics)

@app.route("/virtual_athletics/<id>", methods=["PUT"])
def virtual_athletics_update(id):
    virtual_athletics = VirtualAthletics.query.get(id)
    if not virtual_athletics:
        abort(404)
    virtual_athletics.athletics_name = request.json['athletics_name']
    virtual_athletics.stage_duration = request.json['stage_duration']
    virtual_athletics.number_of_participants = request.json['number_of_participants']
    virtual_athletics.distance_in_meters = request.json['distance_in_meters']
    virtual_athletics.creator = request.json['creator']
    virtual_athletics.memory_require = request.json['memory_require']
    db.session.commit()
    return virtual_athletic_schema.jsonify(virtual_athletics)

@app.route("/virtual_athletics/<id>", methods=["DELETE"])
def virtual_athletics_delete(id):
    virtual_athletics = VirtualAthletics.query.get(id)
    if not virtual_athletics:
        abort(404)
    db.session.delete(virtual_athletics)
    db.session.commit()
    return virtual_athletic_schema.jsonify(virtual_athletics)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0')