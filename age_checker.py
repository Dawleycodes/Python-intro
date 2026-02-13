from datetime import datetime

name = input("What is your name? ")
birth_year = int(input("What year were you born? "))

current_year = datetime.now().year
age = current_year - birth_year

print(f"Hello {name}")

if age < 18:
    print("You are a minor")
else:
    print("You are an adult")
