Here's a `README.md` file for your project based on the files you've provided:

---

# EncapAi - Google Custom Search Integration

This repository contains a Python-based Flask web application that integrates with Google Custom Search API and enables searching the web using Google's Custom Search Engine (CSE). The project uses service account authentication to securely access Google's APIs and retrieve relevant search results. The application is also designed to enrich search results with additional content fetched from the links returned by the API.

## Project Structure

- **app.py**: Contains the Flask application and the logic for interacting with the Google Custom Search API, including authentication and rendering the results.
- **main.py**: Another Flask-based API that provides a search endpoint. It retrieves search results using the Custom Search API and enriches those results with content fetched from the links.
- **credentials.json**: Google service account credentials used for API authentication.
- **requirements.txt**: Contains the required Python packages to run the project.

## Features

- **Google Custom Search**: Uses Google Custom Search Engine (CSE) to search the web for a given query.
- **Content Enrichment**: Fetches and displays the content of search result links to enrich the user experience.
- **Flask Web Application**: Provides a web interface for users to search using the custom search engine and view results.
- **Service Account Authentication**: Utilizes a service account to authenticate and authorize access to Google APIs securely.

## Installation

### Step 1: Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/your-username/EncapAi.git
cd EncapAi
```

### Step 2: Install Dependencies

Install the required dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Step 3: Configure Google API Credentials

1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project and enable the **Custom Search API**.
3. Create a service account, and download the JSON credentials file.
4. Place the credentials file in the project directory and rename it to `credentials.json`.

### Step 4: Set Up the Google Custom Search Engine (CSE)

1. Go to [Google Custom Search Engine](https://cse.google.com/cse/) and create a new CSE.
2. Obtain your **CSE ID** and **API Key**.
3. Update the values of `CSE_ID` and `API_KEY` in `app.py` and `main.py` with the values from your CSE.

### Step 5: Run the Flask Application

Start the Flask development server:

```bash
python app.py
```

For `main.py`, you can also run it similarly:

```bash
python main.py
```

Once the server is running, you can access the search page by navigating to `http://127.0.0.1:5000/` in your browser.

### Step 6: Testing the Search API

You can test the search functionality by visiting the endpoint `/search?query=your-query` (for example: `/search?query=Python programming`).

## How It Works

### **app.py**:
- **Authenticate with Google Service Account**: The app authenticates using the service account credentials (`credentials.json`).
- **Custom Search API**: Executes a search query using Google's Custom Search API and returns the results.
- **Flask Web Interface**: Renders a search interface on the web using an embedded Google CSE search box, and shows results from the API below the search bar.

### **main.py**:
- **Custom Search API**: Similar to `app.py`, it makes a request to Google Custom Search API.
- **Enriching Results**: For each result, it fetches additional content from the URL of the search result using the `BeautifulSoup` library.
- **Flask API Endpoint**: Provides a `/search` endpoint where users can send a query and receive enriched search results.

## Example Search Results

When you search for a term (e.g., "Python programming"), the application fetches results and displays:
- Title of the search result
- Link to the result
- Snippet from the result
- Enriched content fetched from the link (if available)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Let me know if you'd like to adjust any details or add more specific sections!
