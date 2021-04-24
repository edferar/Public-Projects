import React from 'react'
import { Navbar } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';



const NavBar = ({String}) =>{
return(
  <Navbar bg="dark" variant="dark">
    <Navbar.Brand href="#home">
      <img
        alt=""
        src="/logo512.png"
        width="30"
        height="30"
        className="d-inline-block align-top"
      />{' '}
      {String}
    </Navbar.Brand>
  </Navbar>


)}

export default NavBar;