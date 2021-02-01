import React, {Component} from "react";
import {Container, Nav, Navbar} from "react-bootstrap";
import PropTypes from "prop-types";
import {connect} from "react-redux";
import {logout} from "../login/LoginActions";
import {withRouter} from "react-router-dom";

class AccountsManage extends Component {
    onLogout = () => {
        this.props.logout();
    };

    render() {
        const {user} = this.props.auth;
        return (
            <div>
                <Navbar bg="light">
                    <Navbar.Brand href="/">Home</Navbar.Brand>
                    <Navbar.Toggle/>
                    <Navbar.Collapse className="justify-content-end">
                        <Navbar.Text>
                            User: <b>{user.username}</b>
                        </Navbar.Text>
                        <Nav.Link onClick={this.onLogout}>Logout</Nav.Link>
                    </Navbar.Collapse>
                </Navbar>
                <Container>
                    <h1>Manage Accounts</h1>
                </Container>
            </div>
        );
    }
}

AccountsManage.propTypes = {
    logout: PropTypes.func.isRequired,
    auth: PropTypes.object.isRequired
};

const mapStateToProps = state => ({
    auth: state.auth
});

export default connect(mapStateToProps, {logout})(withRouter(AccountsManage));
