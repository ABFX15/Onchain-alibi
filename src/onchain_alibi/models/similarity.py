def score(features) -> float:
    """
    Calculate a similarity score based on the provided features.
    
    Args:
        features (dict): A dictionary containing feature values.
        
    Returns:
        float: A similarity score between 0 and 1.
    """
    score = 0 
    if features["tx_count"] > 50:
        score += 20
    if features["dex_interactions"] > 2:
        score += 30
    if features["active-days"] >= 5:
        score += 10
    return min(score, 100)