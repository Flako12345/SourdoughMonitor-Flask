from flask import request, jsonify
from . import api
from ..models import Reading
from .. import db


@api.route('/readings/', methods = ['POST'])
def new_reading():
    reading = Reading.from_json(request.json)
    db.session.add(reading)
    db.session.commit()
    return jsonify(201)



