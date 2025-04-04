from flask import render_template, request
import json
import re
from . import app_blueprint

# Load movies from the JSON database when the blueprint is initialized
with open('data/movies.json') as f:
    movies = json.load(f)

@app_blueprint.route('/', methods=['GET'])
def index():
    """
    Renders the home page and processes search queries.
    - If the query is numeric, it searches for a movie by its position.
    - Otherwise, it treats the query as a title search and supports wildcards (use * as a wildcard).
    """
    query = request.args.get('query')
    result = []
    if query:
        if query.isdigit():
            pos = int(query)
            # Find movies that match the given position
            result = [movie for movie in movies if movie.get('position') == pos]
        else:
            # Convert the query to a regex pattern (wildcard '*' becomes '.*')
            regex = re.compile(query.replace('*', '.*'), re.IGNORECASE)
            result = [movie for movie in movies if regex.search(movie.get('title'))]
    return render_template('index.html', movies=movies, result=result)
