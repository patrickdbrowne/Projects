The source code is from the Course "Ethereum Blockchain Developer -- Build Projects in Solidity".

Uses Truffle and Solidity to create a Smart Contract that allows owners to create items, set prices, people to pay, and deliver the goods. 

The project acts as a medium for consumers to pay for items in ETH or Wei.

Follow these instructions if you want to run the smart contract using Truffle:
    1. Download "Projects/Blockchain_Development/Projects" as a zip file and extract it.
    2. Install MetaMask and create an account.
    3. Install nodejs and truffle.
    4. Open the terminal and move to the directory this application is in.
    5. Type "truffle development" into the command prompt. Make sure this server is running in the background while using the smart contract. 
    6. Copy the first private key that appears in the terminal. 
    7. Open MetaMask, go to settings, and click "Import Account".
    8. Paste the private key in the text box and continue. Your imported account should have 100 ETH.
    9. Open another terminal and move to the "client" folder.
    10. Type "npm start" and hit enter. You should be brought to a webpage.
    11. Allow scripts to run in the URL box if prompted.
    12. Connect the MetaMask to "Localhost 8454".
    13. ...And now you can freely play around with the Smart Contract!
    Note: Each time you create a new item you can: set the gas fees to 0 through MetaMask; pay the gas fees through MetaMask;
    or make sure to pay over 21000 Wei in the node terminal if that's where you choose to pay the address.
If you want to make a payment to an item address via the Truffle console, type something like:
web3.eth.sendTransaction({to:"0xf74d50b19Ea05Fc7aBB2b24D2906680D218671E5", value:100, from:accounts[1], gas:300000});

Make sure gas is over 21000 Wei.

If you are facing issues running the smart contract, try:
    - going to settings and resetting account;
    - refreshing page;
    - changing gas fee to above 21000;
    - terminating the console and browser, and trying again;
    - changing the test network.
