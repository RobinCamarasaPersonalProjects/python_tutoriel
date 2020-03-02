import numpy as np


def ex_1(n: int) -> np.ndarray:
    """
    Creer une fonction qui affiche les nombres entre 1 et n par ordre croissant.

    :param n: Un nombre
    """
    for i in range(1, n+1):
        print(i)


def ex_2(n: int) -> np.ndarray:
    """
    Creer une fonction qui affiche les nombres entre 1 et n par ordre décroissant.

    :param n: Un nombre
    """
    for i in range(n, 0, -1):
        print(i)


def ex_3(n: int) -> np.ndarray:
    """
    Créer la fonction factorielle

    :param n: Un nombre
    """
    acc = 1
    for i in range(1, n+1):
        acc *= i
    return acc


def ex_4(age):
    """
    Créer une fonction affichant la catégorie d’une personne en fonction de son age.

    :param age: Age de la personne consideree
    """
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

