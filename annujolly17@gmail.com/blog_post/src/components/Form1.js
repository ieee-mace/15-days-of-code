import React, { Component } from "react";

class Form extends Component {
  constructor(props) {
    super(props);
    this.state = { name: "", age: 0, email: "" };
  }
  handleClick = (e) => {
    e.preventDefault();
    this.setState({ [e.target.name]: e.target.value });
  };
  submit = (y) => {
    y.preventDefault();
  };
  render() {
    return (
      <div>
        <form action="" onSubmit={this.submit}>
          Name{" "}
          <input type="text" name="name" id="" onChange={this.handleClick} />
          Age <input type="text" name="age" id="" onChange={this.handleClick} />
          Email
          <input type="text" name="email" id="" onChange={this.handleClick} />
        </form>
        <button className="btn btn-dark" onSubmit={this.submit}>
          Submit
        </button>
        <br />
        Name : {this.state.name}
        Age: {this.state.age}
      </div>
    );
  }
}

export default Form ;
