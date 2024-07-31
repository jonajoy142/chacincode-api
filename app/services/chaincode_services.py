from hfc.fabric import Client
from pathlib import Path
import asyncio

# Resolve and verify network JSON path
network_json_path = Path("app/config/network.json").resolve()
print(f"Resolved network JSON path: {network_json_path}")

if not network_json_path.exists():
    raise FileNotFoundError(f"The network configuration file {network_json_path} does not exist.")

# Initialize the Fabric client
client = Client(net_profile=str(network_json_path))
print("Client initialized:", client)

# Retrieve the admin user
org1_admin = client.get_user(org_name='org1.example.com', name='jona')
if org1_admin is None:
    print("Failed to retrieve user 'jona' from 'Org1'. Check the user definition and file paths.")
else:
    print("Successfully retrieved the user 'jona':", org1_admin)

# Print organizations and users for debugging
print("Organizations:", client.organizations)
for org_name, org in client.organizations.items():
    print(f"Org: {org_name}, MSP ID: {org._mspid}, Users: {org._users}")

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

        # channel = client.get_channel('mychannel3')
        # if not channel:
        #     raise ValueError("Channel 'mychannel3' could not be retrieved.")
        client.new_channel('mychannel3')
        channel = client.get_channel('mychannel3')
        if not channel:
            raise ValueError("Channel 'mychannel3' could not be retrieved.")
        peer = client.get_peer('peer0.org1.example.com')
        if not peer:
            raise ValueError("Peer 'peer0.org1.example.com' could not be retrieved.")
        
                # policy, see https://hyperledger-fabric.readthedocs.io/en/release-1.4/endorsement-policies.html
        policy = {
    'identities': [
        {'role': {'name': 'member', 'mspId': 'Org1MSP'}},
    ],
    'policy': {
        '1-of': [
            {'signed-by': 0},
        ]
    }
}
        
        # # Invoke the chaincode
        # response = await client.chaincode_invoke(
        #     requestor=org1_admin,
        #     channel_name='mychannel3',
        #     peers=['peer0.org1.example.com'],
        #     cc_name='mycc',
        #     fcn='AddProduct',
        #     args=args,
        #     wait_for_event=True
        # )
        # print("Chaincode response:", response)
        # return response
        response = await client.chaincode_query(
            requestor=org1_admin,
            channel_name='mychannel3',
            peers=['peer0.org1.example.com'],
            cc_name='mycc',   
            args=["GetProductDetails", "contract1"]
        )
        print("Chaincode query response:", response)
        return response

    except Exception as e:
        print(f"Error invoking chaincode: {e}")
        return {"error": str(e)}

# Example product data for testing
# product_data = {
#     'contractId': 'contract2',
#     'productName': 'Product1',
#     'quantity': 10,
#     'quality': 'High',
#     'farmerIds': ['farmer1', 'farmer2'],
#     'offTakerID': 1,
#     'logisticID': 2,
#     'deliveryStatus': 'Delivered'
# }

# # Run the function for testing
# async def main():
#     response = await add_product_to_ledger(product_data)
#     print("Add Product Response:", response)

# # Run the main function in the asyncio event loop
# if __name__ == '__main__':
#     asyncio.run(main())
