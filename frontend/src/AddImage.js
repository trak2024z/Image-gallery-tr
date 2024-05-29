import React, { useState } from "react";
import axios from './api/axios';
const AddImage = () => {
    const [formData, setFormData] = useState({
        name: "",
        path: null,
    });

    const { imageName, image } = formData;

    const onChange = (e) => {
        if (e.target.name === "path") {
            setFormData({ ...formData, [e.target.name]: e.target.files[0] });
        } else {
            setFormData({ ...formData, [e.target.name]: e.target.value });
        }
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
          const response = await axios.post(`http://localhost:8000/galleries/1/picture/`, formData, {
            headers: {
              'Authorization': `Token ${localStorage.getItem('token')}`,
              'Content-Type': 'multipart/form-data'
            }
          });
          console.log('Image uploaded successfully:', response.data);
        } catch (error) {
          console.error('Error uploading image:', error);
        }
    };

    return (
        <div>
            <nav className="navbar">
                <div className="navbar-brand">IMAGEGALLERY</div>
            </nav>
            <section>
                <form onSubmit={handleSubmit}>
                    <label htmlFor="imageName">Image Name</label>
                    <input
                        type="text"
                        id="imageName"
                        autoComplete="off"
                        value={imageName}
                        name="name"
                        required
                        onChange={onChange}
                    />

                    <label htmlFor="image">Select Image</label>
                    <input
                        type="file"
                        id="image"
                        name="path"
                        accept="image/*"
                        required
                        onChange={onChange}
                    />

                    <button type="submit">Add Image</button>
                </form>
            </section>
        </div>
    );
};

export default AddImage;