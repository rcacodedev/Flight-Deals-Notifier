import requests
from config import SHEETY_ENDPOINT, BASE_URL, AUTH_BEARER


class DataManager:
    def __init__(self) -> None:
        self.sheety_endpoint = SHEETY_ENDPOINT
        self.headers = {
            "Authorization": AUTH_BEARER,
            "Content-Type": "application/json",
        }

    def get_information_sheet(self):
        try:
            response = requests.get(url=self.sheety_endpoint)
            response.raise_for_status()
            data = response.json()
            sheet_data = data.get("prices", [])
            return sheet_data
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return None
        except ValueError as e:
            print(f"Error decoding JSON: {e}")
            return None
    
    def update_sheet_with_iatas_code(self, sheet_data):
        base_url = BASE_URL

        for entry in sheet_data:
            row_id = entry.get("id")
            iata_code = entry.get("iataCode")

            if row_id and iata_code:
                sheety_row_endpoint = f"{BASE_URL}/{row_id}"

                payload = {
                    "price": {
                        "iataCode": iata_code
                    }
                }
                try:
                    response = requests.put(url=sheety_row_endpoint, headers=self.headers, json=payload)
                    response.raise_for_status()

                    if response.status_code == 200:
                        print(f"Row with ID {row_id} updated successfully.")
                    else:
                        print(f"Error updating row with ID {row_id}. Status code: {response.status_code}")
                except requests.exceptions.RequestException as e:
                    print(f"Error updating row with ID {row_id}: {e}")
            else:
                print("Missing information to perform the update.")
