import requests, time 
from typing import List, Dict 
from .validator import validate_address, get_api_key

BASE_URL = "https://api.etherscan.io/api"
OFFSET = 10_000 # Max per page
RATE = 0.25 

def fetch_data(addr:str, max_pages: int = 1) -> List[Dict]:
    """
    Fetch transaction data for a given wallet address from Etherscan API.
    
    Args:
        addr (str): The wallet address to fetch transactions for.
        max_pages (int): The maximum number of pages to fetch. Default is 1.
        
    Returns:
        List[Dict]: A list of transaction dictionaries.
    """
    addr = validate_address(addr)
    key = get_api_key() 
    
    all_rows: List[Dict] = [] 
    for page in range(1, max_pages + 1):
        url = (
            f"{BASE_URL}?module=account&action=txlist"
            f"&address={addr}&page={page}&offset={OFFSET}"
            f"&sort=asc&apikey={key}"
        )
        r = requests.get(url, timeout=15)
        if r.status_code != 200:
            raise ConnectionError(f"Failed to fetch data: {r.status_code} {r.reason}")
        payload = r.json() 
        if payload["status"] != "1":
            break 
        rows = payload["result"]
        all_rows.extend(rows)
        if len(rows) < OFFSET:
            break 
        time.sleep(RATE)
    return all_rows