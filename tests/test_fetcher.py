import unittest 
from onchain_alibi.data.fetcher import fetch_data
 
def test_fetch_account():
    """Test that we can fetch transactions for a valid Ethereum address"""
    txs = fetch_data("0xd8da6BF26964af9d7eed9e03e53415d37aa96045", max_pages=1)
    assert len(txs) > 0, "No transactions fetched for the account"
    assert isinstance(txs, list), "Expected a list of transactions"
    # Check that the first transaction has expected fields
    if txs:
        tx = txs[0]
        assert "value" in tx, "Transaction should have a 'value' field"
        assert "hash" in tx, "Transaction should have a 'hash' field"
        assert "from" in tx, "Transaction should have a 'from' field"
        print(f"Successfully fetched {len(txs)} transactions")

if __name__ == "__main__":
    test_fetch_account()