import numpy as np


def ex_1(c: str) -> int:
    """
    Créer une fonction qui renvoie la position dans l’alphabet d’un charactère.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return alphabet.index(c) + 1


def ex_2(s: str) -> list:
    """
    En s’aidant de l’exercice 1, créer une fonction qui renvoie la liste des positions dans
    l’alphabet des charactères d’une chaîne de charactère.
    """
    result = []
    for c in s:
        result.append(ex_1(c))
    return result


def ex_3(n: int) -> list:
    """
    Implémentez une fonction qui renvoie la liste des nombres premiers  entre  1  et  n a
    l’aide  de  la  méthode  du  crible  d’Eratosthene

    :param n: Nombre
    """
    prime = [True] * (n+1)
    prime[0] = False
    prime[1] = False
    result = []
    for i in range(2, n+1):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False
    for i, item in enumerate(prime):
        if item:
            result.append(i)
    return result

