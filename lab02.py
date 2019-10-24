import time

print("This program will add 2 numbers that the user provides.")
time.sleep(2)

def check_if_valid():
    while True:
        try:
            num = float(input("Please enter a number: "))
        except ValueError:
            print("That was not a number, please try again.")
            continue
        else:
            return float(num)

a = check_if_valid()
b = check_if_valid()

print("The sum is " + str(a+b))