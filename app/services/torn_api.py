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

        headers = {
            "Authorization": f"ApiKey {self.api_key}"
        }

        url = f"{BASE_URL}/market/{item_id}/itemmarket"

        all_listings = []
        item_info = None

        while url:

            response = requests.get(url, headers=headers)
            response.raise_for_status()

            data = response.json()

            # DEBUG
            print("\n===== PAGE =====")
            print(data["_metadata"])
            print(f"Listings on this page: {len(data['itemmarket']['listings'])}")

            if item_info is None:
             item_info = data["itemmarket"]["item"]

            all_listings.extend(data["itemmarket"]["listings"])

            url = data["_metadata"]["links"]["next"]

        return {
            "itemmarket": {
                "item": item_info,
                "listings": all_listings
            }
        }