# solutions to ethernaut challenges in brownie

https://ethernaut.openzeppelin.com/

## setup

create .env file with the following

```
#your private key from metamask
export PRIVATE_KEY=0x00000000000000000000000000000

#your infura project id (register a free account on infura.io)
export WEB3_INFURA_PROJECT_ID=abcd1234
```

## run

1. get your game instance address on ethernaut
2. paste in address in scripts (eg. deploy_coinflip.py)
3. run script to solve the challenge (eg. brownie run deploy_coinflip --network rinkeby)
4. click submit instance on ethernaut