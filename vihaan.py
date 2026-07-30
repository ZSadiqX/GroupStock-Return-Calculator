# --- FUNCTION 1: INPUT VALIDATION ---
# This function makes sure the user didn't enter bad data
def validate_inputs(buy_price, current_price, quantity):
    # Check if prices are negative or if quantity is zero or less
    if buy_price < 0 or current_price < 0 or quantity <= 0:
        print("❌ Error: Prices cannot be negative. Quantity must be greater than zero.")
        return False  # Stops the app because data is invalid
    return True  # Allows the app to continue because data is good


# --- FUNCTION 2: CORE CALCULATOR ENGINE ---
# This function handles the 4 required mathematical formulas
def calculate_return(buy_price, current_price, quantity):
    # Formula 1: Calculate total initial investment
    investment = buy_price * quantity

    # Formula 2: Calculate what the stock is worth right now
    current_value = current_price * quantity

    # Formula 3: Calculate total dollar profit or loss
    profit_loss = current_value - investment

    # Formula 4: Calculate the total percentage return
    percent_return = (profit_loss / investment) * 100

    # Package all 4 results into a dictionary and round them to 2 decimals
    return {
        "Total Investment": round(investment, 2),
        "Current Value": round(current_value, 2),
        "Net Profit/Loss": round(profit_loss, 2),
        "Total Return (%)": round(percent_return, 2)
    }


# --- FUNCTION 3: USER TERMINAL INTERFACE ---
# This function manages the questions asked in the PyCharm terminal
def run_calculator_app():
    print(" Stock Return Calculator Engine")
    print("-----------------------------------")

    # Ask the user for inputs so we never have to type numbers into the code text
    buy = float(input("Enter Buy Price ($): "))
    current = float(input("Enter Current Price ($): "))
    qty = int(input("Enter Number of Shares: "))

    print("\nProcessing calculations...")
    print("-----------------------------------")

    # Run the validation step first before doing any math
    if validate_inputs(buy, current, qty):
        # Send the clean numbers to the calculation engine
        results = calculate_return(buy, current, qty)

        # Display the final calculated results neatly
        print("--- CALCULATED METRICS ---")
        print(f"Total Investment: ${results['Total Investment']}")
        print(f"Current Value: ${results['Current Value']}")

        # Format the Net Profit/Loss to show a + or - sign clearly
        net_pl = results["Net Profit/Loss"]
        if net_pl > 0:
            print(f"Net Profit/Loss: +${net_pl}")
        else:
            # Replaces Python's default negative sign (-) with standard currency formatting (-$)
            formatted_loss = str(net_pl).replace("-", "-$")
            print(f"Net Profit/Loss: {formatted_loss}")

        print(f"Total Return (%): {results['Total Return (%)']}%")


# --- START THE APP ---
# This line automatically triggers the program when you hit run in PyCharm
if __name__ == "__main__":
    run_calculator_app()
