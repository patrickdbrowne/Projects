pragma solidity ^0.8;

/**
Default value of any variable is always 0, False etc.. so there aren't errors
You can choose to assign a variable to a value or not.
Public can be accessed anywhere
uint is equivalent to uint256 (alias) and int is equivalent to int256
uint8 accepts 0 - 255

uint or unsigned integer has no sign (not negative) and int has a sign but stores half the positive integers (can be negative).

Structure:
- variables: {type i.e., uint, int, string, bool etc.} {public|private} {name}
- function: function {name} ({type} param1, ...) {public|private} {open brace} ... {close brace}

functions will appear as buttons etc. in the UI
The same process applies with booleans
*/


/** 
ACCESSING PUBLIC INFORMATION
Balances and some other information for each address are stored publicly on the blockchain so can be accessed through solidity. 
Currency is given in wei (smallest unit of currency). 1 ETH is 1 * 10^18=> 10**18 wei.
Other functions on addresses include:
- .transfer(...)
- .send(...)
- .call().value()
- .delegatecall()
etc.

STRINGS
In Solidity, strigns don't have as many methods as they do in other languages. You need to enter strings with quotes ("") in the UI and use
a "memory" key word before it in parameters. This is so the computer knows where to search.

OPERATIONS
similar to JavaScript (JS) in this respectt
"and" operation is "&&"
"or" operation is "||"
if (... && ...) {}
*/
contract WorkingWithVariables {
    uint public integer;
    uint8 public num;
    ///_num is given in textbox when smart contract is deployed because of parameter
    function setUint(uint _num) public {
        integer = _num;
    }

    bool public myBool;
    function setBool(bool _myBool) public {
        myBool = _myBool;
    }

    ///shown as button because no parameter and has same syntax as Javascript
    function incrementUint() public {
        num++;
    }

    function decrement() public {
        ///If num == 0 and it decrements, num will be 255 because of its range
        num--;
    }

    ///address is a type of variables used for addresses
    address public myAddress;
    function setAddress(address _myAddress) public {
        myAddress = _myAddress;
    }

    ///Finds balance in wallet
    /**
    view function reads data and can return data 
    */
    function findBalance() public view returns(uint) {
        return myAddress.balance;
    }
    
    ///Strings need a "memory" key word before it's accessed. Stored as a byte array then converted using UTF-8.
    ///Try not to work with strings if you can because it is "expensive"
    string public myString;
    function setString(string memory _myString) public {
        myString = _myString;
    }

}
