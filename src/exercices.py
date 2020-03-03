import numpy as np
from typing import Callable
import matplotlib.pyplot as plt


def ex_1(x_min, x_max, f: Callable) -> None:
    """
    Ecrire une fonction (informatique) affichant une fonction (mathématique) sur l’interval [xmin,xmax]
    """
    x = np.linspace(x_min, x_max, 1001)
    plt.plot(x, f(x))
    plt.show()


def ex_2(mu: float, sigma: float, n: int) -> None:
    """
    Ecrire une fonction qui affiche l’histogramme d’une simulation d’une loi normale de moyenne mu et d’ecart-type sigma comportant nbpoints.

    :param mu: Moyenne de la distribution
    :param sigma: Ecart-type de la distribution
    """
    x = mu + sigma * np.random.randn(n)
    plt.hist(x)
    plt.show()


def ex_3() -> None:
    """
    Affichez sous forme d’histogramme avec incertitudes les données contenues  dans  les  fichiers
    data/meanscore.npy,  data/menheight.npy  et  data/stdscore.npy.
    """
    # Load data
    mean = np.load('../data/mean_score.npy')
    men_height = np.load('../data/men_height.npy')
    std_score = np.load('../data/std_score.npy')

    # Create figure
    fig, ax = plt.subplots()
    ax.bar(men_height, mean, 0.04, yerr=std_score)
    ax.set_title('Score obtained')
    ax.set_xlabel('Men height')
    ax.set_ylabel('Score')
    fig.tight_layout()
    plt.show()

