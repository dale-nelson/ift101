import time
<<<<<<< HEAD
dur = time.time()
=======
>>>>>>> ca52a16fe01ae2a839c77a24d96f2c8c13c511f3

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

<<<<<<< HEAD
print("The total of both numbers is {0}.".format(z))

print("This program took {0} seconds to run.".format(round(time.time()-dur,2)))
=======
print("The total of both numbers is: " + str(z))
>>>>>>> ca52a16fe01ae2a839c77a24d96f2c8c13c511f3
