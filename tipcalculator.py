print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? £"))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_percent = (tip / 100) + 1 

to_pay = round(total_bill / people * tip_percent, 2)
to_pay = "{:.2f}".format(to_pay)

print (f"Each person should pay: £{to_pay}")
