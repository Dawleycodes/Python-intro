print("Welcome to the tip calculator by Dawley.")
bill = float(input("what was the total bill?\n $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?\n"))
split = float(input("How many people to split the bill?\n "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_percent = total_bill / split
final_amount = round(bill_per_percent, 2)
print(f"total bill including tip: ${total_bill}")
print(f"Tip amount: ${total_tip_amount}")
print(f"Each person should pay ${final_amount}")


