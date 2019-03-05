factorial_decor = {}

def main():
    # Can't do factorial for 998 or over.
    try:
        factorial(998)
    except:
        print("I can't do factorial of 998, too much recursion :(")
    # Decoring the max
    factorial(997)
    # Can do 1992 factorial.
    print(factorial(1992))
    pass


def decorator(x):
    if x in factorial_decor:
        return factorial_decor[x]




def factorial(x):
    if x == 1:
        return 1
    if decorator(x):
        return decorator(x)
    else:
        answer = x * factorial(x-1)
        factorial_decor[x] = answer
        return answer


if __name__ == '__main__':
    main()