pragma solidity ^0.8;

contract StartStopUpdateExample {

    address public owner;
    bool public paused;
    //Just like classes, a constructor automatically assigns variables (does something) when contract is called
    
    constructor() public {
        //owner is address/person who deploys contract
        owner = msg.sender;
    }
    function sendMoney() payable public {

    }
    //owner can pause contract so it won't execute
    function setPaused() public {
        require(owner == msg.sender, "oh my gah you're not the owner >:(");
        paused = !paused;
    }

    //transfers all money in smart contract to givenaddress
    function withdrawMoney(address payable _to) public {
        //In solidity, require is the equivalent to if statements (conditionals) for the code to continue in the function
        //param1 is the thing that needs to be true, param2 is the error or exception and the error message

        //owner must be the address withdrawing money so they're in control
        require(msg.sender == owner, "You're not the owner");
        require(!paused, "Soz contract is paused");
        _to.transfer(address(this).balance);
    }

    function destroySmartContract(address payable _to) public {
        //This function destroys the deployed Smart contract. But, the parameter is an address which will receive the remaining balance in the smart contract
        //so it's basically not wasted. Once this code runs:
        /**
        "You can still send transactions to the address and transfer Ether there, but there won't be any code that could send you the Ether back."
        */
        require(msg.sender == owner, "You are not the owner");
        selfdestruct(_to);
    }
}


/**
For contracts to undergo transactions, an external account (one with a private key) needs to initiate it.

It is the blockchain (ledger or database) that stores information about each address (balance and transfer), but each address stores a private key. So money is not 
inside the wallet, just the blockchain.

.send() returns a boolean (true if transaction succeeded, false if it didn't go through or there's an exception)

IMPORTANT GLOBAL PROPERTIES
msg.sender - address of person who called the function or deployed contract
msg.value - amount of ETH the contract received
now - current timestamp (plus or minus 15 seconds because of miners so not extremely accurate)

A function receives ETH if it is "payable". Keyword must be used in code.

to.transfer(address(this).balance)
the "to" is the address the money is going to 
the address(this).balance is the amount of money being transferred from smart contract to "to"
*/