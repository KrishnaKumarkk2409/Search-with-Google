import os
import google.auth
from google.auth.transport.requests import Request
from google.auth import impersonated_credentials
from googleapiclient.discovery import build
from flask import Flask, render_template_string

# Replace with your own values
SERVICE_ACCOUNT_FILE = 'credentials.json'  # Path to your service account key
CSE_ID = 'e7c4b9c38fac14b32'  # Your Custom Search Engine ID
API_KEY = 'AIzaSyDoX4znJCDvmS7hxkJpll7wL5IPYLXqhiU'  # Your Custom Search API Key

app = Flask(__name__)

# Authenticate using the service account key
def authenticate_with_service_account(service_account_file):
    credentials, project = google.auth.load_credentials_from_file(service_account_file)
    credentials = credentials.with_subject('your_service_account_email')  # Optional if needed
    return credentials

# Function to perform a custom search using the API
def custom_search(query):
    # Authenticate
    credentials = authenticate_with_service_account(SERVICE_ACCOUNT_FILE)
    
    # Build the Custom Search API service
    service = build("customsearch", "v1", developerKey=API_KEY)

    # Execute the search query
    res = service.cse().list(q=query, cx=CSE_ID).execute()
    
    if 'items' in res:
        return res['items']  # List of search results
    else:
        return []

# HTML Template with CSE Search Box
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Google Custom Search</title>
</head>
<body>
    <h1>Search the Web using Google Custom Search Engine</h1>
    <!-- Custom Search Engine Embed -->
    <script async src="https://cse.google.com/cse.js?cx={{ cse_id }}"></script>
    <div class="gcse-search"></div>

    <h2>Search Results from Python API (if needed):</h2>
    <ul>
        {% for result in results %}
            <li><a href="{{ result.link }}">{{ result.title }}</a><br>{{ result.snippet }}</li>
        {% endfor %}
    </ul>
</body>
</html>
'''

# Flask route for the search page
@app.route('/')
def search_page():
    query = 'Python programming'  # Example search query for the API-based search
    results = custom_search(query)  # Fetch results using the API

    return render_template_string(HTML_TEMPLATE, cse_id=CSE_ID, results=results)

if __name__ == "__main__":
    app.run(debug=True)
