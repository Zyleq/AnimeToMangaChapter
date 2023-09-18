import React, { useState } from 'react';
import axios from 'axios';

function App() {
    const [animeName, setAnimeName] = useState('naruto-shippuden');  // default value
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(false);

    const fetchData = async () => {
        setLoading(true);
        try {
            const response = await axios.get(`http://localhost:5000/fetch-data/${animeName}`);
            console.log(response.data);

            setData(response.data);
        } catch (error) {
            console.error("Error fetching data:", error);
            setData([{ "error": "Failed to fetch data." }]);
        }
        setLoading(false);
    }

    return (
        <div className="App">
            <h1>Anime to Manga Conversion</h1>

            {/* Input for anime name */}
            <input 
                type="text"
                value={animeName}
                onChange={(e) => setAnimeName(e.target.value)}
            />
            <button onClick={fetchData}>Fetch Data</button>

            {/* Display fetched data */}
            {loading ? (
                <p>Loading...</p>
            ) : (
                <ul>
                    {data.map((item, index) => (
                        <li key={index}>
                            {item[0]} - {item[1]} - {item[2]}
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
}

export default App;
