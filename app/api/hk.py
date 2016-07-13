from flask import jsonify, request, g, abort, url_for, current_app, session
from flask.ext.login import LoginManager, current_user
from . import api
from .. import cache
from app.models import Hk

# Primary key list: get the hk now list

@api.route('/<ip_db>/hk/nbufs/<start_time>')
def get_hk_nbufs(ip_db, start_time):
    try:
        hks =getattr(Hk,ip_db).with_entities(Hk.nbuf, Hk.now, Hk.time).filter(Hk.time>start_time).order_by(Hk.now).limit(200).all()
        return jsonify({'hk_nbufs': [item.nbuf for item in hks], 'hk_nows': [item.now for item in hks], 'hk_times': [item.time for item in hks]})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})
# get the length of hk now list


@api.route('/<ip_db>/hk/count')
def get_hk_count(ip_db):
    try:
        count =getattr(Hk,ip_db).count()
        # could not return long type, so use str()
        return str(count)
        # return jsonify({'hk': [item.now&mask for item in hks]})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})
# get a tuple of Hk table


@api.route('/<ip_db>/hk/<nbuf>')
@cache.cached(timeout=3600)
def get_hk(ip_db, nbuf):
    try:
        hk =getattr(Hk,ip_db).filter_by(nbuf=nbuf).first()
        return jsonify({'hk': hk.to_json()})
    except BaseException as error:
        print('Invalid request: {}', format(error))
        return jsonify({})