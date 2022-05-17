from django.http import HttpResponse
import requests

# TODO USE THIS package
from algosdk.v2client import algod

# TODO Feel free to copy-paste the secrets.py file into the Step3 folder and import it here

from secrets import (
    ALGOD_ADDRESS,
    ALGOD_HEADERS

)
PINATA_GATEWAY = "https://gateway.pinata.cloud/ipfs/"

# TODO fill me out
ASSET_ID = 82787313

def serve_image(request):
    # TODO modify this function to:
    def ipfs_to_cid (address) :
        return address.replace("ipfs://", "").replace("#arc3", "")

    client = algod.AlgodClient(algod_token="", algod_address=ALGOD_ADDRESS, headers=ALGOD_HEADERS)
    # 1. Query the algorand blockchain for your NFT
    q = client.asset_info(ASSET_ID)
    # 2. Recover the IPFS Metadata address from the NFT
    ipfs_md_addy = q['params']['url']
    # 3. Query the metadata from IPFS
    md_cid = ipfs_to_cid(ipfs_md_addy)
    url = PINATA_GATEWAY + md_cid
    response = requests.get(url)
    response_dict = response.json()
    # 4. Extract the IPFS image address
    img_addy = response_dict['image']
    # 5. Query the image from IPFS
    img_cid = ipfs_to_cid(img_addy)
    img_url = PINATA_GATEWAY + img_cid
    img_response = requests.get(img_url)
    # 6. Serve the image as an HTTP response
    content_type=response_dict['image_mimetype']
    # image_bytes = open("../beautiful_temple.jpeg", "rb")
    print(response)
    print(response_dict)
    return HttpResponse(img_response.content, content_type=content_type)

def home_page(request):
    return HttpResponse("<h1>Visit localhost:8000/nft to view your NFT!</h1>")
