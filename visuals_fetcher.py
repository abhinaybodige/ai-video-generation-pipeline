import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("PEXELS_API_KEY")

def refine_query(topic):

    topic = topic.lower()

    if "bumrah" in topic:
        return "Jasprit Bumrah fast bowler India cricket bowling yorker"

    if "virat" in topic:
        return "Virat Kohli batting India cricket"

    if "ai" in topic or "artificial intelligence" in topic:
        return "artificial intelligence technology robot futuristic"

    # default fallback
    return topic

def fetch_images(topic, count=8):
    search_query = refine_query(topic)
    url = "https://api.pexels.com/v1/search"
    headers = {
        "Authorization": API_KEY
    }
    params = {
        "query": search_query,
        "per_page": count,
        "orientation": "landscape"
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    image_paths = []

    for i, photo in enumerate(data["photos"]):
        img_url = photo["src"]["large"]

        img_data = requests.get(img_url).content
        file_name = f"image_{i}.jpg"

        with open(file_name, "wb") as f:
            f.write(img_data)

        image_paths.append(file_name)

    return image_paths
