pragma solidity ^0.8;


/**
GAS CONSUMPTION
deploy as few contracts as possible to reduce gas prices. Gas prices are charged
for each deployed smart contract.

MAPPING ONTO STRUCTS
You can map onto structs to hold more data. Access values with [] and variables within structs with . 
e.g., "mapping(uint => A) public myStructMapping;"

Try to avoid arrays because it is expensive and increases gas price

ENUMS
*not a lot of detail
This is another user-defined datatype in solidity: enum ActionChoices {GoLeft, GoRight, GoStraight, SitStill}
*/
contract MappingsSctructExample {
    /**
    Structs are a user-defined data type that can store multiple related items. A struct variable is similar to a database record
    since it may contain multiple data types related to a single entity. A bit like an object?
    https://www.geeksforgeeks.org/solidity-enums-and-structs/

    Structs are initialised with default values like mappings.
    You can include structs of other types in struct members, but not of the same type making it discursive. i.e.,
    struct A {
        struct B
        uint number
    }
    the above is ok.

    Struct A {
        struct A
        uint number
    }
    this one is not
    */
    struct Payment {
        //amount of money paid
        uint amount;
        //time of transaction in milliseconds since Epoch unix (Jan 1, 1970)
        uint timestamps;
    }
    struct Balance {
        uint totalBalance;
        uint numPayments;
        mapping(uint => Payment) payments;
    }


    mapping(address => Balance) public balanceReceived;

    function getBalance() public view returns(uint) {
        return address(this).balance;
    }

    function sendMoney() public payable {
        //Access a variable from the structure (struct)
        // 1. accesses Balance value using sender's address as a key
        // 2. accesses the totalBalance variable in the Balance struct using the dot (.) like with attributes in Python
        // 3. Adds balance of the address in that value
        balanceReceived[msg.sender].totalBalance += msg.value;

        //Recording a Payment in memory (like RAM it only stores it during execution of the smart contract)
        //Each time this function is called, the memory creates a new instance of Payment payment, so is not carried 
        //through between functions.

        //Creates an instance of Payment object/structure. The parameters correspond with order of the variables listed. i.e.,
        //msg.value is amount, and block.timestamp is timestamps.
        /**
        msg.value is the amount sent (wei)
        block.timestamp is an alias for now. Interchangeable keywords.
        */
        Payment memory payment = Payment(msg.value, block.timestamp);

        
        balanceReceived[msg.sender].payments[balanceReceived[msg.sender].numPayments] = payment;
        balanceReceived[msg.sender].numPayments++;
    }

    function withdrawMoney(address payable _to, uint _amount) public {
        require(balanceReceived[msg.sender] >= _amount, "Insufficient funds :O");
        balanceReceived[msg.sender] -= _amount;
        _to.transfer(_amount);
    }

    function withdrawAllMoney(address payable _to) public {
        uint balanceToSend = balanceReceived[msg.sender];
        balanceReceived[msg.sender] = 0;
        _to.transfer(balanceToSend);
    }
}
  
  