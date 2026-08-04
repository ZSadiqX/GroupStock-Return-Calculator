# GroupStock Return Calculator

Welcome to the **GroupStock Return Calculator**! This project is a Vercel-ready Web Application that helps users track their stock investments by calculating the total investment, current/sell value, profit or loss, and percentage return.

## Architecture
- **Frontend (Website)**: React (Vite)
- **Backend (API)**: Python (Flask) serverless functions in the `api/` directory.

## Features
- **Inputs**: Stock symbol, buy price, current/sell price, quantity, optional fees, and optional dividends.
- **Outputs**: Total investment, current value, profit/loss amount, percentage gain/loss, and final status (Profit/Loss/Break-even).
- **Validation**: Ensures that invalid entries (like negative prices or quantities of zero) are caught before calculations run (powered by the Python Backend).

## How to Run Locally

You will need two terminal windows open to run both the React frontend and the Python backend.

### 1. Start the Python Backend
Open a terminal in the root project folder:
```bash
pip install -r requirements.txt
python api/index.py
```
*(The API will start running at `http://127.0.0.1:5328`)*

### 2. Start the React Frontend
Open a second terminal in the root project folder:
```bash
npm install
npm run dev
```
*(Visit the provided `localhost` URL in your browser to view the app!)*

## Team Contributions
- **Vihaan**: Built the foundational calculator engine with dictionary mapping, and the input validation logic (to prevent bad data).
- **Priyan**: Created the core Python calculator logic in `feesdividends.py`, incorporating fees and dividends into the math calculation.
- **Prateek**: Conducted comprehensive QA testing (`QA_Testing.md`), outlining test cases for input validation and identifying edge cases.
- **Sadiq**: Integrated and patchwork combined all teammate's code into one unified architecture, migrating it to a Vercel-ready React + Python web application.
