from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_anime_meme():
    url = "https://meme-api.com/gimme/Animemes"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        meme_url = data.get('url')
        title = data.get('title', 'No title available')

        return title, meme_url
    else:
        return {"Failed to fetch meme. Status Code:", response.status_code}

print(get_anime_meme())

@app.route("/")
def index():
    title, meme_url = get_anime_meme()
    return render_template("index.html", title=title, meme_url=meme_url)

if __name__ == "__main__":
    app.run()