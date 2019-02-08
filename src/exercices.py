def ex_1(n):
    for i in range(1, n+1):
        print(i)


def ex_2(n):
    for i in range(n, 0, -1):
        print(i)


def ex_3(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def ex_4(age):
    if age in range(100):
        if age < 18:
            print('Mineur')
        elif age < 23:
            print('Etudiant')
        elif age < 62:
            print('Travailleur')
        else:
            print('Retraite')
    else:
        print('Age invalide')
