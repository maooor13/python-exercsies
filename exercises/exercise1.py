def main():
    run_bank()

def back_screen(accounts, account):
    print("to check pin again and call get action :) - todo")
    pass

def change_pin(accounts, account):
    print("no pin for you - todo")
    pass

def change_balance(accounts, account, amount):
    accounts[1][account] = accounts[1][account] + amount
    print("You have successfully changed you balance.")
    print("You now have {} Shekels.".format(accounts[1][account]))
    pass

def withdraw(accounts, account):
    if get_balance(accounts,account) < 0:
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
            back_screen(accounts, account)
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
            back_screen(accounts, account)
        elif answer == "n":
            withdraw(accounts, account)



    # IF ANSWER IS C - IF ANSWER IS OTHER
    if amount == "c":
        how_much = int(input("How much would you like to withdraw?"))
        # CHECK IF TRIES TO WITHDRAW NEGATIVE AMOUNT
        while how_much<=0:
            how_much = int(input("{} must be positive.\n How much would you like to withdraw?".format(how_much)))
        # CHECK IF CAN WITHDRAW AMOUNT GIVEN
        if get_balance(accounts,account) < how_much:
            print("You can not withdraw {} Shekels.\nYou have only {} Shekels.".format(how_much,get_balance(accounts,account)))
            withdraw(accounts, account)
        # CONFIRMATION
        answer = (input("Are you sure you want to withdraw {} Shekels?(y/n)".format(how_much)))
        while answer != "y" and answer != "n":
            answer = input("Please enter a valid answer.\nAre you sure you want to withdraw {} Shekels?(y/n)".format(how_much))
        if answer == "y":
            change_balance(accounts, account, how_much*-1)
            back_screen(accounts, account)
        elif answer == "n":
            withdraw(accounts, account)

    if amount == "d":
        back_screen(accounts,account)

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
# returns True or False.
# returns False if the user choose to quit.
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
    if action == "balance":
        print("The balance of account {} is: {}.".format(account, get_balance(accounts, account)))
    if action == "withdraw":
        withdraw(accounts, account)
    if action == "pin":
        change_pin(accounts, account)
    if action == "quit":
        print("Thanks you for using our bank. \n Goodbye.")
        return False

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
    if not check_pin(accounts, account_number, input("Enter PIN number.\n")):
        print("You have reached the maximum amount of attempts.\n"
              "Try again later.")
        return
    while not actions(accounts, account_number):
        return


    pass

if __name__ == '__main__':
    main()