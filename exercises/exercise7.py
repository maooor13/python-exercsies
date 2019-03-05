factorial_decor = {}

def main():
    print(factorial(500))
    pass


def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x-1)


if __name__ == '__main__':
    main()