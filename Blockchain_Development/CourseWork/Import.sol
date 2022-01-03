pragma solidity ^0.5.13;

//This third part imports a file to be used, similar to other languages. Note the "./" means same directory
//The actual code is identical to Inheritance.sol
//Make sure to run this file and not accidentally "FileForImport.sol" in remix

import "./FileForImport.sol";

//"contract A is B" extends A from B, so A has the same attributes, methods (like in Python etc.) and modifiers as B. This is inheritance in solidity.
contract InheritanceModifierExample is Owned {

    mapping(address => uint) public tokenBalance;

    uint tokenPrice = 1 ether;

    constructor() public {
        tokenBalance[owner] = 100;
    }

    // call modifier after the "public/private/..." keyword. the modifier code is copied back to this function then everything is called remember...
    function createNewToken() public onlyOwner {
        tokenBalance[owner]++;
    }
    
    function burnToken() public onlyOwner{
        tokenBalance[owner]--;
    }

    function purchaseToken() public payable {
        require((tokenBalance[owner] * tokenPrice) / msg.value > 0, "Not enough tokens");
        tokenBalance[owner] -= msg.value / tokenPrice;
        tokenBalance[msg.sender] += msg.value / tokenPrice;
    }

    function sendToken(address _to, uint _amount) public {
        require(tokenBalance[msg.sender] >= _amount, "Not enough tokens");
        assert(tokenBalance[_to] + _amount >= tokenBalance[_to]);
        assert(tokenBalance[msg.sender] - _amount <= tokenBalance[msg.sender]);
        tokenBalance[msg.sender] -= _amount;
        tokenBalance[_to] += _amount;
    }

}