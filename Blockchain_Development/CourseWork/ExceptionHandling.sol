pragma solidity 0.6.12;

//This version demonstrates issue with integer roll over
contract ExceptionExample {

    mapping(address => uint64) public balanceReceived;

    function receiveMoney() public payable {
        assert(msg.value == uint64(msg.value));
        balanceReceived[msg.sender] += uint64(msg.value);
        assert(balanceReceived[msg.sender] >= uint64(msg.value));
    }

    function withdrawMoney(address payable _to, uint64 _amount) public {
        require(_amount <= balanceReceived[msg.sender], "Not Enough Funds, aborting");
        //assert statements must be true, otherwise they will throw an exception to 
        //assert is used for internal problem in contract, and require is for returned values.
        assert(balanceReceived[msg.sender] >= balanceReceived[msg.sender] - _amount);
        balanceReceived[msg.sender] -= _amount;
        _to.transfer(_amount);
    }
}
/**
When an exception happens, transaction, and excecuted code before that execution would be reverted.
Solidity does not allow reactions to exceptions.

ASSERT
Asserts should not be used often, only for when something unexpected happens internally like missing funds. 
Asserts consume all gas and terminate the program. Does not allow user to continue?

REQUIRE
Requires validates user inputs and returns gas. Allows user to try again.

check video 43 to see typical uses of these keywords

REVERT
the "revert" keyword is equivalent to require(false), by throwing an error and reverting everything.
*/