import React, { Component } from "react";
import ItemManagerContract from "./contracts/ItemManager.json";
import ItemContract from "./contracts/Item.json";
import getWeb3 from "./getWeb3";

import "./App.css";

class App extends Component {

  constructor(parent) {
    super(parent);
    this.aboutButton = React.createRef();
    this.howButton = React.createRef();
    this.contractButton = React.createRef();
    this.aboutContent = React.createRef();
    this.howContent = React.createRef();
    this.contractContent = React.createRef(); 
    //clears or displays pages corresponding to buttons
    this.state = {
      displayContract: "none",
      displayAbout: "none",
      displayHow: "none",
      loaded:false,
      cost:100,
      itemName:"Example_1",
      number: 0,
      paid: 0,
    }
  }

  componentDidMount = async () => {
    try {
      // Get network provider and web3 instance.
      this.web3 = await getWeb3();

      // Use web3 to get the user's accounts.
      this.accounts = await this.web3.eth.getAccounts();

      // Get the contract instance.
      this.networkId = await this.web3.eth.net.getId();

      // Stores instance of itemManager in App.js as a class variable
      this.itemManager = new this.web3.eth.Contract(
        ItemManagerContract.abi,
        ItemManagerContract.networks[this.networkId] && ItemManagerContract.networks[this.networkId].address,
      );
      
      // Stores instance of item in App.js as a class variable
      this.item = new this.web3.eth.Contract(
        ItemContract.abi,
        ItemContract.networks[this.networkId] && ItemContract.networks[this.networkId].address,
      );


      // Set web3, accounts, and contract to the state, and then proceed with an
      // example of interacting with the contract's methods.
      this.listenToPaymentEvent();
      this.setState({ loaded:true });
    } catch (error) {
      // Catch any errors for any of the above operations.
      alert(
        `Failed to load web3, accounts, or contract. Check console for details.`,
      );
      console.error(error);
    }
  };

  listenToPaymentEvent = () => {
    let self = this;
    //function listens to the SupplyChainStep event for each instance of deployed contract
    this.itemManager.events.SupplyChainStep().on("data", async function(evt){
      console.log(evt);
      if (evt.returnValues._step == 1) {
        //Create item object
        let itemObj = await self.itemManager.methods.items(evt.returnValues._itemIndex).call();
        //inform user their payment was successful
        alert("Item " + itemObj._identifier + " was paid. Deliver it now!");
        self.setState({paid: self.state.paid+1});
      }
    });
  }

  //Notation from React to handle events
  handleInputChange = (event) => {
    const target = event.target;
    const value = target.type === "checkbox" ? target.checked : target.value;
    const name = target.name;
    this.setState({
      [name]: value
    })
  }

  handleSubmit = async() => {
    const {cost, itemName} = this.state;
    //create new item on blockchain
    let result = await this.itemManager.methods.createItem(itemName, cost).send({from: this.accounts[0]});
    console.log(result);
    this.setState({number: this.state.number+1});
    //informs user of how much and where to pay for item
    alert("Please send " + cost + " Wei to " + result.events.SupplyChainStep.returnValues._itemAddress);
  }
  
  //disables buttons when clicked
  aboutPage = async() => {
    this.aboutButton.current.disabled = true;
    this.howButton.current.disabled = false;
    this.contractButton.current.disabled = false;
    this.setState({displayContract: "none"});
    this.setState({displayAbout: "block"});
    this.setState({displayHow: "none"});
  }
  howPage = async() => {
    this.aboutButton.current.disabled = false;
    this.howButton.current.disabled = true;
    this.contractButton.current.disabled = false;
    this.setState({displayContract: "none"});
    this.setState({displayAbout: "none"});
    this.setState({displayHow: "block"});
  }
  contractPage = async() => {
    this.aboutButton.current.disabled = false;
    this.howButton.current.disabled = false;
    this.contractButton.current.disabled = true;
    this.setState({displayContract: "block"});
    this.setState({displayAbout: "none"});
    this.setState({displayHow: "none"});
  }


  render() {    
    if (!this.state.loaded) {
      return <div>Loading Web3, accounts, and contract...</div>;
    }
    return (
      <div className="App">
        <button id="About" ref={this.aboutButton} class="navigate" onClick={this.aboutPage}>About Blockchain</button>
        <button id="How" ref={this.howButton} class="navigate" onClick={this.howPage}>How to use this Smart Contract</button>
        <button id="Contract" ref={this.contractButton} class="navigate" onClick={this.contractPage}>The Smart Contract</button>
        
        <div id="aboutContent" ref={this.aboutContent} style={{display:this.state.displayAbout}}>
          <br></br>
          <h1 class="headers">What is Blockchain?</h1>
          <p1>The term "Blockchain" refers to a decentralised system used to store information. The system is very secure, storing a copy of the database on each 
            node in the blockchain. This is why ledgers are a common dataset found on the blockchain. There are different networks and blockchains, with Mainnet being
            the primary public Ethereum production blockchain. This is where actual-value transactions occur.
          </p1>
          <br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br><br></br>
          <h1 class="headers">What are Smart Contracts?</h1>
          <p1>
            It follows that "Smart Contracts" are automated programs built into the blockchain to facilitate, verify, or negotiate a contract agreement. It's typically used
            to distribute assets between parties once certain conditions are met, so that each person involved in the transaction can be certain of the outcome.
          </p1>

        </div>
        <div id="howContent" ref={this.howContent} style={{display:this.state.displayHow}}>
          <br></br>
          <h1 class="headers">Requirements</h1>
          <p1>Ensure you have MetaMask To run the smart contract, you can choose to:<br></br>
            1. use the "Localhost8454" local network using truffle (refer to the README.txt for instructions);<br></br>
            2. use a test network, like the Ropsten Test Network or the Goerli Test Network. Find out how to request 
            ETH <a href="https://blog.logrocket.com/top-4-ethereum-testnets-testing-smart-contracts/">here</a>;<br></br>
            3. or use Mainnet, which is not recommended since this program is not production ready. <br></br> 
            Note: Wei is the currency used in the smart contract, which is the smallest unit of ETH. <br></br>1 ETH = 1 &#215; 10<sup>18</sup> Wei.       
          </p1>

          <br></br><br></br><br></br>
          <h1 class="headers">Instructions</h1>
          <p1>
            This smart contract lets the deployer, or the owner, create items and attach an associated price onto it. If the
            deployment was successful, you should receive an alert with the amount that needs to be paid for the item, and the 
            unique address you, or the customer, should send the money to. Once a full payment has been made, you should receive one last 
            alert informing you that your product can be dispatched for delivery!
            <br></br><br></br>
            You can create as many items as your heart desires, and there should be a record of each item in the next page as well...
          </p1>
        </div>

        <div id="contractContent" ref={this.contractContent} style={{display:this.state.displayContract}}>
          <br></br>
          <h1 id="title">Blockchain Product Creator</h1>
          <p1>Price of Product (Wei): </p1>
          <br></br><br></br><br></br>
          <input type="number" min="0" name="cost" value={this.state.cost} onChange={this.handleInputChange} />
          <br></br><br></br><br></br>
          <p1>Name of Product: </p1>
          <br></br><br></br><br></br>
          <input type="text" align="left" name="itemName" value={this.state.itemName} onChange={this.handleInputChange} />
          <br></br><br></br><br></br><br></br>
          <button type="button" id="submit" onClick={this.handleSubmit}>Create new Item</button>
          <br></br><br></br><br></br><br></br>
          <p1>Number of Products Created:{this.state.number}</p1>
          <br></br><br></br><br></br><br></br>
          <p1>Number of Products Paid for:{this.state.paid}</p1>
        </div>
       
      </div>
    );
  }
}

export default App;
