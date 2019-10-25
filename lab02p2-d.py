print("This program calculates the value of a $5000 principal investment annually.")
princ = 5000
apr = 3

def check_if_valid():
    while True:
        try:
            val = float(input("How many years do you want to calculate? Decimals are also accepted. "))
        except ValueError:
            print("That is not a number. Please try again.")
        else:
            return val

def value(a,b,c):
    return a*((1+(0.03*b))**c)

years = check_if_valid()

print("The value after {0} years is: ${1}".format(years,round(value(princ,apr,years),2)))