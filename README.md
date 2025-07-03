## Onchain Alibi 

# A Python app that:
1. Analyzes wallet behavior (tx timing, DEX usage, contracts interacted with, signature patterns)
2. Generates a unique “behavior fingerprint”

# Flags:
- Suspicious similarities between wallets
- “Sleeper” Sybils (wallets that wake only for drops)
- Contract interaction patterns that suggest automation
- Outputs a trust score, wallet similarity %, and optional verdict ("likely same user")