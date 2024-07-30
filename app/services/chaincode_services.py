from hfc.fabric import Client
from app.config.config import settings
import asyncio
from pathlib import Path

network_json_path = Path("app/config/network.json").resolve()
print(f"Resolved network JSON path: {network_json_path}")

if not network_json_path.exists():
    raise FileNotFoundError(f"The network configuration file {network_json_path} does not exist.")

client = Client(net_profile="app/config/network.json")
print("Client intitilzd in add product", client)
print("Organizations:", client.organizations)
org1_admin = client.get_user('Org1', 'Admin')
print(org1_admin, "org1_admin")
print(client.organizations, "organizations" , "ADD PRODUCT")


async def add_product_to_ledger(product_data: dict):
    args = [
        product_data['contractId'],
        product_data['productName'],
        str(product_data['quantity']),
        product_data['quality'],
        ','.join(product_data['farmerIds']),
        str(product_data['offTakerID']),
        str(product_data['logisticID']),
        product_data['deliveryStatus']
    ]
    print(args, "ARGS")
    
    try:
        # await client.connect()  # Connect to the Fabric network
        response = await client.chaincode_invoke(
        requestor=org1_admin,
        channel_name='mychannel3',
        peers=['peer0.org1.example.com'],
        cc_name='mycc',
        args=["AddProduct","contract2","Product1","10","High","[\"farmer1\",\"farmer2\"]","1","2","Delivered"],
        wait_for_event=True
        )
    except Exception as e:
        print(f"Error invoking chaincode: {e}")
        return {"error": str(e)}

    print(response, "Herer")

    return response

# ... rest of your code
