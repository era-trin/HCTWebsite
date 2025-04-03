from flask import Blueprint, render_template,request,jsonify,redirect,url_for

views = Blueprint(__name__,'views')

@views.route("/")
def home():
    return render_template('index.html', name="Ellan")

@views.route("/profile")
def profile():
    args = request.args
    name = args.get('name')
    return render_template("index.html", name = name) #wip

@views.route("/json")
def get_json():
    return jsonify({'name': 'Tim', 'coolness': 10}) #wip

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data) 

@views.route("/go_to_home")
def go_to_home():
    return redirect(url_for("views.home")) #wip - move to contact



