from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from exchange_rate import get_exchange_rate, convert_currency
from notification_manager import NotificationManager
from config import ACCOUNT_SID, AUTH_TOKEN, PHONE

# Class instances
flight_search = FlightSearch()
data_manager = DataManager()
notification_manager = NotificationManager(account_sid=ACCOUNT_SID, auth_token=AUTH_TOKEN)

# Default values
lowest_price = 0

# Get user input for the departure city
user_city_name = input("Enter your departure city name: ")

# Fetch data from the Google Sheet
sheet_data = data_manager.get_information_sheet()

# Find the entry corresponding to the user's city
user_entry = next((entry for entry in sheet_data if entry["city"].lower() == user_city_name.lower()), None)

if user_entry:
    # Get the departure airport code for the user's city
    departure_airport_code = user_entry.get("iataCode", "TESTING")

    # Get date strings for tomorrow and 6 months later
    departure_date = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
    return_date = (datetime.now() + timedelta(days=6 * 30)).strftime("%d/%m/%Y")

    # Perform flight search
    flights = flight_search.search_flights(departure_airport_code, departure_date, return_date)

    # Print flight information
    for flight in flights:
        # Get the exchange rate from GBP to EUR (for example)
        exchange_rate_gbp_to_eur = get_exchange_rate("GBP", "EUR")

        # Perform a conversion from GBP to EUR
        amount_in_eur = convert_currency(flight.price, exchange_rate_gbp_to_eur)

        # Compare to the lowest price on Google Sheet
        if amount_in_eur < lowest_price or lowest_price == 0:
            # Update the lowest price recorded
            lowest_price = amount_in_eur
            # Create the message to send
            message_body = (
                f"Precio: {amount_in_eur:.2f} EUR\n"
                f"Departure City: {flight.departure_city}\n"
                f"Departure Airport IATA: {departure_airport_code}\n"
                f"Arrival City: {flight.destination_city}\n"
                f"Arrival Airport IATA: {flight.departure_airport_code}\n"
                f"Outbound Date: {departure_date}\n"
                f"Inbound Date: {return_date}"
            )

            # Send the message using NotificationManager
            notification_manager.send_twilio_message(message_body, PHONE)
else:
    print(f"City '{user_city_name}' not found in the Google Sheet.")
