"use client"; // Dodaj to na początku pliku

import React from 'react';
import { motion } from 'framer-motion';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faTrash } from '@fortawesome/free-solid-svg-icons';

const Modal = ({ setSelectedImg, selectedImg, onDelete }) => {
  const handleClick = (e) => {
    if (e.target.classList.contains('backdrop')) {
      setSelectedImg(null);
    }
  };

  const handleDelete = () => {
    onDelete(selectedImg);
    setSelectedImg(null);
  };

  return (
    <motion.div className="backdrop" onClick={handleClick}
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
    >
      <motion.div className="modal-content"
        initial={{ y: "-100vh" }}
        animate={{ y: 0 }}
      >
        <img src={selectedImg} alt="enlarged pic" />
        <button className="button" onClick={handleDelete}>
                  <FontAwesomeIcon icon={faTrash} />
              </button>
      </motion.div>
    </motion.div>
  );
}

export default Modal;
