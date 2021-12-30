pragma solidity ^0.8;

contract MappingsSctructExample {

    //Each address has 0 balance by default
    mapping(address => uint) public balanceReceived;

    //Returns the balance of the smart contract
    function getBalance() public view returns(uint) {
        return address(this).balance;
    }

    //Adds the amount the address sent to it's value. E.g., address A sends 2 ETH, address B sends 5 ETH. The balance of the 
    //smart contract is 7 ETH, balance of address A is 2 ETH, and balance of address B is 5 ETH. 
    function sendMoney() public payable {
        balanceReceived[msg.sender] += msg.value;
    }

    //Allows address to withdraw partial amount from their balance. 1. Checks withdrawal amount is less than balance in sender,
    //2. Reduces balance of sender by _amount 3. Sends amount of money from sender to address. It could be sending money to itself
    //or someone else.
    function withdrawMoney(address payable _to, uint _amount) public {
        require(balanceReceived[msg.sender] >= _amount, "Insufficient funds :O");
        balanceReceived[msg.sender] -= _amount;
        _to.transfer(_amount);
    }

    //If address A withdraws it's money, it will get 2 ETH back and it's balance will be reset to 0. Write the code in this order.
    //Then, contract will have balance of 5 ETH, Address A has balance of 0 ETH, and Address B has balance of 5 ETH.
    function withdrawAllMoney(address payable _to) public {
        uint balanceToSend = balanceReceived[msg.sender];
        balanceReceived[msg.sender] = 0;
        _to.transfer(balanceToSend);
    }
}