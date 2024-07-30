import logging
from hfc.fabric import Client
from pathlib import Path

logger = logging.getLogger(__name__)

def load_network_profile(profile_path: str) -> Client:
    network_json_path = Path(profile_path).resolve()
    logger.info(f"Resolved network JSON path: {network_json_path}")

    if not network_json_path.exists():
        logger.error(f"The network configuration file {network_json_path} does not exist.")
        raise FileNotFoundError(f"The network configuration file {network_json_path} does not exist.")

    try:
        client = Client(net_profile=str(network_json_path))
        org1_admin = client.get_user(org_name='org1.example.com', name='jona')
        logger.info("Client initialized successfully.")
        print(client.organizations, "organizations")
        print(client.peers, "peers")
        print(client.orderers, "orderers")
        print(client.CAs, "CA_CERTS")
        # print(client.cryptoSuite, "CryptoSuite")
        return client
    except Exception as e:
        logger.error(f"Failed to initialize the client: {str(e)}")
        raise

def validate_network(client: Client):
    try:
        # Orderer validation
        orderers = client.orderers
        if not orderers:
            logger.warning("No orderers found in the network profile.")
        for orderer_name, orderer in orderers.items():
            logger.info(f"Connected to orderer: {orderer_name}")
            
        # Peer validation
        peers = client.peers
        if not peers:
            logger.warning("No peers found in the network profile.")
        for peer_name, peer in peers.items():
            logger.info(f"Connected to peer: {peer_name}")
            
        # # Channel validation
        # channel_name = "mychannel"  # Replace with your actual channel name
        # channel = client.get_channel(channel_name)
        # if channel:
        #     logger.info(f"Successfully accessed channel: {channel_name}")
        # else:
        #     logger.error(f"Channel {channel_name} does not exist.")
            
        # TLS Configuration Check
        for peer_name, peer in peers.items():
            tls_cert = getattr(peer, 'tls_cert', None) 
            if tls_cert:
                logger.info(f"TLS certificate for peer {peer.url} is properly configured.")
            else:
                logger.warning(f"No TLS certificate found for peer {peer}.")
    except Exception as e:
        logger.error(f"Network validation error: {str(e)}")
        raise