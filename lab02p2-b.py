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
<<<<<<< HEAD
deg = "\u00b0"

print("That temperature in Fahrenheit is {0}{1}C".format(round(f_to_c(x),2),deg))
=======

print("That temperature in Celsius is: " + str(f_to_c(x)))
>>>>>>> ca52a16fe01ae2a839c77a24d96f2c8c13c511f3
