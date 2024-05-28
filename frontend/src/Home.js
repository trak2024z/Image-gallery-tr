import React from "react";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUser, faPlus } from '@fortawesome/free-solid-svg-icons';
const Home = () => {

    const token = localStorage.getItem("token");
    const userJson = localStorage.getItem("user");
    const user = userJson ? JSON.parse(userJson) : null;
    return (
        <div>
          <nav className="navbar">
                <div className="navbar-brand">IMAGEGALLERY</div>
                <div className="navbar-buttons">
                    {token && user ? (
                      <React.Fragment>
                        <button className="button">
                        <a href="/add-image" className="button">
                        <FontAwesomeIcon icon={faPlus} />
                        </a>
                        </button>
                      <div className="dropdown">
                          <button className="button">
                          <FontAwesomeIcon icon={faUser} />
                          </button>
                          <div className="dropdown-content">
                              <a href="/user-details">User Details</a>
                              <a href="/logout">Logout</a>
                          </div>
                      </div>
                  </React.Fragment>
                    ) : (
                        <button className="button">
                        <a href="/login" className="button">Login</a>
                        </button>
                    )}
                </div>
            </nav>
            <div className="main-content">
            {token && user ? (
                <div>
                    <div className="photo-grid">
                            <div className="photo-column">
                                <img src="https://i.imgur.com/CzXTtJV.jpg"/>
                                <img src="https://i.imgur.com/OB0y6MR.jpg"/>
                            </div>
                            <div className="photo-column">
                                <img src="https://farm4.staticflickr.com/3075/3168662394_7d7103de7d_z_d.jpg"/>
                                <img src="https://farm9.staticflickr.com/8505/8441256181_4e98d8bff5_z_d.jpg"/>
                            </div>
                            <div className="photo-column">
                                <img src="https://farm9.staticflickr.com/8295/8007075227_dc958c1fe6_z_d.jpg"/>
                                <img src="https://farm4.staticflickr.com/3224/3081748027_0ee3d59fea_z_d.jpg"/>
                            </div>
                        </div>
                    {/* <a href="/logout">Logout</a> */}
                </div>
            ) : (
                <div>
                    <p>You are not logged in.</p>
                </div>
            )}
        </div>
      </div>
    );
};

export default Home;