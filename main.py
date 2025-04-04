from flask import Flask
from app import app_blueprint as web_app
from api import api_blueprint as api_app

app = Flask(__name__)

# Register the web UI blueprint
app.register_blueprint(web_app)
# Register the API blueprint under the /api prefix
app.register_blueprint(api_app, url_prefix='/api')

if __name__ == '__main__':
    # Run the application on the local system on port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
