from flask import Blueprint

# Create a blueprint for the API endpoints
api_blueprint = Blueprint('api', __name__)

# Import routes so they are registered with the blueprint
from . import routes
