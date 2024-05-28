import { useState, useEffect } from 'react';
import axios from 'axios';

const useDocuments = (endpoint) => {
  const [docs, setDocs] = useState([]);

  useEffect(() => {
    const fetchDocuments = async () => {
      try {
        const response = await axios.get(`http://localhost:8000/api/${endpoint}`);
        setDocs(response.data);
      } catch (err) {
        console.error(err.message);
      }
    };

    fetchDocuments();

    return () => {
      setDocs([]);
    };
  }, [endpoint]);

  return { docs };
}

export default useDocuments;