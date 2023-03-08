
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give?10, 12, or 15? "))
no_of_people = int(input("How many people to split the bill? "))
# (bill + (tip%bill)) / people_count
tip_as_percent = tip_percentage / 100
total_tip_amount = bill * tip_as_percent
total_bill = total_tip_amount + bill
bill_to_be_paid = total_bill/no_of_people
bill_to_be_paid = "{:.2f}".format(bill_to_be_paid)
print(f"Each person should pay: ${bill_to_be_paid}")