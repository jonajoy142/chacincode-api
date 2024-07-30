from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    # Hardcode the path directly
    FABRIC_NETWORK_CONFIG: str = "app/config/network.json"

    class Config:
        # No need for env_file since we're hardcoding the path
        env_file = None

# Initialize settings
settings = Settings()

# Verify the path to network.json
network_json_path = Path(settings.FABRIC_NETWORK_CONFIG).resolve()
if not network_json_path.exists():
    raise FileNotFoundError(f"The network configuration file {network_json_path} does not exist.")
