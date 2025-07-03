from dataclasses import dataclass
from datetime import datetime

@dataclass
class Tx: 
    """Transaction data structure."""
    hash: str 
    block_number: int 
    timestamp: datetime 
    from_address: str 
    to: str | None 
    value_eth: float 
    gas_used: int 
    gas_price_gwei: float 