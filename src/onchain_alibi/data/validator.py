from web3 import Web3 
import os 

def validate_address(addr: str) -> bool:
    """    Validate if the given address is a valid Ethereum address.
    
    Args:
        address (str): The wallet address to validate.
        
    Returns:
        bool: True if the address is valid, False otherwise.
    """
    if not Web3.is_address(addr):
        raise ValueError("Invalid Ethereum address") 
    return Web3.to_checksum_address(addr)

def get_api_key() -> str: 
    """    Get the Etherscan API key from environment variables.
    
    Returns:
        str: The Etherscan API key.
        
    Raises:
        ValueError: If the API key is not set in environment variables.
    """
    key = os.getenv("ETHERSCAN_API_KEY")
    if not key:
        raise EnvironmentError("ETHERSCAN_API_KEY is not set in environment variables")
    return key


    