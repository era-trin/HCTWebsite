from flask import Flask
from views import views
from contact import contactform
from about import about
#initiallizes the webpage + imports visuals

app = Flask(__name__)
app.config["SECRET_KEY"] = '1220'
app.register_blueprint(views,url_prefix="/home")
app.register_blueprint(contactform,url_prefix = "/form")
app.register_blueprint(about,url_prefix="/about")





if __name__ == '__main__': # runs on port 8000
    app.run(debug=True, port = 8000)