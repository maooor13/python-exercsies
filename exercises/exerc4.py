def main():
    string = input("Enter string.")
    string = string_compress(string)
    print(string)

    pass


def string_compress(string):
    new_string = ""
    amount = 1
    new_string += string[amount - 1]

    for char in range(len(string) - 1):
        if string[char] == string[char + 1]:
            amount = amount + 1
        else:
            new_string += str(amount)
            new_string += string[char + 1]
            amount = 1
    new_string += str(amount)
    return new_string
    pass


if __name__ == '__main__':
    main()
