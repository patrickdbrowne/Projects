pragma solidity ^0.8;
//This second part utilises inheritance by making a second contract (even though you should try to limit contracts made)
contract Owned {
    address owner;

    constructor () public {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        //the underscore copies the function's code it's used in
        _;
        require(msg.sender == owner, "Only the owner can use this function...");

        //after all the code, the whole thing is copied back or just called.
    }

}

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