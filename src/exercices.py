import numpy as np
import pandas as pd


def ex_1() -> pd.DataFrame:
    """
    Mettre les donnees contenues dans data/id.npy et data/height.npy sous forme de dataframe.
    """
    id = np.load('../data/id.npy')
    heights = np.load('../data/height.npy')
    return pd.DataFrame(data= {'id': id, 'heights': heights})


def ex_2() -> None:
    """
    Joindre au dataframe de l’exercice 1 les donnees contenues dansle fichier data/nom.csv
    en supprimant les lignes ayant des valeurs nulles. Exportez ensuite le dataframe
    obtenu dans un fichier output/data.csv.
    """
    df = pd.read_csv('../data/nom.csv')
    df2 = df.join(ex_1().set_index('id'), on='id')
    df2.dropna(inplace=True)
    df2.to_csv('../output/data.csv')

