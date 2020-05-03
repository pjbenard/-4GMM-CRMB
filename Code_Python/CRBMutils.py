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


class Arrays():
    def HeatEquation(self, n):
        N_diff = 2**n
        
        f_diff = np.zeros(N_diff+2)
        f_diff[0] = 1

        #construction des matrices A en format sparse
        tab_A_0 = [np.repeat([1,0],[N_diff//2,N_diff//2+1],0),
                   np.repeat([0,-2,-1,0],[1,N_diff//2-1,1,N_diff//2+1],0),
                   np.repeat([0,1,0],[1,N_diff//2-1,N_diff//2+1],0)]
        
        tab_A_1 = [np.repeat([0,((N_diff+2)**2),0],[N_diff//2,N_diff//2,1],0),
                   np.repeat([1,0,-((N_diff+2)**2),-2*((N_diff+2)**2),1],[1,N_diff//2-1,1,N_diff//2,1],0),
                   np.repeat([0,((N_diff+2)**2)],[N_diff//2,N_diff//2+1],0)]
        
        A_0 = spsp.diags(tab_A_0,[-1,0,1],(N_diff+2,N_diff+2))*((N_diff+2)**2)
        A_1 = spsp.diags(tab_A_1,[-1,0,1],(N_diff+2,N_diff+2))
        
        return 