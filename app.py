from flask import Flask, render_template, send_from_directory, abort, request, redirect, url_for, Response, jsonify
from flask_marshmallow import Marshmallow
from flask_cors import CORS, cross_origin

import json
import time
import sqlite3
app = Flask(__name__, static_url_path='')
cors = CORS(app)


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from database_setup import Base, EffectsProfile

# Connect to Database and create database session
engine = create_engine('sqlite:///profile-collection.db',connect_args={'check_same_thread': False})
Base.metadata.bind = engine

DBSession = scoped_session(sessionmaker(bind=engine))

#TODO: Ensure marshmallow is thread safe
# add input data validation
# ensure sqlalchemy setup/init is proper
# Provide better error return codes/info
# possibly remove use of id in uri
# Find better way of performing data base operations rather than explicitly locking


ma = Marshmallow(app)

'''    verblib_set_wet ( verb, verblib_initialwet );
    verblib_set_room_size ( verb, verblib_initialroom );
    verblib_set_dry ( verb, verblib_initialdry );
    verblib_set_damping ( verb, verblib_initialdamp );
    verblib_set_width ( verb, verblib_initialwidth );
    verblib_set_mode ( verb, verblib_initialmode );'''


class EffectsProfileSchema(ma.Schema):
    class Meta:
        fields = ('title','author','tremoloFreq', 'tremoloDepth', 'tremoloEnabled', 
                 'tremoloOrderNumber', 'overDriveThresh', 'overDriveEnabled', 'overDriveOrderNumber', 
                 'distortThresh', 'distortEnabled', 'distortOrderNumber', 'reverbWetLevel', 'reverbRoomSize', 
                 'reverbDryLevel', 'reverbDampLevel', 'reverbWidth','reverbEnabled', 'reverbMode',
                 'reverbOrderNumber', 'isSelected')

effects_profile_schema = EffectsProfileSchema()
effects_profiles_schema = EffectsProfileSchema(many=True)

@app.before_request
def only_json():
    if not request.is_json and (request.method == 'POST' or request.method == 'DELETE'): 
        print(request.content_type)
        abort(400)  # or any custom BadRequest message

@app.route('/staticContent/<path:path>')
def send_js(path):
    return send_from_directory('staticContent', path)

# landing page that will display all the profiles in our database
@app.route('/effectsProfiles', methods=['GET'])
def showEffectProfiles():
    session = DBSession()
    session.execute("begin exclusive transaction")
    effectProfiles = session.query(EffectsProfile).all()
    result = effects_profiles_schema.dump(effectProfiles)
    session.execute("commit")
    session.close()
    return jsonify(result)




# This will let us add/change/delete profiles
@app.route('/effectsProfile/', methods=['GET', 'POST', 'DELETE'])
def changeProfile():
    session = DBSession()
    session.execute("begin exclusive transaction")
    
    if request.method == 'POST':
        jsonData = request.get_json()
        
        requestedProfile = session.query(EffectsProfile).filter_by(title=jsonData['title']).one_or_none()
        if requestedProfile == None:
            newProfile = EffectsProfile(**jsonData)
            session.add(newProfile)
            session.commit()
            session.close()
            status_code = Response(status=200)
            return status_code
        dictData = request.get_json()
        dictData["isSelected"] = requestedProfile.isSelected
        for key, value in dictData.items():
            setattr(requestedProfile, key, value)
        session.commit()
        session.close()
        status_code = Response(status=200)
        return status_code
    elif request.method == 'GET':
        jsonData = request.get_json()
        
        requestedProfile = session.query(EffectsProfile).filter_by(title=jsonData['title']).one_or_none()
        if requestedProfile == None:
            session.commit()
            session.close()
            status_code = Response(status=404)
            return status_code
        result = effects_profile_schema.dump(requestedProfile)
        session.commit()
        session.close()
        return jsonify(result)
    elif request.method == 'DELETE':
        jsonData = request.get_json()
        
        requestedProfile = session.query(EffectsProfile).filter_by(title=jsonData['title']).one_or_none()
        if requestedProfile == None:
            session.commit()
            session.close()
            status_code = Response(status=404)
            return status_code
        session.delete(requestedProfile)
        session.commit()
        #session.execute("commit")
        session.close()
        status_code = Response(status=200)
        return status_code

@app.route('/effectsProfile/selectedProfile/', methods=['GET', 'POST'])
def selectedProfile():
    session = DBSession()
    session.execute("begin exclusive transaction")
    if request.method == 'POST':
        jsonData = request.get_json()
        requestedProfile = session.query(EffectsProfile).filter_by(title=jsonData['title']).one_or_none()
        if requestedProfile == None:
            session.commit()
            session.close()
            status_code = Response(status=404)
            return status_code
        else:
            currentSelected = session.query(EffectsProfile).filter_by(isSelected=True).one_or_none()
            if currentSelected != None:
                setattr(currentSelected, 'isSelected', False)
            setattr(requestedProfile, 'isSelected', True)
            session.commit()
            session.close()
            status_code = Response(status=200)
            return status_code
    elif request.method == 'GET':
        jsonData = request.get_json()
        currentSelected = session.query(EffectsProfile).filter_by(isSelected=True).one_or_none()
        if currentSelected == None:
            session.commit()
            session.close()
            status_code = Response(status=404)
            return status_code
        else:
            result = effects_profile_schema.dump(currentSelected)
            session.commit()
            session.close()
            return jsonify(result)
if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=4996)#host='0.0.0.0' (for local network) host='localhost' (for this computer only)
