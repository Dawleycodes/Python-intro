from datetime import datetime

name = input("What is your name? ")

try:
    birth_year = int(input("What year were you born? "))
except ValueError:
    print("Please enter a valid year (numbers only).")
    exit()

current_year = datetime.now().year
age = current_year - birth_year

print(f"\nHello {name}")

if age < 0:
    print("You entered a future year 🤨")
elif age < 18:
    print("You are a minor")
elif age < 65:
    print("You are an adult")
else:
    print("You are a senior")

