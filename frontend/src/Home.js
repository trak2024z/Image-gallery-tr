"use client";

import React, { useState, useEffect } from "react";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUser, faPlus } from '@fortawesome/free-solid-svg-icons';
import axios from './api/axios';
import Modal from './Modal';

const Home = () => {
    const token = localStorage.getItem("token");
    const userJson = localStorage.getItem("user");
    const user = userJson ? JSON.parse(userJson) : null;
    const [images, setImages] = useState([]);
    const [selectedImg, setSelectedImg] = useState(null);

    useEffect(() => {
        const getImages = async () => {
            try {
                const response = await axios.get(`http://localhost:8000/galleries/1/pictures`);
                setImages(response.data.images);
            } catch (error) {
                console.error('Error fetching images:', error);
            }
        };
        getImages();
    }, []);

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
                <div className="image-grid">
                    {images.map(image => (
                        <div className="image-item" key={image.id} onClick={() => setSelectedImg(image)}>
                            <img src={`http://localhost:8000${image.path}`} alt={image.name} />
                        </div>
                    ))}
                </div>
            </div>
            {selectedImg && <Modal selectedImg={selectedImg} setSelectedImg={setSelectedImg} />}
        </div>
    );
};

export default Home;