
# Employee Record System

A Python-based application for processing employee records from a CSV file and storing them in MySQL.

## Features
- Reads employee data from a CSV file
- Sends records to a FastAPI server
- Stores data in MySQL
- Implements error handling and retries


### Clone the Repository

git clone https://github.com/Birakisor/Employee-Record-System.git

## go to folder
cd Employee-Record-System

## Installation and Steps

## vertual env
python -m venv venv
venv\Scripts\activate

## Installed required 
pip install -r requirements.txt

## Create DB
CREATE DATABASE employee_db;

CREATE USER 'user'@'localhost' IDENTIFIED BY 'gorilla';
GRANT ALL PRIVILEGES ON employee_db.* TO 'user'@'localhost';
FLUSH PRIVILEGES;

## Intial Db with Python code

python database_setup.py

## Run server
uvicorn server_api:app --reload


