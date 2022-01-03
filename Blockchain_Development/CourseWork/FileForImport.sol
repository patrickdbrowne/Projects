pragma solidity ^ 0.5.13;

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