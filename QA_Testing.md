# QA Testing Results

| Test ID | Test Case | Input | Expected Output | Actual Output | Pass/Fail | Screenshot |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| TC-01 | Negative buy price | -100 | Reject negative value and prompt for valid input | Displayed "Value cannot be negative. Please try again." and requested input again | Pass | testcase1 |
| TC-02 | Negative sell price | -50 | Reject input and prompt again | Displayed "Value cannot be negative. Please try again." and requested input again | Pass | testcase2 |
| TC-03 | Negative quantity | -5 | Reject input and prompt again | Displayed "Quantity must be at least 1." and requested input again | Pass | testcase3 |
| TC-04 | Zero quantity | 0 | Reject input (quantity should be greater than 0) | Displayed "Quantity must be at least 1." and requested input again | Pass | testcase4 |
| TC-05 | Zero buy price | 0 | Reject input or display a clear error | Displayed "Value must be greater than zero." and requested input again | Pass | testcase5 |
| TC-06 | Zero sell price | 0 | Accept if valid, or display an appropriate error | Displayed "Value must be greater than zero." and requested input again | Pass | testcase6 |
| TC-07 | Empty buy price | Press Enter without typing anything | Prompt for valid input | Displayed "Input cannot be empty. Please try again." and requested input again. | Pass | testcase7 |
| TC-08 | Empty sell price | Press Enter | Prompt for valid input | Displayed "Input cannot be empty. Please try again." and requested input again. | Pass | testcase8 |
| TC-09 | Empty quantity | Press Enter | Prompt for valid input | Displayed "Input cannot be empty. Please try again." and requested input again. | Pass | testcase9 |
| TC-10 | Decimal buy price | 100.5 | Accept and continue | Accepts and continues | Pass | |
| TC-11 | Decimal sell price | 125.75 | Accept and continue | Accepts and continues | Pass | testcase10/11/12 |
| TC-12 | Decimal quantity | 2.5 | Accept only if fractional shares are supported; otherwise reject | Displayed "Please enter a whole number (no decimals)." and requested input. | Pass | |
| TC-13 | Letters | abc | Reject input | Displayed "Please enter a valid number." and requested input for buy/sell price. Displayed "Please enter a whole number (no decimals)." and requested input for quantity. | Pass- but output for quantity can be changed to "Please enter a valid number." instead of "Please enter a whole number (no decimals)." | testcase13 |
| TC-14 | Mixed letters and numbers | 123abc | Reject input | Displayed "Please enter a valid number." and requested input for buy/sell price. Displayed "Please enter a whole number (no decimals)." and requested input for quantity. | Pass- but output for quantity can be changed to "Please enter a valid number." instead of "Please enter a whole number (no decimals)." | testcase14 |
| TC-15 | Special characters | @#$% | Reject input | Displayed "Please enter a valid number." and requested input for buy/sell price. Displayed "Please enter a whole number (no decimals)." and requested input for quantity. | Pass- but output for quantity can be changed to "Please enter a valid number." instead of "Please enter a whole number (no decimals)." | testcase15 |
| TC-16 | Spaces only | " " | Treat as invalid input | Displayed "Input cannot be empty. Please try again." and requested input again. | Pass | testcase16 |
| TC-17 | Leading/trailing spaces | " 100 " | Trim spaces and accept | Accepts and continues. | Pass | testcase17 |
| TC-18 | Very large number | 999999999999 | Accept or display a limit error; no crash | Accepts and continues; no crash. | Pass | testcase18 |
| TC-19 | Very small decimal | 0.000001 | Accept if appropriate or reject gracefully | Accepts and continues. | Pass | testcase19 |
| TC-20 | Multiple decimal points | 12.3.4 | Reject input | Displayed "Please enter valid number." and requested input. | Pass | testcase20 |
| TC-21 | Scientific notation | 1.00E+06 | Accept if supported; otherwise reject | Displayed "Please enter valid number." and requested input. | Pass- scientific notation not supported. | testcase21 |
| TC-22 | Comma in number | 1,000 | Accept or display a clear validation error | Displayed "Please enter valid number." and requested input. | Fail- does not accept inputs with comma in number. | testcase22 |
| TC-23 | Plus sign | (+)100 | Accept or reject consistently | Accepts consistently. | Pass | testcase23 |
| TC-24 | Valid input (control test) | Buy = 100, Sell = 150, Qty = 10 | Calculate correct profit and return | Displays "Stock Return Report" and requests to show scenario table. | Pass | testcase24 |
