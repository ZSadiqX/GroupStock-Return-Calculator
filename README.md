# GroupStock Return Calculator

Welcome to the **GroupStock Return Calculator**! This project is a simple calculator that helps users track their stock investments by calculating the total investment, current/sell value, profit or loss, and percentage return.

## Features
- **Inputs**: Buy price, current/sell price, quantity, optional fees, and optional dividends.
- **Outputs**: Total investment, current value, profit/loss amount, percentage gain/loss, and final status (Profit/Loss/Break-even).

## Formulas Used
- **Investment** = `Buy Price × Quantity`
- **Current Value** = `Current/Sell Price × Quantity`
- **Profit/Loss** = `Current Value - Investment - Fees + Dividends`
- **Percentage Return** = `(Profit/Loss / Investment) × 100`

## How to Use
1. Make sure you have Python installed.
2. Run the Python script in your terminal:
   ```bash
   python feesdividends.py
   ```
3. Follow the interactive prompts to enter your investment details:
   - Buy price per share
   - Current price per share
   - Number of shares (quantity)
   - Brokerage fees
   - Dividends received
4. The calculator will display your results transparently.

## Team Contributions
- **Priyan**: Created the core Python calculator logic (`feesdividends.py`), incorporating fees and dividends into the calculation with clear user validation.
- **Prateek**: Conducted comprehensive QA testing (`QA_Testing.md`), outlining test cases for input validation and identifying edge cases.
- *More contributions to be added soon!*