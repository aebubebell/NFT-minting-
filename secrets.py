from algosdk import mnemonic

# TODO
PINATA_API_KEY = "8cde29e38e8dcb32950f"
PINATA_API_SECRET = "421dc73f2003d42e8ee317b8855f1e11eb3345c6ca920ae5a3abc9fc965759bc"

# TODO
PURESTAKE_API_KEY = "BMPOgGPnZO7nZJbMZgesgZMNtMqfFjB5Y3FUrtT0"

# TODO
account_mnemonic = "nasty heavy regret bundle hundred say spray lazy reduce satisfy average shine lottery special much flush trim bomb umbrella crash divorce another marriage about around"
account_private_key = mnemonic.to_private_key(account_mnemonic)
account_address = mnemonic.to_public_key(account_mnemonic)

ALGOD_ADDRESS = "https://testnet-algorand.api.purestake.io/ps2"
ALGOD_HEADERS = {"X-API-Key": PURESTAKE_API_KEY}
