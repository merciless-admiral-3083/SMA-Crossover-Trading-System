-- SQL script to create table for storing stock data

CREATE DATABASE IF NOT EXISTS sma_trading;
USE sma_trading;

CREATE TABLE IF NOT EXISTS stock_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    datetime DATETIME,
    open DOUBLE,
    high DOUBLE,
    low DOUBLE,
    close DOUBLE,
    volume BIGINT
);
