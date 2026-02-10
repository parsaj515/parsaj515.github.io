from flask import Flask, render_template, request
import requests
from urllib.parse import quote

app = Flask(__name__)

# === CONFIGURATION ===
TMDB_API_KEY = "4cf8d9f210c05b597cb5fd41e0e30889"
TMDB_BASE_URL = "https://api.themoviedb.org/3"
VIDSRC_BASE_URL = "https://vidsrc-embed.ru/embed"


# === HELPER FUNCTIONS ===

def tmdb_search(query, media_type="movie"):
    url = f"{TMDB_BASE_URL}/search/{media_type}"
    params = {"api_key": TMDB_API_KEY, "query": query}
    r = requests.get(url, params=params)
    if r.status_code != 200:
        return []
    return r.json().get("results", [])

def tmdb_get_details(media_type, tmdb_id):
    url = f"{TMDB_BASE_URL}/{media_type}/{tmdb_id}"
    params = {"api_key": TMDB_API_KEY}
    r = requests.get(url, params=params)
    return r.json() if r.status_code == 200 else {}

def tmdb_get_season_details(tv_id):
    url = f"{TMDB_BASE_URL}/tv/{tv_id}"
    params = {"api_key": TMDB_API_KEY}
    r = requests.get(url, params=params)
    if r.status_code != 200:
        return {}
    tv_info = r.json()
    return tv_info.get("seasons", [])


def make_vidsrc_embed_url(media_type, tmdb_id, **kwargs):
    params = [f"tmdb={tmdb_id}"]
    for k, v in kwargs.items():
        if v:
            val = quote(str(v)) if "url" in k else v
            params.append(f"{k}={val}")
    q = "&".join(params)
    return f"{VIDSRC_BASE_URL}/{media_type}?{q}"


# === ROUTES ===

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    query = ""
    media_type = "movie"
    if request.method == "POST":
        query = request.form.get("query")
        media_type = request.form.get("media_type", "movie")
        if query:
            results = tmdb_search(query, media_type)
    return render_template("index.html", results=results, query=query, media_type=media_type)


@app.route("/watch/<media_type>/<int:tmdb_id>", methods=["GET", "POST"])
def watch(media_type, tmdb_id):
    details = tmdb_get_details(media_type, tmdb_id)
    seasons = tmdb_get_season_details(tmdb_id) if media_type == "tv" else []
    
    season = episode = None
    ds_lang = sub_url = autoplay = autonext = None
    embed_url = None

    if request.method == "POST":
        if media_type == "tv":
            season = request.form.get("season")
            episode = request.form.get("episode")
            autonext = request.form.get("autonext", "0")
        ds_lang = request.form.get("ds_lang")
        sub_url = request.form.get("sub_url")
        autoplay = request.form.get("autoplay", "1")

        kwargs = {
            "ds_lang": ds_lang,
            "sub_url": sub_url,
            "autoplay": autoplay
        }
        if media_type == "tv":
            kwargs.update({"season": season, "episode": episode, "autonext": autonext})
        embed_url = make_vidsrc_embed_url(media_type, tmdb_id, **kwargs)

    return render_template(
        "watch.html",
        media_type=media_type,
        details=details,
        tmdb_id=tmdb_id,
        embed_url=embed_url,
        seasons=seasons
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
