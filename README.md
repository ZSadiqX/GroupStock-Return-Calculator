```markdown
# GroupStock Return Calculator

Live Demo: https://group-stock-return-calculator.vercel.app/

GroupStock Return Calculator is a full-stack web application developed as a collaborative group project for the ThinkSabio Internship 2026 Minor Projects Program (Technology Track, Project 5). The application allows users to enter the details of a stock investment and receive a transparent, step-by-step breakdown of their total investment cost, current portfolio value, net profit or loss in dollar terms, and the overall percentage return on their investment. Optional inputs for brokerage fees and dividends received are also supported, making the calculator more realistic and applicable to real-world scenarios.

The project began as a Python command-line tool and was subsequently migrated into a production-ready web application deployed on Vercel, combining a React frontend with a Python Flask backend running as serverless functions.

---

## Table of Contents

- [Live Demo](#live-demo)
- [Project Background](#project-background)
- [Architecture Overview](#architecture-overview)
- [Features](#features)
- [Formulas and Calculations](#formulas-and-calculations)
- [Input Validation Rules](#input-validation-rules)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [How to Run Locally](#how-to-run-locally)
- [Deployment on Vercel](#deployment-on-vercel)
- [QA Testing](#qa-testing)
- [Team Contributions](#team-contributions)
- [Common Mistakes This Tool Prevents](#common-mistakes-this-tool-prevents)

---

## Live Demo

The application is deployed and publicly accessible at:

https://group-stock-return-calculator.vercel.app/

No installation or setup is required to use the live version. Simply open the URL in any modern web browser, enter your stock investment details, and click Calculate Return.

---

## Project Background

This project was assigned as part of the ThinkSabio Internship 2026, a program designed to give students practical exposure to real-world software development and financial literacy concepts. The task required students to build a stock return calculator that clearly demonstrates the financial outcome of a stock investment, including edge cases such as fees, dividends, losses, and break-even scenarios.

The project specification required the following:

- Accept inputs for stock symbol, buy price, current or sell price, quantity of shares, and optional brokerage fees.
- Calculate and display total investment, current value, profit or loss, and percentage return.
- Validate all user inputs and display clear error messages for invalid data.
- Test against at least five scenarios: a profit case, a loss case, a break-even case, a decimal price case, and a fee case.
- Include a README explaining how to use the tool.

The team decided to go beyond the minimum requirements by building a full web application with a Python-powered backend and a React-based frontend, and deploying it live on Vercel so that anyone can access it without needing to install Python or any dependencies.

---

## Architecture Overview

The application is structured as a two-layer full-stack web application.

### Frontend

The frontend is built with React using the Vite build tool. It is responsible for rendering the user interface, managing form state, sending user input to the backend API, and displaying the returned results. The frontend is a single-page application and does not perform any calculations itself. All mathematical logic is delegated to the Python backend to ensure consistency with the team's original Python code.

### Backend

The backend is a Python Flask application located in the `api/` directory. Vercel automatically detects Python files in this directory and deploys them as serverless functions using the `@vercel/python` runtime. The backend exposes a single endpoint at `/api/calculate` that accepts a JSON POST request, validates the inputs, performs all four required calculations, and returns the results as a JSON response.

This architecture ensures that the core calculation logic written by the team in Python is preserved exactly as originally designed, and is simply exposed over HTTP rather than through a terminal prompt.

### Communication

When a user fills in the form on the website and clicks Calculate Return, the React frontend sends a POST request to `/api/calculate` with the input values formatted as JSON. The Python backend processes the request and returns a JSON object containing the four calculated output values. The React frontend then displays these values to the user in a formatted results card.

During local development, Vite's built-in proxy feature is configured to forward all `/api` requests from the frontend development server (running on port 5173) to the Flask backend server (running on port 5328). On Vercel, this routing is handled automatically by the platform.

---

## Features

- Stock symbol input for labeling and identifying the investment being calculated.
- Buy price input representing the price per share at the time of purchase.
- Current or sell price input representing the price per share at the time of evaluation or sale.
- Quantity input representing the total number of shares purchased.
- Optional brokerage fees input that is subtracted from the profit to reflect real-world trading costs.
- Optional dividends received input that is added to the profit to reflect income earned from holding the stock.
- Transparent output of all four intermediate and final values: total investment, current value, net profit or loss, and percentage return.
- A final status label that clearly identifies the outcome as a profit, a loss, or a break-even result.
- Server-side input validation that rejects negative prices, zero or negative quantities, and other invalid inputs before any calculation is attempted.
- Clear and descriptive error messages returned to the user when invalid inputs are detected.
- A results display that shows profit values with a positive sign and loss values with a negative sign for immediate clarity.

---

## Formulas and Calculations

The calculator implements four core financial formulas. These formulas are executed in Python on the backend and are identical to those defined in the original project specification.

### Total Investment

This represents the total amount of money spent to purchase the shares.

```
Total Investment = Buy Price x Quantity
```

### Current Value

This represents what the investment is currently worth at the evaluated price.

```
Current Value = Current Price x Quantity
```

### Net Profit or Loss

This represents the net financial outcome of the investment after accounting for fees paid and dividends received.

```
Net Profit/Loss = Current Value - Total Investment - Fees + Dividends
```

### Percentage Return

This represents the overall return on the investment expressed as a percentage of the original amount invested. This is the standard metric used to compare investment performance.

```
Percentage Return = (Net Profit/Loss / Total Investment) x 100
```

All output values are rounded to two decimal places for clarity and consistency.

---

## Input Validation Rules

All validation is performed on the Python backend before any calculation is executed. The following rules are enforced:

- Buy price must be greater than zero. A buy price of zero would result in a division by zero error when calculating the percentage return.
- Current price must be zero or greater. A current price of zero is valid and represents a total loss of investment value.
- Quantity must be a whole number greater than zero. Fractional shares are not supported.
- Brokerage fees must be zero or greater. Negative fees are not a valid input.
- Dividends must be zero or greater. Negative dividends are not a valid input.

If any of these rules are violated, the backend returns a 400 Bad Request response with a descriptive error message, and the frontend displays that message to the user in a clearly styled error box.

---

## Project Structure

```
GroupStock-Return-Calculator/
|
|-- api/
|   |-- index.py              Python Flask API backend. Contains validation
|                             logic and all four calculator formulas.
|                             Deployed by Vercel as a serverless function.
|
|-- src/
|   |-- App.jsx               Main React component. Renders the input form,
|   |                         sends data to the API, and displays results.
|   |-- index.css             Global stylesheet for the application.
|   |-- assets/
|       |-- background.jpg    Background image designed by Pranand Potturi.
|
|-- feesdividends.py          Priyan's original standalone Python calculator
|                             with fees and dividends support.
|
|-- vihaan.py                 Vihaan's original standalone Python calculator
|                             with validation and terminal interface.
|
|-- main.py                   Combined Python CLI version merging all
|                             teammates' contributions into one terminal app.
|
|-- QA_Testing.md             Prateek's full QA test suite with 24 test cases.
|
|-- requirements.txt          Python package dependencies for the backend.
|                             Used by both local setup and Vercel deployment.
|
|-- vercel.json               Vercel deployment configuration. Defines how to
|                             build the React frontend and route API requests
|                             to the Python serverless function.
|
|-- vite.config.js            Vite configuration. Sets up the local API proxy
|                             so the frontend can reach the Python backend
|                             during development.
|
|-- package.json              Node.js project configuration and dependencies.
|-- index.html                HTML entry point for the React application.
|-- README.md                 This file.
```

---

## Prerequisites

To run this project locally, you will need the following installed on your machine:

- Python 3.8 or higher
- pip (Python package manager, included with Python)
- Node.js 18 or higher
- npm (Node package manager, included with Node.js)

You can verify your installations by running the following commands in your terminal:

```bash
python --version
node --version
npm --version
```

---

## How to Run Locally

Running the project locally requires two terminal windows to be open at the same time, since the Python backend and the React frontend are separate processes.

### Step 1: Clone the Repository

If you have not already done so, clone the repository to your local machine and navigate into the project folder.

```bash
git clone https://github.com/ZSadiqX/GroupStock-Return-Calculator.git
cd GroupStock-Return-Calculator
```

### Step 2: Start the Python Backend

Open your first terminal window and navigate to the project root. Install the required Python packages and start the Flask development server.

```bash
pip install -r requirements.txt
python api/index.py
```

The backend API will start and listen for requests at `http://127.0.0.1:5328`. Keep this terminal open. If you close it, the calculations will stop working.

### Step 3: Start the React Frontend

Open a second terminal window and navigate to the same project root. Install the Node.js dependencies and start the Vite development server.

```bash
npm install
npm run dev
```

Vite will start the frontend and display a local URL, typically `http://localhost:5173`. Open that URL in your browser to use the application. The Vite proxy will automatically forward all API requests from the browser to your running Python backend.

---

## Deployment on Vercel

The project is configured to deploy automatically to Vercel. The `vercel.json` file at the root of the project defines the build and routing configuration.

When Vercel runs a deployment, it performs two build steps simultaneously. First, it uses the `@vercel/static-build` runtime to run `npm run build`, which compiles the React application into a static `dist` directory. Second, it uses the `@vercel/python` runtime to package the `api/index.py` Flask application as a serverless function.

All incoming HTTP requests to paths beginning with `/api/` are routed to the Python serverless function. All other requests are served from the compiled React static files.

To deploy your own instance, connect your fork of this repository to a Vercel account and import the project. Vercel will detect the configuration automatically and deploy without any additional setup required.

---

## QA Testing

A comprehensive quality assurance test suite is documented in `QA_Testing.md`. The suite contains 24 individual test cases designed and executed by Prateek, covering the following categories:

- Negative values for buy price, sell price, and quantity.
- Zero values for all numeric inputs.
- Empty inputs submitted without any value entered.
- Decimal price inputs to verify floating-point handling.
- Integer-only quantity enforcement.
- Alphabetic and special character inputs to test non-numeric rejection.
- Inputs with leading or trailing whitespace.
- Extremely large numeric inputs to verify the absence of crashes.
- Extremely small decimal inputs.
- Malformed numbers such as multiple decimal points and scientific notation.
- Numbers formatted with commas.
- A valid control test to confirm correct output under normal conditions.

All 24 test cases document the input used, the expected output, the actual output observed, and a pass or fail status. One identified failure is that comma-formatted numbers such as `1,000` are not accepted by the current validation, which is noted as a known limitation.

---

## Team Contributions

### Vihaan Doradla

Vihaan was responsible for building the foundational Python calculator engine. His contribution, preserved in `vihaan.py`, introduced a structured approach to the project by separating the code into three distinct functions: an input validation function that checks for invalid data before any math is performed, a core calculation engine that packages all four formula results into a Python dictionary, and a terminal user interface function that handles input prompts and output formatting. His use of a dictionary to store and return results became the standard data format adopted by the rest of the project.

### Priyan

Priyan built the fees and dividends version of the calculator, preserved in `feesdividends.py`. His contribution extended the core calculation engine to accept brokerage fees and dividends as optional parameters and incorporated them into the profit and loss formula. He also implemented Python exception handling around the input prompts to prevent the application from crashing on invalid type input, and added the break-even status check to the output display.

### Prateek

Prateek was responsible for quality assurance testing, documented in `QA_Testing.md`. He designed and executed 24 test cases systematically covering valid inputs, invalid inputs, boundary conditions, and edge cases. His testing identified one known failure in the current implementation (comma-formatted numbers) and provided specific suggestions for improving consistency in error messages for quantity validation. His work ensures that the calculator has been thoroughly verified before submission.

### Pranand Potturi

Pranand was responsible for the visual design and user interface concept of the web application. He designed multiple visual themes and background artwork for the project, exploring different aesthetic directions including a stock chart theme, a beach and financial freedom theme, and a neon dark grid theme. The neon dark grid background image currently used on the live website is his design. His work established the visual identity of the project and gave the web application a distinctive and professional appearance.

### Sadiq

Sadiq was responsible for integrating all teammates' individual contributions into a single unified codebase and managing the full software development lifecycle of the project. This included merging Vihaan's and Priyan's Python logic into a combined `main.py` CLI application, initializing and managing the GitHub repository, scaffolding the full-stack web application architecture using React and Vite for the frontend and Flask for the backend, configuring Vercel deployment with the correct build and routing settings, implementing the CSS styling and glassmorphism card design, and writing all project documentation. He also resolved deployment issues including API routing configuration on Vercel and file naming issues with the background image asset.

---

## Common Mistakes This Tool Prevents

The following are common errors that students and new investors make when calculating stock returns. This tool is specifically designed to prevent them.

- Confusing percentage gain with dollar gain. A stock going up by 10 dollars means very different things depending on whether you own 1 share or 1000 shares. This tool always calculates total dollar profit based on quantity.
- Ignoring quantity. Price movement alone does not represent total profit or loss. This tool requires quantity as a mandatory input.
- Ignoring fees. Brokerage fees reduce your actual profit. This tool subtracts fees from the result to show the true net outcome.
- Showing only the final result. This tool displays every intermediate value including total investment, current value, and net profit or loss so that the full calculation is transparent and auditable.
- Accepting invalid inputs silently. This tool validates every input on the backend and returns a descriptive error message rather than producing a silently incorrect result.

---

This project was built for educational purposes as part of the ThinkSabio Internship 2026 Minor Projects Program, Technology Track, Project 5.
```
