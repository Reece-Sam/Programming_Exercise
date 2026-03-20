from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("NEWS_API_KEY")

@app.route("/")
def home():
    url = f"https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    print(data)

    articles = data.get("articles", [])

    return render_template("index.html", articles=articles)




if __name__ == "__main__":
    app.run(debug=True)