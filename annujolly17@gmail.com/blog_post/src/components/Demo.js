import React, { Component } from 'react';

class Demo extends Component {
  constructor(props) {
    super(props);
    
  }
  
  render() {
    return (
      <div>
        {this.props.face}
      </div>
    );
  }
}

export default Demo;