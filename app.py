from flask import Flask, render_template, request, redirect
from db import get_db
from utils import get_video_metadata
from bson.objectid import ObjectId

app = Flask(__name__)

# Home route – show form + video list
@app.route('/', methods=['GET', 'POST'])

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

@app.route("/terms")
def terms():
    return render_template("terms.html")
    
def index():
    db = get_db()
    videos = list(db.videos.find().sort('_id', -1))  # Latest first

    if request.method == 'POST':
        video_url = request.form.get('video_url')
        if video_url:
            metadata = get_video_metadata(video_url)
            db.videos.insert_one({
                'url': video_url,
                'title': metadata['title'],
                'thumbnail': metadata['thumbnail']
            })
            return redirect('/')

    return render_template('index.html', videos=videos)

# Optional: delete a video
@app.route('/delete/<video_id>')
def delete(video_id):
    db = get_db()
    db.videos.delete_one({'_id': ObjectId(video_id)})
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
