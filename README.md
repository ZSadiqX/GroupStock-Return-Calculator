# GroupStock Return Calculator

Welcome to the **GroupStock Return Calculator**! This project is a simple calculator that helps users track their stock investments by calculating the total investment, current/sell value, profit or loss, and percentage return.

## Features
- **Inputs**: Stock symbol, buy price, current/sell price, quantity, optional fees, and optional dividends.
- **Outputs**: Total investment, current value, profit/loss amount, percentage gain/loss, and final status (Profit/Loss/Break-even).
- **Validation**: Ensures that invalid entries (like negative prices or quantities of zero) are caught before calculations run.

## Formulas Used
- **Investment** = `Buy Price × Quantity`
- **Current Value** = `Current/Sell Price × Quantity`
- **Profit/Loss** = `Current Value - Investment - Fees + Dividends`
- **Percentage Return** = `(Profit/Loss / Investment) × 100`

## How to Use
1. Make sure you have Python installed.
2. Run the combined application in your terminal:
   ```bash
   python main.py
   ```
3. Follow the interactive prompts to enter your investment details.
4. The calculator will display your results transparently with a beautifully formatted UI!

## Team Contributions
- **Vihaan**: Built the foundational calculator engine with dictionary mapping, the input validation logic (to prevent bad data), and the neat terminal user interface format.
- **Priyan**: Created the core Python calculator logic in `feesdividends.py`, incorporating fees and dividends into the math calculation.
- **Prateek**: Conducted comprehensive QA testing (`QA_Testing.md`), outlining test cases for input validation and identifying edge cases.
- **Sadiq**: Integrated and patchwork combined all teammate's code into one unified, nice looking application (`main.py`).