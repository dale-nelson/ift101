def main():
    print("This program checks if a number is positive, negative, or 0.")
    input_val = loop_until_valid()
    if input_val < 0:
        print("{0} is negative.".format(round(input_val, 2)))
    elif input_val > 0:
        print("{0} is positive.".format(round(input_val, 2)))
    else:
        #0 isn't working!!!! Try and find out why.
        print("Your input equals 0.")
    return

def check_if_valid():
    try:
        return float(input())
    except ValueError:
        print("That is not a number. Please try again.")
    return

def loop_until_valid():
    valid_check = check_if_valid()
    while not valid_check:
        valid_check = check_if_valid()
    else:
        return valid_check

main()