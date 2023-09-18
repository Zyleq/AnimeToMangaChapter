from flask import Flask, jsonify
from flask_cors import CORS
from flask_caching import Cache
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.config['CACHE_TYPE'] = 'SimpleCache'  # Using simple in-memory caching for demonstration
cache = Cache(app)
CORS(app)

@cache.memoize(timeout=3600)
def fetch_data(anime_name):
    anime_name = anime_name.replace(" ","-")
    url = f"https://listfist.com/list-of-{anime_name}-episode-to-chapter-conversion"
    response = requests.get(url)
    results = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract elements from each class
        col1_elements = [e.text.strip() for e in soup.select('td.col-1.odd')]
        col2_elements = [e.text.strip() for e in soup.select('td.col-2.even')]
        col3_elements = [e.text.strip() for e in soup.select('td.col-3.odd')]

        # Combine them into pairs
        pairs = list(zip(col1_elements, col2_elements, col3_elements))

        # Add each pair to results
        for pair in pairs:
            results.append(pair)

        return results
    else:
        return None

@app.route("/fetch-data/<anime_name>")
def get_data(anime_name):
    data = fetch_data(anime_name)

    if data:
        return jsonify(data)
    else:
        return jsonify({"error": "Failed to retrieve data"}), 500

if __name__ == "__main__":
    app.run(debug=True)
