def main():
    print(factorial(500))
    pass


def factorial(x):
    return x * factorial(x-1)


if __name__ == '__main__':
    main()