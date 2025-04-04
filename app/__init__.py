from flask import Flask, Blueprint

# Create a blueprint for the web UI
# app_blueprint = Blueprint('app', __name__)

app_blueprint = Blueprint('web_app', __name__, template_folder='templates')


# Import routes so they are registered with the blueprint
from . import routes
