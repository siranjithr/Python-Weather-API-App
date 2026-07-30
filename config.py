import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# API Key
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Default Units
UNITS = "metric"