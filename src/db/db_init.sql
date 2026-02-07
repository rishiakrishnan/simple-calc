CREATE DATABASE IF NOT EXISTS calculator_db;
USE calculator_db;

CREATE TABLE IF NOT EXISTS calculations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    a FLOAT,
    b FLOAT,
    operation VARCHAR(5),
    result VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
