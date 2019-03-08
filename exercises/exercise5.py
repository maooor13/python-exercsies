def main():
    id = input("Enter ID.")
    if id.isdigit():
        if check_valid_id(int(id)):
            print("Valid.")
        else:
            print("Not valid.")
    else:
        main()
    pass


def calculate_id(id):
    sum = 0
    for digit in range(len(str(id))):
        if digit % 2 == 1:
            sub_sum = id % 10
        else:
            sub_sum = id % 10 * 2
            if sub_sum >= 10:
                sub_digit = sub_sum % 10
                sub_sum = int(sub_sum / 10)
                sub_sum += sub_digit
        sum += sub_sum
        id = int(id / 10)
    return sum


def sub_from_ten(calc):
    tens = int(calc / 10)
    tens += 1
    tens *= 10
    return tens - calc

def check_valid_id(id):
    last_digit = id % 10
    calc = calculate_id(int(id / 10))
    calc = sub_from_ten(calc)
    return calc == last_digit


if __name__ == '__main__':
    main()
