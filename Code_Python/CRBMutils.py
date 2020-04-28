"""
Courte description de a fonction

Parameters
----------
arg1 : type
    description de l'arg1
arg2 : type
    description de l'arg2
arg3 : type
    description de l'arg3

Returns
-------
type
    description de la valeur 1 retournée
type
    description de la valeur 2 retournée
"""

import numpy as np

def training_set_creator(*args):
    """
    Create list of all points in n-dimensional grid.

    Parameters
    ----------
    args : list
        list of 3-tuples (start, end, num).

    Returns
    -------
    list
        list of n-tuples which points in the n-dimensional grid.
    """
    linspace_args = (np.linspace(*arg) for arg in args)
    
    meshes = np.meshgrid(*linspace_args)
    dimensions = map(np.ravel, meshes)
    tuples = zip(*dimensions)
    
    return list(tuples)


