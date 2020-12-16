import "./sass/main.scss";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
function App() {
  console.log(process.env.REACT_APP_TEST);
  console.log(process.env.NODE_ENV);
  console.log("removed alert, added console.log");
  return (
    <Router>
      <Switch>
        <Route path={"/"}>
          <h1>Home Page</h1>
        </Route>
      </Switch>
    </Router>
  );
}

export default App;
