from flask import flash, Blueprint, request, redirect, render_template, url_for, jsonify, Markup, send_from_directory, Response, make_response
from flask.views import MethodView
from flask_login import LoginManager, UserMixin, login_required, current_user
from datetime import datetime, timedelta, date
import time
import json
from werkzeug.exceptions import NotFound
import subprocess
import shlex
import os

from . import app
# from . import query_db, db
from .login import login_manager # THIS IS NEEDED


SH_data = Blueprint('SH_data', __name__, template_folder='templates')
ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))

class HomePage(MethodView):
    def get(self):
        return render_template('home.html')


class FoodData(MethodView):
    def get(self):
        if current_user is not None and current_user.is_authenticated:
            flash('HELLO USER', 'success')

        return render_template('food_data.html')


SH_data.add_url_rule('/', view_func=HomePage.as_view('home'))
SH_data.add_url_rule('/data/', view_func=FoodData.as_view('FoodData'))


@app.route('/generate_report/', methods=["POST"])
def generate_report():
    uid = current_user.id


    try:
        # do some stuff
        return jsonify(result='Success')
    except Exception as e:
        print "ERROR!!! {error}: {msg}".format(error=type(e).__name__, msg=str(e))
        flash(Markup("Uh oh! Something went wrong. Please check your inputs again or contact an Admin.<br>"
                     "<b>{error}:</b> {msg}".format(error=type(e).__name__, msg=str(e))), 'danger')
        return jsonify(result='Error')
