import React from 'react';
// import logo from './logo.svg';
// import './App.css';
import styled from 'styled-components'

import ProductsList from 'Components/Products/ProductsList'


// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

const RootDiv = styled.div`
  max-width: 600px;
  margin: 0 auto;
`

const App = () => <RootDiv><ProductsList /></RootDiv>

export default App;
