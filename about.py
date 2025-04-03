from flask import Blueprint, render_template,request,jsonify,redirect,url_for

about = Blueprint('aboutus',__name__)

@about.route("/")
def infopage():
    return render_template('about_us.html')