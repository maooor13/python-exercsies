def main():
    get_list()
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




if __name__ == '__main__':
    main()