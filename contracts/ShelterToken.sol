// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract ShelterToken is ERC20 {

    constructor(address _receiver, uint256 _initialSupply) ERC20("Shelter Token", "SHT") {
        _mint(_receiver, _initialSupply);
    }

}