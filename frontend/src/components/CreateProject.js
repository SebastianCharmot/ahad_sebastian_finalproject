import React, {Component} from 'react';
import Form from 'react-bootstrap/Form';
import Row from 'react-bootstrap/Row';
import Container from 'react-bootstrap/Container';
import Col from 'react-bootstrap/Col';
import {Button} from 'react-bootstrap'


export default class CreateProject extends Component{
    state = {
        title : "",
        sDescription : "",
        lDescription : "",
        image: "",
        funding_required: "",
        funding_recieved: "",
        completed: "",
        category: "",
        likes: "",
        comments: "",
        alumni_contribution: "",
        student: ""
        }
        // handleChange(event){
        //     this.setState({
        //         title: input

        //     })
        //     event.preventDefault();
        //     console.log(this.state.title)
        //   }

render(){
    return(
<Container>
<Row>
<Form onSubmit={this.handleChange}>
  <Form.Group controlId="exampleForm.ControlInput1">
    <Form.Label>Title</Form.Label>
    <Form.Control type="title" placeholder="title" />
  </Form.Group>

  {/* ref={(input) => this.handleChange()} */}

  <Form.Group controlId="exampleForm.ControlTextarea1">
    <Form.Label>Short Description</Form.Label>
    <Form.Control as="textarea" rows="3" />
  </Form.Group>

  <Form.Group controlId="exampleForm.ControlTextarea1">
    <Form.Label>Long Description</Form.Label>
    <Form.Control as="textarea" rows="5" />
  </Form.Group>

  <Form.Group controlId="exampleForm.ControlInput1">
    <Form.Label>Funding Required</Form.Label>
    <Form.Control type="number" placeholder="1000" />
  </Form.Group>

  <Form.Group controlId="exampleForm.ControlSelect1">
    <Form.Label>Category</Form.Label>
    <Form.Control as="select">
      <option>Science</option>
      <option>Art</option>
      <option>Entrepreneurship</option>
      <option>Social</option>
      <option>Student Organizations</option>
    </Form.Control>
  </Form.Group>

  <Button variant="primary" type="submit" on>
    Submit
  </Button>



  
  
</Form>
</Row>
</Container>
    )

}
}