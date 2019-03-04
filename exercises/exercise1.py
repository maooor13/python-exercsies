def main():
    run_bank()


# This function checks the user for pin
# Then it calls back to the actions
# If the user wants to quit or enters the wrong PIN it returns False
def check_screen(accounts, account):
    return check_pin(accounts, account) and actions(accounts, account)
    pass

def change_pin(accounts, account):
    print("Your current PIN is {}.".format(accounts[0][account]))
    print("What would you like your PIN to be?")
    print("Remember your PIN can be only 4 digits.")
    PIN = input()
    while not check_change_pin(PIN):
        PIN = input("Invalid PIN.\nTry Again.")
    accounts[0][account] = PIN
    print("Your PIN has been updated successfully!")
    print("Your current PIN is {}.".format(accounts[0][account]))
    pass

def check_change_pin(PIN):
    if PIN.isdigit():
        if len(PIN) is 4:
            return True
    return False


def change_balance(accounts, account, amount):
    accounts[1][account] = accounts[1][account] + amount
    print("You have successfully changed you balance.")
    print("You now have {} Shekels.".format(accounts[1][account]))
    pass

def withdraw(accounts, account):
    print("You have {}₪.".format(get_balance(accounts, account)))
    if get_balance(accounts,account) <= 0:
        print("You can't withdraw any money, you have no money.")
        return
    print("How much money would you like to withdraw?")
    print("a.20₪ b.50₪ c.other d.go back")
    print("Please use letters only")
    amount = input().lower()
    # WHILE UNTIL VALID ANSWER
    while amount != "a" and amount != "b" and amount != "c" and amount != "d":
        print("Invalid answer. Please choose a b or c")
        print("How much money would you like to withdraw?")
        print("a.20₪ b.50₪ c.other")
        print("Please use letters only")
        amount = input().lower()


    # IF ANSWER IS A - IF ANSWER IS 20 SHEKELS
    if amount == "a":
        # CHECK IF CAN WITHDRAW 20
        if get_balance(accounts,account) < 20:
            print("You can not withdraw 20 Shekels.\nYou have only {} Shekels.".format(get_balance(accounts,account)))
            withdraw(accounts, account)
        # CONFIRMATION
        answer = input("Are you sure you want to withdraw 20 Shekels?(y/n)")
        while answer != "y" and answer != "n":
            answer = input("Please enter a valid answer.\nAre you sure you want to withdraw 20 Shekels?(y/n)")
        if answer == "y":
            change_balance(accounts, account, -20)
            check_screen(accounts, account)
        elif answer == "n":
            withdraw(accounts, account)



    # IF ANSWER IS B - IF ANSWER IS 50 SHEKELS
    if amount == "b":
        # CHECK IF CAN WITHDRAW 50
        if get_balance(accounts,account) < 50:
            print("You can not withdraw 20 Shekels.\nYou have only {} Shekels.".format(get_balance(accounts,account)))
            withdraw(accounts, account)
        # CONFIRMATION
        answer = input("Are you sure you want to withdraw 50 Shekels?(y/n)")
        while answer != "y" and answer != "n":
            answer = input("Please enter a valid answer.\nAre you sure you want to withdraw 50 Shekels?(y/n)")
        if answer == "y":
            change_balance(accounts, account, -50)
            check_screen(accounts, account)
        elif answer == "n":
            withdraw(accounts, account)



    # IF ANSWER IS C - IF ANSWER IS OTHER
    if amount == "c":
        how_much = input("How much would you like to withdraw?")
        while not valid_amount_input(accounts, account, how_much):
            print("Can't withdraw {}₪.".format(how_much))
            print("Returning to withdrawal screen.")
            withdraw(accounts, account)

        answer = (input("Are you sure you want to withdraw {} Shekels?(y/n)".format(how_much)))
        while answer != "y" and answer != "n":
            answer = input("Please enter a valid answer.\nAre you sure you want to withdraw {} Shekels?(y/n)".format(how_much))

        if answer == "y":
            change_balance(accounts, account, int(how_much)*-1)
            check_screen(accounts, account)

        elif answer == "n":
            withdraw(accounts, account)

    if amount == "d":
        check_screen(accounts,account)

    pass

def valid_amount_input(accounts, account, amount):
    # Returns false if not valid input for amount
    if amount.isdigit():
        if 0 < int(amount) <= get_balance(accounts, account) :
            return True
    return False
    pass

def get_balance(accounts, account):
    return accounts[1][account]
    pass

def get_action():
    switcher = {
        "a": "balance",
        "bal": "balance",
        "view": "balance",
        "balance": "balance",

        "b": "withdraw",
        "wit": "withdraw",
        "withdraw": "withdraw",

        "c": "pin",
        "PIN": "pin",
        "pin": "pin",

        "d": "quit",
        "quit": "quit",
        "q": "quit",
    }

    option = input("What would you like to do? ")
    return switcher.get(option.lower(), "invalid")
    pass

# This def gets all accounts(so it can change the PIN) and account number.
# returns False if the user chose to quit.
def actions(accounts, account):
    print("Welcome!\n"
          "In our bank you can do multiple actions!")
    print("You can - \n"
          "a. View balance(\"bal\" or 'a'). b. Withdraw money(\"wit\" or 'b').\n"
          "c. Change PIN(\"PIN\" or 'c').   d. Quit(\"Quit\" or 'd')")
    action = get_action()
    while action == "invalid":
        print("Invalid action.")
        action = get_action()
    handle_action(accounts,account,action)
    pass

def handle_action(accounts, account, action):
    if action == "balance":
        print("The balance of account {} is: {}₪.".format(account, get_balance(accounts, account)))
    if action == "withdraw":
        withdraw(accounts, account)
    if action == "pin":
        change_pin(accounts, account)
    if action == "quit":
        print("Thanks you for using our bank.\nGoodbye.")
        return False
    return True

# This function gets all accounts, account number and PIN number
# Returns True if PIN is the pin num of account
# User has 3 attempt to enter the correct PIN
def check_pin(accounts, account):
    PIN = input("Enter PIN number.")
    counter = 4
    print("You entered {}.".format(PIN))
    while accounts[0][account] != PIN and counter:
            print("You've enter wrong PIN.\n"
                  "You have {} more tries.\n".format(counter))
            counter = counter - 1
            PIN = input("Enter PIN number.\n")
    if accounts[0][account] == PIN:
        return True
    print("You have entered the wrong PIN number too many times.")
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
    pass

# These function initiates all accounts
# and assign them with PIN number and balance
def init_accounts():
    # Account is a variable that contains two dictionaries
    # First dictionary is acc number and PIN
    # Second dictionary is acc number and balance
    accounts = {
        # Dictionary of account_number:PIN
        "123456":"1234",
        "598123":"5486",
        "112358":"8510",
        "000000":"0000"
    },{
        # Dictionary of account_number:balance
        "123456": 5000,
        "598123": 84320,
        "112358": -120,
        "000000": 0
    }
    return accounts
    pass

def run_bank():
    accounts = init_accounts()
    print(accounts)
    account_number = get_bank_acc_number(accounts)
    print("Account number:{}".format(account_number))
    while check_screen(accounts, account_number):
        pass
    run_bank()
    pass

if __name__ == '__main__':
    main()