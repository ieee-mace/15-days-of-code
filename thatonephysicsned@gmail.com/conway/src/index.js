import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

class Grid extends React.Component{
  render(){
    return(
      <div>
      GRID 
      </div>
    );
  }
}

class Main extends React.Component{

  constructor() {
    super();
    this.state = {
      generation: 0,
    }
  }

  render(){
    return(
      <div>
        <h1>Conway</h1>
        <h2>The Game of Life</h2>
        <Grid
        />
        <h3>Generations: {this.state.generation}</h3>
      </div>
    );
  }

}

ReactDOM.render(
  <Main />,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
