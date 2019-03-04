def main():
    # get_list()
    get_list_as_list()
    pass


def is_int(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def get_list():
    sum = 0
    print("Enter numbers until you want to stop.")
    print("When you want to stop type \"Stop\".")
    num = input("Enter Number.\n")
    while num.lower() != "stop":
        if is_int(num):
            sum = sum + int(num)
        else:
            print("Invalid input, ignoring.")
        num = input("Enter Number.\n")
    print("The sum is {}.".format(sum))


def get_list_as_list():
    sum = 0
    print("Enter numbers by list.")
    print("For example - \"1,2,3,4,5\"")
    lst = input("Input:")
    lst = lst.split(',')
    print(lst)
    try:
        for num in lst:
          sum = sum + int(num)
    except:
        print("Bad list. Try again.")
        get_list_as_list()
    print(sum)


if __name__ == '__main__':
    main()