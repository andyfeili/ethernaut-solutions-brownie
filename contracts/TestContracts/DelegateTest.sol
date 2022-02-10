// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

contract TestTest {
    function pwn1() public{

    }

    function pwn2() public{

    }

    function pwn3() public {

    }
}

contract DelegateTest {

  address public owner;
  DelegateTest public delegate_test;
  DelegationTest public delegation_test;
  bytes public msgData;
  uint public receivedValue;

  constructor(address _owner) public {
    owner = _owner;
  }

  function pwn() public {
    owner = msg.sender;
  }
}

contract DelegationTest {

  address public owner;
  DelegateTest public delegate_test;
  DelegationTest public delegation_test;
  bytes public msgData;
  uint public receivedValue;
  uint public whichOne;

  constructor(address _delegateAddress) public {
    delegate_test = DelegateTest(_delegateAddress);
    owner = msg.sender;
  }

  fallback() external payable{
    (bool result,) = address(delegate_test).delegatecall(msg.data);
    //(bool result,) = address(delegate_test).delegatecall(abi.encodeWithSignature("pwn()"));

    if (result) {
      this;
    }

    delegation_test = this;
    msgData = msg.data;
    whichOne = 1;

  }

  receive() external payable{
    receivedValue = msg.value;
    msgData = msg.data;
    whichOne = 2;
  }

}