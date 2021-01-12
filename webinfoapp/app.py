from flask import Flask
from webinfoapp.views.index import bp as index_bp 
from webinfoapp.views.createnotes import bp as createnotes_bp

app = Flask(__name__)

app.register_blueprint(index_bp)
app.register_blueprint(createnotes_bp)