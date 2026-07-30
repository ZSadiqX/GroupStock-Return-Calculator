def calculate_return(buy_price, current_price, quantity, fees=0, dividends=0):

    if buy_price < 0:
        raise ValueError("Buy price cannot be negative.")
    if current_price < 0:
        raise ValueError("Current price cannot be negative.")
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")
    if fees < 0:
        raise ValueError("Fees cannot be negative.")
    if dividends < 0:
        raise ValueError("Dividends cannot be negative.")

   
    investment = buy_price * quantity
    current_value = current_price * quantity
    profit_loss = current_value - investment - fees + dividends
    percent_return = (profit_loss / investment) * 100

    return investment, current_value, profit_loss, percent_return


def main():
    print("=== Stock Return Calculator (Fees & Dividends) ===")

    buy_price = float(input("Enter buy price per share: $"))
    current_price = float(input("Enter current price per share: $"))
    quantity = int(input("Enter number of shares: "))
    fees = float(input("Enter brokerage fees ($0 if none): $"))
    dividends = float(input("Enter dividends received ($0 if none): $"))

    investment, current_value, profit_loss, percent_return = calculate_return(
        buy_price,
        current_price,
        quantity,
        fees,
        dividends
    )

    print("\n----- Results -----")
    print(f"Investment: ${investment:.2f}")
    print(f"Current Value: ${current_value:.2f}")
    print(f"Profit/Loss: ${profit_loss:.2f}")
    print(f"Percent Return: {percent_return:.2f}%")

    if profit_loss > 0:
        print("Status: Profit")
    elif profit_loss < 0:
        print("Status: Loss")
    else:
        print("Status: Break-even")

if __name__ == "__main__":
    main()
