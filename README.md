# 🎥 Video Link Embedder (Full-Stack Flask App)

Paste any video link and it will:
- ✅ Show the embedded video player
- ✅ Extract and display title + thumbnail automatically
- ✅ Save to MongoDB for listing later

---

## 🔧 Tech Stack

- Frontend: HTML + CSS (Jinja templates)
- Backend: Python Flask
- Database: MongoDB Atlas
- Hosting: GitHub (frontend) + Render (backend)

---

## 🚀 Features

- Paste video links via form
- Auto-fetch video title & thumbnail
- Supports YouTube, Vimeo, and most websites (via og:image meta)
- Clean responsive UI
- Render-ready deployment (uses Gunicorn)

---

## 📂 Project Structure
video-link-app/ ├── app.py ├── db.py ├── utils.py ├── requirements.txt ├── Procfile ├── runtime.txt ├── .env.example ├── templates/ │   └── index.html └── static/ └── style.css
---

## 🛠️ Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/video-link-app.git
cd video-link-app
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
MONGO_URI=your_mongodb_connection_string
MONGO_DB_NAME=video_links_app
MIT ©️ 2025 ANUP KUMAR
---

✅ Is README se koi bhi developer ya user aapka project **samajh bhi sakta hai aur chala bhi sakta hai**, chahe Render pe ho ya local machine par.
