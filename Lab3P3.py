def main():
    global num_input
    print("This program checks if a number is positive, negative, or 0.")
    loop_until_valid()
    if num_input < 0:
        print("{0} is negative.".format(round(num_input, 2)))
    elif num_input > 0:
        print("{0} is positive.".format(round(num_input, 2)))
    elif not num_input:
        print("Your input equals 0.")
    return

def check_if_valid():
    global num_input
    try:
        num_input = float(input())
        return True
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