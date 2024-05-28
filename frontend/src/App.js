import Home from './Home';
import Register from './Register';
import Login from './Login';
import Logout from './Logout';
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import AddImage from './AddImage';


function App() {
  return (
    <main className="App">
      <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/register" element={<Register/>}/>
        <Route path="/login" element={<Login/>}/>
        <Route path="/logout" element={<Logout/>}/>
        <Route path="/add-image" element={<AddImage/>}/>
      </Routes>
      </BrowserRouter>
    </main>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
export default App;