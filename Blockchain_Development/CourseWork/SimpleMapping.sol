pragma solidity ^0.8.4;

//mappings are a type of data type:
/**
- accessed like dictionaries e.g., myMapping[_index]
- each key/value data is initialised with default values e.g. each bool is false
- each value can be changed like a dictionary
- mappings don't have a length

equivalent to (python dictionary):
{
1: "false",
2: "false",
3: "false", ...}
*/

/**
mappings are in the form mapping(key_type => value_type) public {name}
 */
contract simpleMappingExample {
    //Each int is assigned the default bool (false)
    mapping(uint => bool) public myMapping;

    //Each address is assigned false
    mapping(address => bool) public myAddressMapping;

    function setValue(uint _index) public {
        //assignes specific value to true
        myMapping[_index] = true;
    }

    //changes specific address to true. Could be used to check existence of an address
    function setMyMapToTrue() public {
        myAddressMapping[msg.sender] = true;
    }
}