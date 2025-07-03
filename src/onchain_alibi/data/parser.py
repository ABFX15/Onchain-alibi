from datetime import datetime 
from typing import List, Dict
from .types import Tx

def parse_row(row: Dict) -> Tx:
    """
    Parse a single transaction row into a Tx object.
    
    Args:
        row (Dict): A dictionary representing a transaction.
        
    Returns:
        Tx: A Tx object containing the parsed transaction data.
    """
    ts = datetime.fromtimestamp(int(row["timeStamp"]))
    return Tx(
        hash=row["hash"],
        block_number=int(row["blockNumber"]),
        timestamp=ts,
        from_address=row["from"],
        to=row.get("to"),
        value_eth=float(row["value"]) / 1e18,  
        gas_used=int(row["gasUsed"]),
        gas_price_gwei=float(row["gasPrice"]) / 1e9,  
    )
    
def rows_to_tx(rows: List[Dict]) -> List[Tx]: 
    """Convert a list of transaction rows to a list of Tx objects.
    
    Args:
        rows (List[Dict]): A list of dictionaries representing transactions.
        
    Returns:
        List[Tx]: A list of Tx objects.
    """
    return[parse_row(r) for r in rows]