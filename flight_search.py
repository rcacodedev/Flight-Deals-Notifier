import requests
from config import API_TEQUILA
from flight_data import FlightData

class FlightSearch:
    def __init__(self):
        self.api_endpoint = "https://tequila-api.kiwi.com/locations/query"
        self.tequila_endpoint = "https://tequila-api.kiwi.com/v2/search"

    def get_iata_code(self, city_name):
        """
        Get the IATA code for a given city.

        Args:
            city_name (str): The name of the city.

        Returns:
            tuple: A tuple containing the IATA code and the response data.
        """
        headers = {
            "apikey": API_TEQUILA,  # Reemplaza con tu clave de API
        }

        params = {
            "term": city_name,
        }

        try:    
            response = requests.get(self.api_endpoint, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()

            locations = data.get("locations", [])
            if locations:
                iata_code = locations[0]["code"]
                return iata_code, data
            else:
                print("No locations found for the specify city.")
                return None, data
        except requests.exceptions.RequestException as e:
            print(f"Error in location search: {e}")
            return None, None

    def search_flights(self, departure_airport_code, departure_date, return_date, max_stopovers=0):
        """
        Search for flights based on the specified parameters.

        Args:
            departure_airport_code (str): The departure airport code.
            departure_date (str): The departure date.
            return_date (str): The return date.
            max_stopovers (int): The maximum number of stopovers.

        Returns:
            list: A list of FlightData objects representing flight information.
        """
        headers ={
            "apikey": API_TEQUILA,
        }

        params ={
            "fly_from": departure_airport_code,
            "date_from": departure_date,
            "date_to": return_date,
            "max_stopovers": max_stopovers,
        }
        try:
            response = requests.get(url=self.tequila_endpoint, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()

            flight_data_list = []
            for route in data["data"]:
                price = route["price"]
                destination_city = route["cityTo"]
                departure_city = route["cityFrom"]
                destination_airport_code = route["flyTo"]

                flight_data = FlightData(price, departure_airport_code, departure_city, destination_city)
                flight_data_list.append(flight_data)

            return flight_data_list
        except requests.exceptions.RequestException as e:
            print(f"Error in flight search: {e}")
            return []