import React from 'react';
import './App.css';

import Navbar from './components/Navbar';

import Demo from './components/Demo';

class App extends React.Component  {
  constructor(props) {
    super(props);
    this.state={die1:'one', die2: 'two'}
    this.change=this.change.bind(this);
  }
  change(){
    let d1=Math.floor(Math.random()*10);
    let d2= Math.floor(Math.random()*10 +Math.random()*10);
    this.setState({
      die1:d1,
      die2:d2
    });
  }

  submit(){
    console.log()
  }
  render(){
    return (
      <div className="App">
        <Navbar/>
        <Demo face={this.state.die1}/>
        <Demo face={this.state.die2}/>
        <button onClick={this.change}>Change</button>

<form>
  
  <input type="enter story"/>
        <button onClick={this.sumit}>Submit</button>
</form>
      </div>
    );
  }
 
}

export default App;
