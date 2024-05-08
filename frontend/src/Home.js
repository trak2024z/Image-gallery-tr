import React from "react";
const Home = () => {

    const token = localStorage.getItem("token");
    const userJson = localStorage.getItem("user");
    const user = userJson ? JSON.parse(userJson) : null;
    return (
        <div>
            <h1>Home</h1>
            {token && user ? (
                <div>
                    <h1>Welcome, {user.username}</h1>
                    <a href="/logout">Logout</a>
                </div>
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