import React from 'react'
import { Navbar, Container, Nav } from 'react-bootstrap'
import logo from '../assets/logo.svg'
import { LinkContainer } from 'react-router-bootstrap'

const NavbarComponent = () => {
  return (
    <div>
      <Navbar variant='dark' className='navbar' expand="lg">
        <Container>
          <Navbar.Brand href="#home">
            <img
              src={logo}
              alt="Continental Logo"
              className=""
              width={150}
            />
          </Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="ms-auto">
              <LinkContainer to="/">
                <Nav.Link href="#live-feed" activeClassName="active">Live Feed</Nav.Link>
              </LinkContainer>
              <LinkContainer to="/dashboard">
                <Nav.Link href="#dashboard" activeClassName="active">Dashboard</Nav.Link>
              </LinkContainer>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>

    </div>
  )
}

export default NavbarComponent