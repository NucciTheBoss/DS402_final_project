import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import "./App.css";
import Header from "./components/Header";
import LandingPage from "./content/LandingPage";
import AlgoOne from "./components/AlgoOne";

function App() {
  return (
    <div className="App">
      <Header />
      <Router>
        <Switch>
          <Route exact path="/" component={LandingPage}></Route>
          <Route path="algoOne" component={AlgoOne}></Route>
        </Switch>
      </Router>
    </div>
  );
}

export default App;
