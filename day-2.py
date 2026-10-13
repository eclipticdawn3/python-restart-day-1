Starting_Balance = 2750000
Starting_Balance = 2750000
Received_Amount = 423785
Paid_Amount = 233657
Total_Remaining_Balance = Starting_Balance + Received_Amount - Paid_Amount

print(f"Your Remaining Balance Is: {Total_Remaining_Balance}")

transaction_type =input("Did You Receive or Pay? ")
transaction_amount =int(input("Enter Amount :"))

if transaction_type == "Receive":
    Starting_Balance += transaction_amount
else:
    Starting_Balance -= transaction_amount

print(f" Your Remaining Balance Is: {Starting_Balance}")


