import numpy as np


def ex_1() -> np.ndarray:
    """
    En une ligne, creer un tableau de dimension (3, 4, 5).
    """
    return np.arange(3 * 4 * 5).reshape(3, 4, 5)


def ex_2(arr: np.ndarray) -> np.ndarray:
    """
    Creer une fonction qui renvoie les indices d’un tableau dont les valeurs sont paires

    :param arr: Numpy array
    """
    return np.where(arr%2 == 0)


def ex_3(n: int) -> np.ndarray:
    """
    Implémentez le triangle de Pascal.

    :param n: Nombre
    """
    result = np.eye(n+1)
    for i in range(1, n+1):
        result[i, :] = result[i-1, :] + np.concatenate((np.array([0]), result[i-1, :-1]))
    return result


def ex_4(A: np.ndarray, B: np.ndarray):
    """
    Ecrire une fonction de résolution de systèmes linéaires de la forme AX = B.

    :param A: Matrice carrée contenant les paramètres du système
    :param B: Vector colonne contenant les paramètres du système
    """
    return np.dot(np.linalg.inv(A), B)


def ex_5():
    """
    Chargez le fichier data/data.npy mettez l’ensemble de ces valeursau carr ́e sauvegardez le tableau dans le fichier data/datasquared.npy
    """
    arr = np.load('../data/data.npy')
    arr = arr ** 2
    np.save('../data/data_squared.npy', arr)


