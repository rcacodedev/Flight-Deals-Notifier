class FlightData:
    def __init__(self, price, departure_airport_code, departure_city, destination_city):
        """
        Constructor for FlightData class.

        Args:
            price (float): The price of the flight.
            departure_airport_code (str): The IATA code of the departure airport.
            departure_city (str): The city of departure.
            destination_city (str): The city of arrival.
        """
        self.price = price
        self.departure_airport_code = departure_airport_code
        self.departure_city = departure_city
        self.destination_city = destination_city

    