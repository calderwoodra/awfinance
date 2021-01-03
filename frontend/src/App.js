import React, {Component} from "react";
import Root from "./Root";
import {Route, Switch} from "react-router-dom";
import {ToastContainer} from "react-toastify";
import Home from "./components/Home";
import Signup from "./components/signup/Signup";
import Login from "./components/login/Login";
import Dashboard from "./components/dashboard/Dashboard";
import AccountsHome from "./components/accounts/AccountsHome";
import AccountsManage from "./components/accounts/manage/AccountsManage";
import AccountsConnect from "./components/accounts/connect/AccountsConnect";

import requireAuth from "./utils/RequireAuth";

import axios from "axios";

if (window.location.origin === "http://localhost:3000") {
    axios.defaults.baseURL = "http://127.0.0.1:8000";
} else {
    axios.defaults.baseURL = window.location.origin;
}

class App extends Component {
    render() {
        return (
            <div>
                <Root>
                    <ToastContainer hideProgressBar={true} newestOnTop={true}/>
                    <Switch>
                        <Route path="/signup$" component={Signup}/>
                        <Route path="/login$" component={Login}/>
                        <Route path="/dashboard$"
                               component={requireAuth(Dashboard)}/>
                        <Route path="/accounts/view"
                               component={requireAuth(AccountsHome)}/>
                        <Route path="/accounts/manage"
                               component={requireAuth(AccountsManage)}/>
                        <Route path="/accounts/connect"
                               component={requireAuth(AccountsConnect)}/>
                        <Route exact path="/" component={Home}/>
                    </Switch>
                </Root>
            </div>
        );
    }
}

export default App;
