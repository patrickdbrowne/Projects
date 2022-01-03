pragma solidity ^0.8;
//THIS IS A 3 PART PROGRAM THAT DOES THE SAME THING BUT WITH MODIFIERS, INHERITANCE, AND IMPORTING FILES
//This smart contract enables exchange of ETH and a made up token
contract InheritanceModifierExample {

    mapping(address => uint) public tokenBalance;

    address owner;

    uint tokenPrice = 1 ether;

    constructor() public {
        owner = msg.sender;
        tokenBalance[owner] = 100;
    }
    /**
    MODIFIER
    Modifiers are used to cut down on repetition. Since there are two require statement in the following functions, a modifier can be used
    to copy and paste the same code in different functions:
    It's equivalent to --
    function createNewToken() public {
        require(msg.sender == owner, "You are not allowed");
        tokenBalance[owner]++;
    }

    function burnToken() public {
        require(msg.sender == owner, "You are not allowed");
        tokenBalance[owner]--;
    }

    */

    modifier onlyOwner() {
        //the underscore copies the function's code it's used in
        _;
        require(msg.sender == owner, "Only the owner can use this function...");

        //after all the code, the whole thing is copied back or just called.
    }

    // call modifier after the "public/private/..." keyword. the modifier code is copied back to this function then everything is called remember...
    function createNewToken() public onlyOwner {
        tokenBalance[owner]++;
    }
    
    function burnToken() public onlyOwner{
        tokenBalance[owner]--;
    }

    function purchaseToken() public payable {
        require((tokenBalance[owner] * tokenPrice) / msg.value > 0, "not enough tokens");
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