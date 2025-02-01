# Day 2 - Tip calculator
print("Welcome to the tip calculator!")
total_bill_amount = float(input("What was the total bill?: $"))
tip_amount = float(input("How much tip would you like to give?: $"))
people_amount = int(input("How many people split the bill?: "))
split_amount = (total_bill_amount + tip_amount) / people_amount
print(f"Each person should pay: ${round(split_amount, 2)}")
