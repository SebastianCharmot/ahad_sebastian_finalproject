import React from 'react';
import './App.css';
import Form from 'react-bootstrap/Form';
import Row from 'react-bootstrap/Row';
import Container from 'react-bootstrap/Container';
import Col from 'react-bootstrap/Col';
import CreateProject from './components/CreateProject';
// import Navbar from './components/Navbar';



export default class App extends React.Component {

  render() {

  return (

    <div className="App">
      <CreateProject />
    </div>



  );
}

}
