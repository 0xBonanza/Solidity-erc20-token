from scripts.helpful_scripts import get_account
from brownie import ShelterToken, network, config
from web3 import Web3

INITIAL_SUPPLY = Web3.toWei(1000000, "ether")  # initial supply of the token
ACCOUNT = get_account()  # account that creates the contract
RECEIVER = ACCOUNT  # receiver of the initial supply (could be another contract for instance)


def deploy_token():
    shelter_token = ShelterToken.deploy(RECEIVER,
                                        INITIAL_SUPPLY,
                                        {"from": ACCOUNT},
                                        publish_source=config["networks"][network.show_active()]["verify"])
    print(f"Shelter token deployed at {shelter_token.address}")
    print(f"Initial supply of {Web3.fromWei(INITIAL_SUPPLY, 'ether')} distributed to {RECEIVER}")


def main():
    deploy_token()
