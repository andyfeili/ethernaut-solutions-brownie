from brownie import GatekeeperTwoExploit, config,accounts

#input the contract address
#> contract.address
contractAddress = '0x5b3f369f8f6bf18DaC955dF97b2819eA9691CE84'
player = accounts.add(config["wallets"]["from_key"])

def solution():
    GatekeeperTwoExploit.deploy(contractAddress,{"from":player})

def main():
    solution()