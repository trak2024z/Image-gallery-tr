import Home from './Home';
import Register from './Register';
import Login from './Login';
import Logout from './Logout';
import Title from './components/Title';
import ImageGrid from './components/ImageGrid';
import Modal from './components/Modal';
import React, { useState } from 'react';
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";


function App() {
  const [selectedImg, setSelectedImg] = useState(null);
  return (
    <main className="App">
      <Title/>
      <ImageGrid setSelectedImg={setSelectedImg} />
      { selectedImg && (
        <Modal selectedImg={selectedImg} setSelectedImg={setSelectedImg} />
      )}
      <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/register" element={<Register/>}/>
        <Route path="/login" element={<Login/>}/>
        <Route path="/logout" element={<Logout/>}/>
      </Routes>
      </BrowserRouter>
    </main>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
export default App;