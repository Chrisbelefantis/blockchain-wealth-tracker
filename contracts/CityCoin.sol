// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "./AddressStorage.sol";

contract CityCoin is ERC20, AddressStorage {
    AddressStorage citizensClaimedToken = new AddressStorage();
    address public tokenHolder;

    constructor() ERC20("CityCoin", "CTY") {
        tokenHolder = msg.sender;
    }

    //Overiding the default ERC20 value for decimals and setting them
    //to 0.
    function decimals() public view virtual override returns (uint8) {
        return 0;
    }

    function claimToken(uint256 amount) public {
        require(
            !citizensClaimedToken.contains(msg.sender),
            "You have already claimed your CITY Token."
        );
        _mint(msg.sender, amount);
        citizensClaimedToken.addAdress(msg.sender);
    }
}
