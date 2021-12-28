pragma solidity ^0.8;

///"this" refers to the instance of the smart contract. Remember smart contracts receive and distribute assets
/**
MESSAGE OBJECT
Each transaction made carries a msg object which has different attributes. You can see this in the terminal. The msg.value gets the value of each transaction made
*/
contract SendMoney {
    ///"payable" means the function can receive money
    uint public balanceReceived;
    
    //This sends the money from the address to the smart contract instance
    function receiveMoney() public payable {
        ///Each time money is received, amount is added to "balanceReceived" or total received so far.
        balanceReceived += msg.value;

    } 

    //returns the amount of money in the current instance of the smart contract
    function getBalance() public view returns(uint) {
        return address(this).balance;
    }

    //The current address receives the balance
    function withdrawMoney() public {
        /**
        msg.sender is the address of the sender, or the person who calls "withdrawMoney()"
        the first payable makes the sender's address payable so it can receive money
        the code seems to work without the second "payable" but idk tbh. Here is a comment on the function from the 8.10.0 documentation:
            // address(test) will not allow to call ``send`` directly, since ``test`` has no payable
            // fallback function.
            // It has to be converted to the ``address payable`` type to even allow calling ``send`` on it.

        */
        
        address payable to = payable(msg.sender);
        to.transfer(getBalance());
    }

    //Sends the balance to another wallet address
    function withdrawMoneyTo(address payable _to) public {
        _to.transfer(this.getBalance());
    }

}