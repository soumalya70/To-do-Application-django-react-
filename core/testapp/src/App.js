import logo from './logo.svg';
import './App.css';
import axios from "axios";
import {useEffect} from 'react'

function App() {
  useEffect(() => {
    const obj = axios.get("http://localhost:8000/tasks") ;
    obj.then(response => {
      console.log(response.data); // This will log the data returned by the server
  }).catch(error => {
      console.error('Error:', error); // Handle any errors that occur during the request
  });
  
  })
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
