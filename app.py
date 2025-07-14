from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import validators

app = Flask(__name__)

# MongoDB Connection (Local or MongoDB Atlas)
client = MongoClient("mongodb://localhost:27017/")
db = client['desi_hamster']
video_collection = db['videos']

# Dummy thumbnail & title extractor (you can enhance this)
def generate_thumbnail(url):
    # For simplicity, using a static image or placeholder
    return "https://via.placeholder.com/300x200.png?text=Video"

def extract_title(url):
    return "Untitled Video"  # You can improve this using YouTube API etc.

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        video_url = request.form.get("video_url")
        if validators.url(video_url):
            video = {
                "url": video_url,
                "title": extract_title(video_url),
                "thumbnail": generate_thumbnail(video_url)
            }
            video_collection.insert_one(video)
        return redirect(url_for("index"))

    videos = list(video_collection.find())
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
    return "<h2>Privacy Policy Page</h2>"

@app.route("/terms")
def terms():
    return "<h2>Terms & Conditions</h2>"

@app.route("/disclaimer")
def disclaimer():
    return "<h2>Disclaimer Page</h2>"

@app.route("/dmca")
def dmca():
    return "<h2>DMCA Page</h2>"

@app.route("/contact")
def contact():
    return "<h2>Contact Page</h2>"

if __name__ == "__main__":
    app.run(debug=True)
