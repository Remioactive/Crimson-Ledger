import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TORN_API_KEY")

BASE_URL = "https://api.torn.com/v2"


class TornAPI:
    def __init__(self):
        if not API_KEY:
            raise ValueError("TORN_API_KEY not found in .env")

        self.api_key = API_KEY

    def get_item_market(self, item_id: int):
        url = f"{BASE_URL}/market/{item_id}/itemmarket"

        headers = {
            "Authorization": f"ApiKey {self.api_key}"
        }

        response = requests.get(url, headers=headers)

        response.raise_for_status()

        return response.json()