def main():
    print("Please enter in a numeric value between 0 and 100 for a grade.")
    valid_val = loop_until_valid()
    pos_val = loop_until_pos(valid_val)
    print("The grade is {0}".format(retrieve_grade(pos_val)))
    return

def retrieve_grade(input):
    if input >= 90 and input <= 100:
        grade = 'A'
    elif input >= 80 and input < 90:
        grade = 'B'
    elif input >= 70 and input < 80:
        grade = 'C'
    elif input >= 60 and input < 70:
        grade = 'D'
    else:
        grade = 'F'
    return grade

def check_if_valid():
    try:
        return int(float(input()))
    except ValueError:
        print("That is not a number. Please try again.")
    return

def loop_until_valid():
    valid_check = check_if_valid()
    while not valid_check:
        valid_check = check_if_valid()
    else:
        return valid_check

def loop_until_pos(input):
    while input < 0 or input > 100:
        print("Only numbers between 0 and 100 can be accepted. Please try again.")
        input = loop_until_valid()
    else:
        return input

main()