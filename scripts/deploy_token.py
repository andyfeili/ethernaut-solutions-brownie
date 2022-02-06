from brownie import Token, network, config,accounts

def main():
    #input the contract address
    #> contract.address
    contractAddress = '0xc67E60E767C61E84d9385260b0d3fe6388ad676d'

    #use player account
    player = accounts.add(config["wallets"]["from_key"])

    contract = Token.at(contractAddress)
