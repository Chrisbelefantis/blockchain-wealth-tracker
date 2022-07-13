// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.5;

contract AddressStorage {
    mapping(address => bool) public Wallet;

    function addAdress(address _wallet) public {
        Wallet[_wallet] = true;
    }

    function contains(address _wallet) public view returns (bool) {
        return Wallet[_wallet];
    }
}
