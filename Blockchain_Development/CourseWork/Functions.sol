pragma solidity ^0.5.13;

contract FunctionsExample {

    //the following two variables are class variables that are unique to each deployment of the smart contract, like with classes in other languages.
    //these are storage variables in solidity

    mapping (address => uint) public balanceReceived; 

    //create a payable variable
    address payable owner;

    constructor() public {
        //owner is address or person that deployed contract
        owner = msg.sender;
    }

    function destroySmartContract() public {
        require(msg.sender == owner, "Only the owner can destroy this smart contract...");
        //"destroys" smart contract giving remaining balance to the owner.
        selfdestruct(owner);
    }

    //A public function, that reads, returns an address value.
    function getOwner() public view returns(address) {
        return owner;
    }

    // a pure function does not interact with storage variables.
    function convertWeiToEther(uint _amount) public pure returns(uint) {
        //1 Ether is synonymous with 1 * 10^18 Wei
        return _amount/1 ether;
    }
    function receiveMoney() public payable {
        //asserting the amount sent is 0 ETH or more
        assert(balanceReceived[msg.sender] + msg.value >= balanceReceived[msg.sender]);
        //adding amount sent by address to the mapping to be accessed later
        balanceReceived[msg.sender] += msg.value;

    }

    function withdrawMoney(address payable _to, uint _amount) public {
        //asserting amount withdrawn is 0 or more ETH
        assert(_amount >= 0);
        require(_amount <= balanceReceived[msg.sender], "You need more funds!");
        balanceReceived[msg.sender] -= _amount;
        _to.transfer(_amount);
    }
    /**The following code is a 'fallback' function. This allows the smart contract to receive money without pressing
    buttons or function, and via the address (like through an external app - metamask)
    actual fallback function notation is: "function ()"
    The function is called when the function-call in the transaction is not found.
    */
    function () external payable {
        receiveMoney();
    }
}
/**
HIERARCHY OF FUNCTIONS
The types of functions that can be called depends on it's privileges and purpose. In other words, 

writing functions i.e., destroySmartContract:
    - can call view functions 
    - can call pure functions
view functions (can only read):
    - can call view functions
    - can call pure functions
    - cannot call writing functions
pure functions (cannot interact with storage variables):
    - cannot call view functions
    - can call pure functions
    - cannot call writing functions

TYPES OF FUNCTIONS
- pure functions
- view function
- public 
    can be called internally and externally relative to the Smart Contract.
- private
    can only be called within the contract (the code) meaning the button will disappear when deployed (because that's an external interaction).
- external 
    can be called from other contracts.
    can be called externally
- internal
    like private functions, but can also be called from derived contracts.

THE CONSTRUCTOR
equivalent to __init__ in Python: called once and only once when the contract is deployed.

ALLOWING PEOPLE TO INTERACT IFF THEY SEND MONEY THROUGH:
require(msg.data.length == 0);
*/