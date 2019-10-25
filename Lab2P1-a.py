import time

print("This program will take 2 numbers and add them together. Decimals can be used.")
time.sleep(1.5)

def check_if_valid():
    while True:
        try:
            var = float(input("Please enter a number: "))
        except ValueError:
            print("This is not a number. Please try again.")
        else:
            return var

def sum(a,b):
    return float(a)+float(b)

x=check_if_valid()
y=check_if_valid()

z=sum(x,y)

print("The total of both numbers is: " + str(z))