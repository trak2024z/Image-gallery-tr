import React, { useState } from "react";
import ProgressBar from './components/ProgressBar';

const Home = () => {
    const token = localStorage.getItem("token");
    const userJson = localStorage.getItem("user");
    const user = userJson ? JSON.parse(userJson) : null;

    const [file, setFile] = useState(null);
    const [error, setError] = useState(null);
    const types = ['image/png', 'image/jpeg'];

    const handleChange = (e) => {
    let selected = e.target.files[0];

    if (selected && types.includes(selected.type)) {
      setFile(selected);
      setError('');
    } else {
      setFile(null);
      setError('Please select png or jpg image file');
    }
  };
    return (
        <div>
            {token && user ? (
                <form>
                <label>
                  <input type="file" onChange={handleChange} />
                  <span>+</span>
                </label>
                <div className="output">
                  { error && <div className="error">{ error }</div>}
                  { file && <div>{ file.name }</div> }
                  { file && <ProgressBar file={file} setFile={setFile} /> }
                </div>
                <a href="/logout">Logout</a>
              </form>
            ) : (
                <div>
                    <p>Nie jesteś zalogowany.</p>
                    <a href="/login">Zaloguj się</a>
                </div>
            )}
        </div>
    );
};

export default Home;