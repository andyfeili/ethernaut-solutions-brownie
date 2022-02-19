from brownie import MagicNum, config,accounts

#check contract address of SimpleToken on rinkeby ether scan
contractAddress = '0xca1893570177b7F121132f19BBB712648c3DE27e'
player = accounts.add(config["wallets"]["from_key"])

def solution():
    #https://medium.com/coinmonks/ethernaut-lvl-19-magicnumber-walkthrough-how-to-deploy-contracts-using-raw-assembly-opcodes-c50edb0f71a2
    #there is a typo in the solution given in the blog post above (repace 42 with 2A)
    bytes = '0x600a600c600039600a6000f3602A60805260206080f3'
    tx = player.transfer(data=bytes)
    contract=MagicNum.at(contractAddress)
    contract.setSolver(tx.contract_address,{"from":player})

def main():
    solution()