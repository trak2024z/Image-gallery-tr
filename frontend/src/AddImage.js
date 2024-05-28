import React, { useState } from "react";

const AddImage = () => {
    const [formData, setFormData] = useState({
        imageName: "",
        image: null,
    });

    const { imageName, image } = formData;

    const onChange = (e) => {
        if (e.target.name === "image") {
            setFormData({ ...formData, [e.target.name]: e.target.files[0] });
        } else {
            setFormData({ ...formData, [e.target.name]: e.target.value });
        }
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
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
                        name="imageName"
                        required
                        onChange={onChange}
                    />

                    <label htmlFor="image">Select Image</label>
                    <input
                        type="file"
                        id="image"
                        name="image"
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