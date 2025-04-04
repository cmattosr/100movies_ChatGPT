# IMDb Top Movies Application

This application displays the top 100 movies (from IMDb) and allows you to search by movie position or title (wildcards supported). It features a web-based UI using Flask and also provides an API endpoint for HTTP requests.

## Folder Structure

imdb-top-movies/ ├── app/ # Web UI code │ ├── init.py │ ├── routes.py │ └── templates/ │ └── index.html ├── api/ # API code │ ├── init.py │ └── routes.py ├── data/ │ └── movies.json # JSON file with movie data (update with top 100 movies) ├── k8s/ │ └── deployment.yaml # Kubernetes deployment file ├── main.py # Main Flask application file ├── requirements.txt # Python dependencies ├── Dockerfile # Docker configuration └── README.md # This documentation file


## Running Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-repo/imdb-top-movies.git
   cd imdb-top-movies

### Create a virtual environment (optional but recommended):
python3 -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate

### Install dependencies:
pip install -r requirements.txt

### Run the application:
python main.py
* The application will be available at http://localhost:5000.

## API Usage

### To retrieve all movies:
curl http://localhost:5000/api/movies

### To search for a movie by position (e.g., position 3) or title (wildcards allowed):
curl "http://localhost:5000/api/movies?q=3"
curl "http://localhost:5000/api/movies?q=God*"

## Dockerization

### Build the Docker image:
docker build -t your-dockerhub-username/imdb-top-movies:latest .

### Run the Docker container:
docker run -p 5000:5000 your-dockerhub-username/imdb-top-movies:latest

