from fastapi import FastAPI
from onchain_alibi.features.fingerprint import build_features
from onchain_alibi.models.similarity import score
from onchain_alibi.data.fetcher import fetch_data

app = FastAPI()

@app.get("/score/{address}")
def score_wallet(address: str):
    """
    Calculate a similarity score for a given wallet address.
    
    Args:
        address (str): The wallet address to score.
        
    Returns:
        dict: A dictionary containing the wallet address and its similarity score.
    """
    txs = fetch_data(address)
    features = build_features(txs)
    trust_score = score(features)
    return {"address": address, "trust_score": trust_score}