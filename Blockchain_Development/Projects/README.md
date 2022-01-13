# What is Blockchain Product Creator?
Uses Truffle and Solidity to create a Smart Contract that allows owners to create items, set prices, people to pay, and deliver the goods. The project acts as a medium for consumers to pay for items in ETH or Wei.

# How to run the program
Follow these instructions if you want to run the smart contract using Truffle:<br>
1. Download "Projects/Blockchain_Development/Projects" as a zip file and extract it.<br>
2. Install MetaMask and create an account.<br>
3. Install nodejs and truffle.<br>
4. Open the command prompt and move to the directory this application is in. I.e., .\Projects<br>
5. Type "truffle development" into the command prompt. Make sure this server is running in the background while using the smart contract. <br>
6. Copy the first private key that appears in the terminal. <br>
7. Open MetaMask, go to settings, and click "Import Account".<br>
8. Paste the private key in the text box and continue. Your imported account should have 100 ETH. Use this account when testing the program with Truffle.<br>
9. Open another terminal and move to the "client" folder. I.e., .\Projects\client <br>
10. Type "npm start" and hit enter. You should be brought to a webpage.<br>
11. Allow scripts to run in the URL box if prompted.<br>
12. Connect the MetaMask to "Localhost 8454".<br>
13. ...And now you can freely play around with the Smart Contract!<br></br>

<ins>Deploying the contract</ins>: Each time you create a new item and deploy the contract through MetaMask, you can:<br> 
- set the gas fees to 0 through MetaMask;<br>
- pay the gas fees through MetaMask; or<br>
- make sure to pay OVER 21000 Wei in the node terminal if that's where you choose to pay the address.<br>
This is where issues most commonly arise. Please look under the "Suggestions" heading for possible fixes.<br></br>

<ins>Paying the address</ins>: You can pay the given address through MetaMask or Truffle. If you want to pay through MetaMask, simply copy and paste the given address and pay in full amount. If you want to make a payment to an item address via the Truffle console, type:<br>
web3.eth.sendTransaction({to:"*address*", value:*amount in wei*, from:*account*, gas:*amount in wei over 21000*});<br>
For example, <br>
web3.eth.sendTransaction({to:"0xf74d50b19Ea05Fc7aBB2b24D2906680D218671E5", value:100, from:accounts[1], gas:300000}); <br></br>

# Some suggestions if you face a problem
If you are facing issues running the smart contract, try:<br>
    - going to settings and resetting account;<br>
    - refreshing page;<br>
    - changing gas fee to above 21000;<br>
    - terminating the console and browser, and trying again;<br>
    - changing the test network. You will need to request ETH with a faucet on the same account.
    
 # Attribution
 Please refer to LICENCE.md
 The Source-Code is Distributed under the License: “Attribution CC BY 4.0”.
