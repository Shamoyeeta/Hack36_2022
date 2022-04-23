import logo from './logo.svg';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import './App.css';

import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

import Login from './Component/Login'
import SignUp from './Component/SignUp'
import Home from './Component/Home'


function App() {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/login">Login</Link>
            </li>
            <li>
              <Link to="/signUp">SignUp</Link>
            </li>
          </ul>
        </nav>

        {/* A <Switch> looks through its children <Route>s and
          renders the first one that matches the current URL. */}


        <Route path="/login" component={Login} />
        <Route path="/signUp" component={SignUp} />
        <Route path="/" component={Home} />

      </div>
    </Router>
  );
}

export default App;
