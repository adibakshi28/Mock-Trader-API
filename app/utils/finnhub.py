import os
import httpx
from dotenv import load_dotenv
from app.core.config import config, FINNHUB_API_KEY
from typing import Dict, Any, List

load_dotenv()

FINNHUB_BASE_URL = config["FINNHUB_API_BASE_URL"]

# === UTILITY FUNCTION ===
async def make_request(endpoint: str, params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Make an asynchronous HTTP GET request to the Finnhub API.
    """

    url = f"{FINNHUB_BASE_URL}{endpoint}"
    params["token"] = FINNHUB_API_KEY


    print(f"Making request to {url} with params: {params}")

    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            return response.json()
    except httpx.TimeoutException:
        raise ConnectionError("❌ Finnhub API request timed out.")
    except httpx.HTTPStatusError as e:
        raise ConnectionError(f"❌ HTTP Error: {e}")
    except httpx.RequestError as e:
        raise ConnectionError(f"❌ Error in API Request: {e}")


# === FINNHUB API FUNCTIONS ===

async def get_stock_symbols(exchange: str) -> List[Dict[str, Any]]:
    """Get the list of supported stock symbols for an exchange."""
    return await make_request("stock/symbol", {"exchange": exchange})


async def get_market_status(exchange: str) -> Dict[str, Any]:
    """Get the current market status for an exchange."""
    return await make_request("stock/market-status", {"exchange": exchange})


async def get_market_holidays(exchange: str) -> List[Dict[str, Any]]:
    """Get a list of market holidays for an exchange."""
    return await make_request("stock/market-holiday", {"exchange": exchange})


async def get_company_profile(symbol: str) -> Dict[str, Any]:
    """Get the general profile of a company by its symbol."""
    return await make_request("stock/profile2", {"symbol": symbol})


async def get_company_news(symbol: str, from_date: str, to_date: str) -> List[Dict[str, Any]]:
    """Get the latest company news."""
    return await make_request("company-news", {"symbol": symbol, "from": from_date, "to": to_date})


async def get_basic_financials(symbol: str, metric: str = "all") -> Dict[str, Any]:
    """Get basic financial metrics for a company."""
    return await make_request("stock/metric", {"symbol": symbol, "metric": metric})


async def get_stock_quote(symbol: str) -> Dict[str, Any]:
    """Get real-time stock quote data."""
    return await make_request("quote", {"symbol": symbol})


# Usage
#   -> The function should be async def
#     try:
#         stock_price = await get_stock_quote("AAPL")
#         aapl_price = stock_price.get("c", "Price not available")
#     except Exception as e:
#         aapl_price = f"Failed to fetch price: {e}"

