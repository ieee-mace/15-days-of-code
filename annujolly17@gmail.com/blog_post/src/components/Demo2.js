import React, { Component } from 'react';

class Demo2 extends Component {
    constructor(props) {
        super(props);
        this.state ={num:1,
        won:false}
        this.handleclick=this.handleclick.bind(this);
    }
    handleclick(e){
        let r= Math.floor(Math.random()*10);
        this.setState({
            num:r
        });

        if(r===7){
            this.setState({
                won:true
            });
            
        }
    }
    render() {
        return (
            <div>
                
                <h1>{this.state.num}</h1>
        <h3>{this.state.won ? 'won' : 'try again'}</h3>
        <div>{ this.state.num!==7 && <button onClick={this.handleclick}>Click</button>}</div>
            </div>
            
        );
    }
}

export default Demo2;