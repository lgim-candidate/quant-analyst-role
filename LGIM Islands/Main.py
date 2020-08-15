

import numpy as np
from Algorithm import Algorithm
import sys

def Main():
    try:
        matrix = ReadInputs()
        algo = Algorithm(matrix)
        algo.ValidateInputs()
    except Exception as e:
        print("Error in inputs:" + str(e))
        sys.exit(1)

    count_islands = algo.RunSearch()
    print("Number of islands is: " + str(count_islands))
    sys.exit(0)

def ReadInputs():
    x = np.array([
        [0,0,0,1,1,0,0,1,1,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,1,0,0],
        [1,0,0,0,0,0,1,1,0,0],
        [0,1,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,1,1,0,0,1,1],
        [0,0,0,1,0,0,0,0,0,0]
    ])

    return(x)

if __name__ == '__main__':
    Main()