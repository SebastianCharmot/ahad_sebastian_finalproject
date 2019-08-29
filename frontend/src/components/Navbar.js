import React from 'react';
import {Link} from 'react-router-dom';

export default function Navbar() {

    return (
        <nav className="Navbar">
          <Link to="/">Home</Link>
          <Link to="/Deposit">Deposit</Link>
          <Link to="/sell">Sell</Link>
          <button onClick={(event) => {
            props.logout()
          }}> Logout </button>
  
  
        </nav>
    )
        }
