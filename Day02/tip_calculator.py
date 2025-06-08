# Day02 - Tip Calculator
import time

print("Welcome to the tip calculator!")
time.sleep(2)
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
total = (bill + (bill * tip / 100)) / people
time.sleep(1)
print(f"Each person should pay: ${total}")
