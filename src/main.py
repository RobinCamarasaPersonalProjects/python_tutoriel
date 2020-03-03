from exercices import *
import numpy as np


if __name__ == '__main__':
    exercices = [
        ex_1, ex_2, ex_3
    ]
    arguments = [
        (lambda x: x**2,),
        (0.5, 0.25, 30),
        None
    ]

    for exercice, args in zip(
        exercices, arguments
    ):
        print("\n\n### {} ###\n".format(exercice.__name__.upper()))
        if args is None:
            input = "None"
            output = exercice()
        else:
            input = args
            output = exercice(*args)
        print(
            '{}\nInput :\n{}\nOutput :\n{}'.format(
                exercice.__doc__,
                input,
                output
            )
        )

