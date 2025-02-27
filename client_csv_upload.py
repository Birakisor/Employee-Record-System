import aiohttp
import asyncio
import pandas as pd
import logging

# API URL
API_URL = "http://127.0.0.1:8000/employees/"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Read CSV File
def read_csv(file_path):
    return pd.read_csv(file_path)

# Async function to send employee data
async def send_employee(session, employee):
    try:
        async with session.post(API_URL, json=employee) as response:
            res = await response.json()
            logging.info(f"Response: {res}")
    except Exception as e:
        logging.error(f"Error sending data: {e}")

# Main async function
async def main(file_path):
    employees = read_csv(file_path).to_dict(orient="records")
    async with aiohttp.ClientSession() as session:
        tasks = [send_employee(session, emp) for emp in employees]
        await asyncio.gather(*tasks)

# Run the client
if __name__ == "__main__":
    file_path = "employees.csv"
    asyncio.run(main(file_path))
