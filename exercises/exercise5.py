def main():
    print(calculate_id(int(21145539)))
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
                sub_sum /= 10
                sub_sum = int(sub_sum)
                sub_sum += sub_digit
        sum += sub_sum
        id = id / 10
        id = int(id)
    return sum


def check_valid_id(id):
    last_digit = id % 10
    last_calc = calculate_id(id / 10)
    return last_calc == last_digit

if __name__ == '__main__':
    main()