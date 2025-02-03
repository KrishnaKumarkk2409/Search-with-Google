from flask import Flask, request, jsonify
import os
import json
import requests
import google.auth
from google.auth.transport.requests import Request
from google.auth import impersonated_credentials
from googleapiclient.discovery import build
from bs4 import BeautifulSoup

app = Flask(__name__)

SERVICE_ACCOUNT_FILE = 'credentials.json'
CSE_ID = 'e7c4b9c38fac14b32'
API_KEY = 'AIzaSyDoX4znJCDvmS7hxkJpll7wL5IPYLXqhiU'
LOG_FILE = 'search_results.json'

def authenticate_with_service_account(service_account_file):
    credentials, project = google.auth.load_credentials_from_file(service_account_file)
    credentials = credentials.with_subject('your_service_account_email')
    return credentials

def fetch_content(link):
    try:
        response = requests.get(link, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            text_parts = soup.stripped_strings
            formatted_text = "\n".join(text_parts)
            return formatted_text
        else:
            return "Unable to fetch content (status code: {})".format(response.status_code)
    except Exception as e:
        return f"Error fetching content: {str(e)}"

def custom_search(query):
    service = build("customsearch", "v1", developerKey=API_KEY)
    results = []
    for start in [1, 11]:
        res = service.cse().list(q=query, cx=CSE_ID, start=start).execute()
        if 'items' in res:
            results.extend(res['items'])
        else:
            break
    return results

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    if not query:
        return jsonify({'error': 'No search query provided.'}), 400

    results = custom_search(query)
    if results:
        enriched_results = []
        for idx, item in enumerate(results, 1):
            title = item.get('title', 'No title')
            link = item.get('link', 'No link')
            snippet = item.get('snippet', 'No snippet')
            content = fetch_content(link)

            enriched_result = {
                'index': idx,
                'title': title,
                'link': link,
                'content': content,
                'snippet': snippet
            }
            enriched_results.append(enriched_result)

        return jsonify(enriched_results)
    else:
        return jsonify({'message': 'No results found!'})

if __name__ == '__main__':
    app.run(debug=True)

