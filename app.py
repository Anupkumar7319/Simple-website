from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv
from utils import get_video_metadata
import validators

load_dotenv()
app = Flask(__name__)

# MongoDB Connection (Atlas or Local)
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client['desi_hamster']
video_collection = db['videos']

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        video_url = request.form.get("video_url")
        if validators.url(video_url):
            meta = get_video_metadata(video_url)
            video = {
                "url": video_url,
                "title": meta['title'],
                "thumbnail": meta['thumbnail']
            }
            video_collection.insert_one(video)
        return redirect(url_for("index"))

    videos = list(video_collection.find())
    for v in videos:
        v['_id'] = str(v['_id'])
    return render_template("index.html", videos=videos)

@app.route("/delete/<video_id>")
def delete(video_id):
    try:
        video_collection.delete_one({"_id": ObjectId(video_id)})
    except:
        pass
    return redirect(url_for("index"))

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

@app.route("/terms")
def terms():
    return render_template("terms.html")

@app.route("/disclaimer")
def disclaimer():
    return render_template("disclaimer.html")

@app.route("/dmca")
def dmca():
    return render_template("dmca.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
