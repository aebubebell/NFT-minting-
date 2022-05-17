import json
from algosdk.v2client import algod
from algosdk import account, mnemonic
from algosdk.future.transaction import AssetConfigTxn, AssetTransferTxn, AssetFreezeTxn
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Shown for demonstration purposes. NEVER reveal secret mnemonics in practice.
# Change these values with your mnemonics
#mnemonic1 = " nasty heavy regret bundle hundred say spray lazy reduce satisfy average shine lottery special much flush trim bomb umbrella crash divorce another marriage about around"
from secrets import (
    ALGOD_ADDRESS,
    ALGOD_HEADERS,
    account_address,
    account_private_key

)


# For ease of reference, add account public and private keys to


# Specify your node address and token. This must be updated.
# algod_address = ""  # ADD ADDRESS
# algod_token = ""  # ADD TOKEN


# Initialize an algod client
algod_client = algod.AlgodClient(algod_token="", algod_address=ALGOD_ADDRESS, headers=ALGOD_HEADERS)

def wait_for_confirmation(client, txid):
    """
    Utility function to wait until the transaction is
    confirmed before proceeding.
    """
    last_round = client.status().get('last-round')
    txinfo = client.pending_transaction_info(txid)
    while not (txinfo.get('confirmed-round') and txinfo.get('confirmed-round') > 0):
        print("Waiting for confirmation")
        last_round += 1
        client.status_after_block(last_round)
        txinfo = client.pending_transaction_info(txid)
    print("Transaction {} confirmed in round {}.".format(txid, txinfo.get('confirmed-round')))
    return txinfo

def main():
    # TRANSFER ASSET
    # transfer asset of 10 from account 1 to account 3
    params = algod_client.suggested_params()
    # comment these two lines if you want to use suggested params
    # params.fee = 1000
    # params.flat_fee = True
    txn = AssetTransferTxn(
        sender=account_address,
        sp=params,
        receiver="UAHTM3EC3PTNDYBA5AGPHVBMXOK4YQE3N23VQEUFAMTHY3AXHBUXDHIWKE",
        amt=1,
        index=82787313)
    stxn = txn.sign(account_private_key)
    # Send the transaction to the network and retrieve the txid.
    try:
        txid = algod_client.send_transaction(stxn)
        print("Signed transaction with txID: {}".format(txid))
        # Wait for the transaction to be confirmed
        confirmed_txn = wait_for_confirmation(algod_client, txid)
        print("TXID: ", txid)
        print("Result confirmed in round: {}".format(confirmed_txn['confirmed-round']))
    except Exception as err:
        print(err)
if __name__ == '__main__':
    main()