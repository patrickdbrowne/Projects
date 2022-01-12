# What is Blockchain Product Creator?
Uses Truffle and Solidity to create a Smart Contract that allows owners to create items, set prices, people to pay, and deliver the goods. The project acts as a medium for consumers to pay for items in ETH or Wei.

# How to run the program
Follow these instructions if you want to run the smart contract using Truffle:<br></br>
    1. Download "Projects/Blockchain_Development/Projects" as a zip file and extract it.<br></br>
    2. Install MetaMask and create an account.<br></br>
    3. Install nodejs and truffle.<br></br>
    4. Open the terminal and move to the directory this application is in.<br></br>
    5. Type "truffle development" into the command prompt. Make sure this server is running in the background while using the smart contract. <br></br>
    6. Copy the first private key that appears in the terminal. <br></br>
    7. Open MetaMask, go to settings, and click "Import Account".<br></br>
    8. Paste the private key in the text box and continue. Your imported account should have 100 ETH.<br></br>
    9. Open another terminal and move to the "client" folder.<br></br>
    10. Type "npm start" and hit enter. You should be brought to a webpage.<br></br>
    11. Allow scripts to run in the URL box if prompted.<br></br>
    12. Connect the MetaMask to "Localhost 8454".<br></br>
    13. ...And now you can freely play around with the Smart Contract!<br></br>

Note: Each time you create a new item you can: set the gas fees to 0 through MetaMask; pay the gas fees through MetaMask; or make sure to pay over 21000 Wei in the node terminal if that's where you choose to pay the address.
If you want to make a payment to an item address via the Truffle console, type something like:
web3.eth.sendTransaction({to:"0xf74d50b19Ea05Fc7aBB2b24D2906680D218671E5", value:100, from:accounts[1], gas:300000});

Make sure gas is over 21000 Wei.

# Common solutions if you face a problem
If you are facing issues running the smart contract, try:<br></br>
    - going to settings and resetting account;<br></br>
    - refreshing page;<br></br>
    - changing gas fee to above 21000;<br></br>
    - terminating the console and browser, and trying again;<br></br>
    - changing the test network.
    
 # Attribution
 Please refer to Licence.md
 The Source-Code is Distributed under the License: “Attribution CC BY 4.0”. A link can be found here: 
