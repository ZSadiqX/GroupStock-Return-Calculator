from flask import Flask, request, jsonify
from flask_cors import CORS
import math

app = Flask(__name__)
CORS(app)

def validate_inputs(buy_price, current_price, quantity, fees, dividends):
    if buy_price < 0 or current_price < 0 or quantity <= 0 or fees < 0 or dividends < 0:
        return False, "Prices, fees, and dividends cannot be negative. Quantity must be greater than zero."
    return True, ""

def calculate_return(buy_price, current_price, quantity, fees=0, dividends=0):
    investment = buy_price * quantity
    current_value = current_price * quantity
    profit_loss = current_value - investment - fees + dividends
    percent_return = (profit_loss / investment) * 100

    return {
        "Total Investment": round(investment, 2),
        "Current Value": round(current_value, 2),
        "Net Profit/Loss": round(profit_loss, 2),
        "Total Return (%)": round(percent_return, 2)
    }

@app.route('/api/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json
        buy = float(data.get('buy_price', 0))
        current = float(data.get('current_price', 0))
        qty = int(data.get('quantity', 0))
        fees = float(data.get('fees', 0))
        dividends = float(data.get('dividends', 0))

        is_valid, error_message = validate_inputs(buy, current, qty, fees, dividends)
        
        if not is_valid:
            return jsonify({"error": error_message}), 400

        results = calculate_return(buy, current, qty, fees, dividends)
        return jsonify(results)

    except ValueError:
        return jsonify({"error": "Invalid input format. Please ensure all values are numbers."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# This is required for Vercel
# Vercel looks for the app object in api/index.py
if __name__ == '__main__':
    app.run(port=5328, debug=True)
