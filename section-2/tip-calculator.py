# Input - Total bill ?
# Tip amount? percentage 10, 12 or 15
# Total person to split the bill?

# Final bill - Round to 2 decimal places

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

total_bill = bill * (1 + tip_percentage / 100)
bill_per_person = round((total_bill / people), 2)
bill_per_person = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${bill_per_person}")
