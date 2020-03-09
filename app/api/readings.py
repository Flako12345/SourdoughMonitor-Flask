from flask import request, jsonify
from . import api
from .authentication import auth
from ..models import Reading, Feeding
from .. import db
from datetime import datetime


@api.route('/readings/', methods = ['POST'])
@auth.login_required
def new_reading():
    reading = Reading.from_json(request.json)
    """
    feeding = Feeding.query.filter_by\
              (Feeding.sourdough_id == reading.sourdough_id).filter_by(Feeding.timestamp <= datetime.now()).\
              order_by(Feeding.timestamp.desc()).first()
              
              """
    feeding = Feeding.query.filter(Feeding.sourdough_id == reading.sourdough_id)\
        .filter(Feeding.timestamp <= datetime.now()).order_by(Feeding.timestamp.desc()).first()

    lastReading = feeding.readings.order_by(Reading.timestamp).first()
    reading.feeding = feeding

    if lastReading == None:
        reading.normalizedReading = 100
    else:
        reading.normalizedReading = (reading.reading / lastReading.reading) * 100

    db.session.add(reading)
    db.session.commit()
    return jsonify(201)



