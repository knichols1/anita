from flask import jsonify, request, g, abort, url_for, current_app, session, flash
from flask.ext.login import LoginManager, current_user
from . import api

from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker
from app.database import Base
import psycopg2
import psycopg2.extensions
import select



@api.route('/connect/<ip>/<db>')
def connect(ip,db):
    try:
        engine = create_engine('postgresql://gui:AniTa08@' + ip.replace('_','.') +'/' + db, convert_unicode=True)
    
        conn=engine.connect()
        # db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))
        db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=conn))
        query_ip_db= 'query_' + ip  + '_' + db
        #  query_ip_db is a string and should be Base's attribute. setattr() is perfect for this job
        setattr(Base,query_ip_db, db_session.query_property())
        flash("Database connect Successful", 'success') # flash message not working, why?
        return 'success'
    except:
        return 'fail'
