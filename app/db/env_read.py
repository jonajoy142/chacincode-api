from typing import Dict
from os import environ, path, getcwd
from dotenv import load_dotenv
from app.constants.app_constants import AppConsts
import requests

env_path = path.join(getcwd(), r"app/.env")
print(env_path)
load_dotenv(env_path)


def read_env_variables() -> Dict[str, str]:
    """
    Read environment variables
    """
    env_dict = {}
    # implement get the variables from
    # AWS lambda --> only in the production/dev in aws
    response = get_from_secret_manager()
    if response:
        print("Reading from secret manager")
        if AppConsts.ENV == 'DEV':
            env_dict['host'] = response['DEV_DB_HOST']
            env_dict['user'] = response['DEV_DB_ROOT_USER']
            env_dict['password'] = response['DEV_DB_ROOT_PWD']
            env_dict['db'] = response['OLA_DEV_DB']
            env_dict['map_key'] = response['GMAP_API_KEY']
            return env_dict
    # if first is failed to get then read from .env file (locally)
    print(f"Reading from .env file {env_path}")
    env_dict['host'] = environ.get('DB_HOST')
    env_dict['user'] = environ.get('DB_USER')
    env_dict['password'] = environ.get('DB_PWD')
    env_dict['db'] = environ.get('DB')
    return env_dict


def get_from_secret_manager():
    """
    Get the variables from AWS secret manager
    """
    try:
        host: str = 'https://mgpp6396b6.execute-api.ap-south-1.amazonaws.com'
        endpoint: str = 'secrets/secrets'
        url: str = f"{host}/{endpoint}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None
    except Exception:
        return None
