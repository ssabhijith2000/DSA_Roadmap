myList = [1, 20, 30, 40, 40]


def isUnique(list):
    a = []
    for i in list:
        if i in a:
            print(i)
            return False
        else:
            a.append(i)
    return True
