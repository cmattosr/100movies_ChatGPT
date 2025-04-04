from flask import jsonify, request
import json
import re
from . import api_blueprint

# Load movies from the JSON database when the blueprint is initialized
with open('data/movies.json') as f:
    movies = json.load(f)

@api_blueprint.route('/movies', methods=['GET'])
def get_movies():
    """
    API endpoint to retrieve movies.
    - Accepts a query parameter 'q' to search by movie title or position.
    - Supports wildcards in title search (using '*' as a wildcard).
    """
    q = request.args.get('q')
    if q:
        result = []
        if q.isdigit():
            pos = int(q)
            # Find movies that match the given position
            result = [movie for movie in movies if movie.get('position') == pos]
        else:
            # Convert the query to a regex pattern (wildcard '*' becomes '.*')
            regex = re.compile(q.replace('*', '.*'), re.IGNORECASE)
            result = [movie for movie in movies if regex.search(movie.get('title'))]
        return jsonify(result)
    # If no query is provided, return all movies
    return jsonify(movies)
