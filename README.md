# Flight Deals Notifier

## Overview

This project is a flight deals notifier that helps you find the best flight deals from London to various destinations. It utilizes the Tequila API for flight searches, Sheety API for Google Sheets integration, and Twilio API for sending notifications.

## Features

- Automatically updates IATA codes in the Google Sheet.
- Search for flight prices from the airport that the user enters.
- Converts the ticket price to euros, if the price is given in GBP.
- Sends an SMS notification if a flight deal is found with a price lower than the specified threshold.

## Setup

### Prerequisites

- Python 3
- Pipenv (for managing dependencies)
- Account in API's Sheety, Kiwi, Open Exchange Rates and Twilio.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/rcacodedev/Flight-Deals-Notifier.git
   cd flight-deals-notifier
