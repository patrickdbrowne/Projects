# What is Blockchain Product Creator?
Uses Truffle and Solidity to create a Smart Contract that allows owners to create items, set prices, people to pay, and deliver the goods. The project acts as a medium for consumers to pay for items in ETH or Wei.

# How to run the program
Follow these instructions if you want to run the smart contract using Truffle:<br>
1. Download "Projects/Blockchain_Development/Projects" as a zip file and extract it.<br>
2. Install MetaMask and create an account.<br>
3. Install nodejs and truffle.<br>
4. Open the command prompt and move to the directory this application is in. I.e., .\Projects<br>
5. Type "truffle develop" into the command prompt. Make sure this server is running in the background while using the smart contract. <br>
6. In the same terminal, type "migrate". This actually deploys the smart contracts on the network (localHost 8545) <br>
7. Copy the first private key that appears in the terminal. <br>
8. Open MetaMask, go to settings, and click "Import Account".<br>
9. Paste the private key in the text box and continue. Your imported account should have 100 ETH. Use this account when testing the program with Truffle.<br>
10. Open another terminal and move to the "client" folder. I.e., .\Projects\client <br>
11. Type "npm start" and hit enter. You should be brought to a webpage.<br>
12. Allow scripts to run in the URL box if prompted.<br>
13. Connect the MetaMask to "Localhost 8454".<br>
14. ...And now you can freely play around with the Smart Contract!<br></br>

<ins>Deploying the contract</ins>: Each time you create a new item and deploy the contract through MetaMask, you can:<br> 
- set the gas fees to 0 through MetaMask;<br>
- pay the gas fees through MetaMask; or<br>
- make sure to pay OVER 21000 Wei in the node terminal if that's where you choose to pay the address.<br>
This is where issues most commonly arise. Please look under the "Suggestions" heading for possible fixes.<br></br>

<ins>Paying the address</ins>: You can pay the given address through MetaMask or Truffle. If you want to pay through MetaMask, simply copy and paste the given address and pay in full amount. If you want to make a payment to an item address via the Truffle console, type:<br>
web3.eth.sendTransaction({to:"*address*", value:*amount in wei*, from:*account*, gas:*amount in wei over 21000*});<br>
For example, <br>
web3.eth.sendTransaction({to:"0xf74d50b19Ea05Fc7aBB2b24D2906680D218671E5", value:100, from:accounts[1], gas:300000}); <br></br>

Read more about using Truffle here: https://trufflesuite.com/docs/truffle/quickstart.html#truffle-quickstart

# Some suggestions if you face a problem
The most common errors arise when deploying the contracts, especially if the contract is on the wrong network or hasn't been deployed at all. Please make sure you have done the following:<br>
- installed all the necessary packages. The versions shouldn't affect it, but I am using npm version 8.1.2 and truffle 5.4.26.
- go to settings, click "Advanced" and then "reset account". This should restart the nonce (number of transactions so far);<br>
- close the webpage, and kill both terminals;
- open the command prompt and move to the ".\Projects" directory;<br>
- type "truffle develop"; <br>
- once the screen has loaded, showing you a list of ten private test keys, type "migrate --reset". This should resolve the issue of the contracts not being deployed by deploying them on the blockchain;<br>
- open another terminal and move to the ".\Projects\client" directory;<br>
- type "npm start";<br>
- make sure MetaMask is connected to "Localhost 8545";<br>
- ensure both terminals are running in the background when running the program;<br>
- You shouldn't need to change the gas fee when prompted, but pay over the required amount if asked.<br></br>

Other things you could try include: <br>
- refreshing page;<br>
- changing gas fee to above 21000;<br>
- terminating the console and browser, and trying again;<br>
- closing the browser and signing into MetaMask again;<br>
- changing the test network if you configure the contract to deploy on that network too via truffle_config.js. This requires more work and you will need to request ETH with a faucet on the same account.<br></br>

You should know if the program works if it alerts you with an address and amount that needs to be paid at that address when you click "Create new Item" with the example given. Once the money is paid at the address, you should receive another alert that delivery is ready for that specific item. Object instances should be printed on the console when they go through a new stage.
    
 # Attribution
 Please refer to LICENCE.md<br>
 The source code can be found https://www.udemy.com/course/blockchain-developer/ under Section 7.<br>
 The Source-Code is Distributed under the License: “Attribution CC BY 4.0”.
