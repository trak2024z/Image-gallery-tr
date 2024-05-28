import { useState, useEffect } from 'react';
import axios from 'axios';

const useUpload = (file) => {
  const [progress, setProgress] = useState(0);
  const [error, setError] = useState(null);
  const [url, setUrl] = useState(null);

  useEffect(() => {
    const uploadFile = async () => {
      const formData = new FormData();
      formData.append('file', file);

      try {
        const response = await axios.post('http://localhost:8000/api/images/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          },
          onUploadProgress: (progressEvent) => {
            const percentCompleted = Math.round((progressEvent.loaded * 100) / progressEvent.total);
            setProgress(percentCompleted);
          }
        });
        setUrl(response.data.file);
      } catch (err) {
        setError(err);
      }
    };

    uploadFile();
  }, [file]);

  return { progress, url, error };
};

export default useUpload;