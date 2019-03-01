def change_pin():
    pass

def withdraw():
    pass

def print_balance():
    pass

def commands():
    pass

def check_pin():
    pass

def get_bank_acc_number():
    pass

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

def main():
    run_bank()


if __name__ == '__main__':
    main()