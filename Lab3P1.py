import statistics

def main():
    num1 = check_if_valid()
    num2 = check_if_valid()
    num3 = check_if_valid()
    print("The average is {0}".format(round(calc_average(num1,num2,num3),2)))
    return

def check_if_valid():
    while True:
        try:
            input_val = float(input("Please enter a number: "))
            return input_val
        except ValueError:
            print("That is not a number, please try again.")

def calc_average(a,b,c):
    tmp_list = [a,b,c]
    return statistics.mean(tmp_list)

main()