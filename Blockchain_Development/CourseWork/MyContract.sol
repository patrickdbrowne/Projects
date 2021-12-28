///pragma depicts the solidity version in the program.
///The ^ indicates that version or higher
pragma solidity ^0.8;

///contract creates a smart contract. This deploys a contract that shows a string "Hello!"
///contracts are equivalent to classes
contract MyContract {
    string public myString = "Hello!";
}
/**
Smart contracts automate transactions
It can do logical operations
State - the set of all variables in a program and their values at any point in time
Its state can change through transactions
Smart contracts are simply programs stored on a blockchain that run when predetermined
conditions are met. They typically are used to automate the execution of an agreement so
that all participants can be immediately certain of the outcome, without any intermediary's
involvement or time loss.

Smart contracts are performed on each node in the blockchain

Style of contracts:
- storage variables
- events
- modifiers
- functions
*/

/** SIMULATING BLOCKCHAIN FOR DEVELOPMENT
Use JavaScript VM to simulate a blockchain in browser's memory. The virtual machine has
5 accounts with 100 ETH in each so you don't need to wait for a real transaction each time.

Refresh the page to regain the 100ETH in each account. It does not connect to your metamask.

*/