# GroupStock Return Calculator - Combined Edition
# Contributors: Vihaan, Priyan, Prateek, Sadiq

# --- FUNCTION 1: INPUT VALIDATION ---
# This function makes sure the user didn't enter bad data (From Vihaan & Priyan)
def validate_inputs(buy_price, current_price, quantity, fees, dividends):
    # Check if prices are negative or if quantity is zero or less
    if buy_price < 0 or current_price < 0 or quantity <= 0 or fees < 0 or dividends < 0:
        print("❌ Error: Prices, fees, and dividends cannot be negative. Quantity must be greater than zero.")
        return False  # Stops the app because data is invalid
    return True  # Allows the app to continue because data is good


# --- FUNCTION 2: CORE CALCULATOR ENGINE ---
# This function handles the required mathematical formulas (From Vihaan & Priyan)
def calculate_return(buy_price, current_price, quantity, fees=0, dividends=0):
    # Formula 1: Calculate total initial investment
    investment = buy_price * quantity

    # Formula 2: Calculate what the stock is worth right now
    current_value = current_price * quantity

    # Formula 3: Calculate total dollar profit or loss (incorporating fees and dividends)
    profit_loss = current_value - investment - fees + dividends

    # Formula 4: Calculate the total percentage return
    percent_return = (profit_loss / investment) * 100

    # Package all results into a dictionary and round them to 2 decimals
    return {
        "Total Investment": round(investment, 2),
        "Current Value": round(current_value, 2),
        "Net Profit/Loss": round(profit_loss, 2),
        "Total Return (%)": round(percent_return, 2)
    }


# --- FUNCTION 3: USER TERMINAL INTERFACE ---
# This function manages the questions asked in the terminal
def run_calculator_app():
    print("===========================================")
    print(" 📈 GroupStock Return Calculator Engine 📉")
    print("===========================================")

    # Ask the user for inputs 
    stock_symbol = input("Enter Stock Symbol (e.g., AAPL): ").upper()
    buy = float(input(f"Enter Buy Price for {stock_symbol} ($): "))
    current = float(input(f"Enter Current Price for {stock_symbol} ($): "))
    qty = int(input("Enter Number of Shares: "))
    fees = float(input("Enter Brokerage Fees ($0 if none): $"))
    dividends = float(input("Enter Dividends Received ($0 if none): $"))

    print("\nProcessing calculations...")
    print("-------------------------------------------")

    # Run the validation step first before doing any math
    if validate_inputs(buy, current, qty, fees, dividends):
        # Send the clean numbers to the calculation engine
        results = calculate_return(buy, current, qty, fees, dividends)

        # Display the final calculated results neatly
        print(f"--- 📊 CALCULATED METRICS FOR {stock_symbol} ---")
        print(f"Total Investment: ${results['Total Investment']:.2f}")
        print(f"Current Value:    ${results['Current Value']:.2f}")

        # Format the Net Profit/Loss to show a + or - sign clearly
        net_pl = results["Net Profit/Loss"]
        if net_pl > 0:
            print(f"Net Profit/Loss:  +${net_pl:.2f}")
            print("Status:           ✅ Profit")
        elif net_pl < 0:
            # Replaces Python's default negative sign (-) with standard currency formatting (-$)
            formatted_loss = f"-${abs(net_pl):.2f}"
            print(f"Net Profit/Loss:  {formatted_loss}")
            print("Status:           ❌ Loss")
        else:
            print(f"Net Profit/Loss:  ${net_pl:.2f}")
            print("Status:           ➖ Break-even")

        print(f"Total Return (%): {results['Total Return (%)']:.2f}%")
        print("===========================================")


# --- START THE APP ---
if __name__ == "__main__":
    run_calculator_app()
