def check_if_valid():
    while True:
        try:
            num = float(input("Please enter a number: "))
        except ValueError:
            print("That is not a number. Please try again.")
        else:
            return num

def f_to_c(a):
    return (a-32)*(5/9)

x = check_if_valid()

print("That temperature in Celsius is: " + str(f_to_c(x)))