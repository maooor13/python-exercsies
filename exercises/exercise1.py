def change_pin():
    pass

def withdraw():
    pass

def print_balance():
    pass

def actions():
    pass

# This function gets all accounts, account number and PIN number
# Returns True if PIN is the pin num of account
# User has 3 attempt to enter the correct PIN
def check_pin(accounts, account, PIN):
    counter = 3
    print("You entered {}.".format(PIN))
    while accounts[0][account] != PIN and counter:
            print("You've enter wrong PIN.\n"
                  "You have {} more tries.\n".format(counter))
            counter = counter - 1
            PIN = input("Enter PIN number.\n")
    if accounts[0][account] == PIN:
        return True
    return False
    pass

# This function gets all accounts and waits
# for user to input his account number.
def get_bank_acc_number(accounts):
    account_number = input("Please enter your bank account number.\n")
    while account_number not in accounts[0]:
        account_number = input("Try again.\n"
                               "Please enter your bank account number.")
    answer = input("The account number that you entered is {}.\n"
                   "confirm?(y/n)".format(account_number))
    while answer is not "y" and answer is not "n":
          answer = input("Invalid answer.\n"
                       "The account number that you entered is {}.\n"
                       "confirm?(y/n)".format(account_number))
    if answer is "y":
        return account_number
    get_bank_acc_number(accounts)

# These function initiates all accounts
# and assign them with PIN number and balance
def init_accounts():
    # Account is a variable that contains two dictionaries
    # First dictionary is acc number and PIN
    # Second dictionary is acc number and balance
    accounts = {
        "123456":"1234",
        "598123":"5486",
        "112358":"8510",
        "000000":"0000"
    },{
        "123456": 5000,
        "598123": 84320,
        "112358": -120,
        "000000": 0
    }
    return accounts

def run_bank():
    accounts = init_accounts()
    print(accounts)
    account_number = get_bank_acc_number(accounts)
    print("Account number:{}".format(account_number))
    while check_pin(accounts, account_number, input("Enter PIN number.\n")) == False:
        print("You have reached the maximum amount of attempts.\n"
              "Try again later.")
        return
    actions()


def main():
    run_bank()


if __name__ == '__main__':
    main()