import requests
from bs4 import BeautifulSoup

def get_video_metadata(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string.strip() if soup.title else "Untitled"
        thumbnail = None

        og_image = soup.find("meta", property="og:image")
        if og_image and og_image.get("content"):
            thumbnail = og_image["content"]
        else:
            twitter_image = soup.find("meta", attrs={"name": "twitter:image"})
            if twitter_image and twitter_image.get("content"):
                thumbnail = twitter_image["content"]

        return {
            "title": title,
            "thumbnail": thumbnail or "https://via.placeholder.com/320x180?text=No+Thumbnail"
        }

    except Exception:
        return {
            "title": "Unknown",
            "thumbnail": "https://via.placeholder.com/320x180?text=Error"
        }
