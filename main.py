name = input("What is your name? ")
birth_year = int(input("What year were you born? "))

age = 2026 - birth_year

print("Hello", name)

if age < 18:
    print("You are a minor")
else:
    print("You are an adult")
