def main():
    list = [1,2,3]
    print(list)
    list = Map(add5,list)
    print(list)
    pass


def add5(x):
    return x+5


def Map(f,list):
    new_list = []
    try:
        for x in list:
            new_list.append(f(x))
    except TypeError:
        print("Bad params for function {}.".format(f.__name__))
        print("Returning list with good params.")
    return new_list


if __name__ == '__main__':
    main()