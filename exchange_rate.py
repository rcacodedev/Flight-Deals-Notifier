import requests
from config import API_EXCHANGE_RATE

def get_exchange_rate(base_currency, target_currency):
        endpoint = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"

        params = {
                "apikey": API_EXCHANGE_RATE,
        }

        try:
            response = requests.get(url=endpoint, params=params)
            response.raise_for_status()
            data = response.json()

            # Check if the target currency is present in the rates
            rate = data["rates"].get(target_currency)
            if rate is not None:
                return rate
            else:
                raise KeyError(f"No exchange rate found for {target_currency}")
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching exchange rate: {e}")
            return None

def convert_currency(amount, exchange_rate):
    """
    Convert the given amount using the provided exchange rate.
    
    :param amount: The amount to convert.
    :param exchange_rate: The exchange rate.
    :return: The converted amount.
    """
    if exchange_rate is not None:
        converted_amount = amount * exchange_rate
        return converted_amount
    else:
        return None
