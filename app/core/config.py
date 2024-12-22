import os
from dotenv import load_dotenv

load_dotenv()

FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")

config = {
    "FINNHUB_API_BASE_URL": "https://finnhub.io/api/v1/",
    "FINNHUB_WEBSOCKET_URL": "wss://ws.finnhub.io"
}
