
import numpy as np
from Algorithm import Algorithm
import pytest


class TestAlgo:

    def test1(self):
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
        algo = Algorithm(x)
        count_islands = algo.RunSearch()
        assert count_islands == 8

    def test2(self):
        x = np.array([
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]
        ])
        algo = Algorithm(x)
        count_islands = algo.RunSearch()
        assert count_islands == 0

    def test3(self):
        x = np.array([
            [1,1,1],
            [1,1,1],
            [1,1,1],
            [1,1,1]
        ])
        algo = Algorithm(x)
        count_islands = algo.RunSearch()
        assert count_islands == 1

    def test4(self):
        x = np.array([
            [1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [1, 0, 0, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1]
        ])
        algo = Algorithm(x)
        count_islands = algo.RunSearch()
        assert count_islands == 6

    def test5(self):
        x = np.array([
            [1, 1, 1, 1, 0],
            [1, 1, 0, 1, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ])
        algo = Algorithm(x)
        count_islands = algo.RunSearch()
        assert count_islands == 1

    def test6(self):
        x = np.array([
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1]
        ])
        algo = Algorithm(x)
        count_islands = algo.RunSearch()
        assert count_islands == 3

    def test7(self):
        x = np.array([
            [1, 1, 2, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1]
        ])
        algo = Algorithm(x)

        try:
            algo.ValidateInputs()
        except Exception as e:
            assert str(e) == "Incorrect inputs. Only 0s and 1s required!"

    def test8(self):
        x = np.array([
            [1, 1, 1, 0, 0],
            [1, 1, 0, "a", 0],
            [0, 0, 1, "bcd", 0],
            [0, 0, 0, 1, 1]
        ])
        algo = Algorithm(x)

        try:
            algo.ValidateInputs()
        except Exception as e:
            assert str(e) == "Incorrect inputs. Only 0s and 1s required!"

    def test9(self):
        x = [1, 1, 2, 0, 0]
        algo = Algorithm(x)

        try:
            algo.ValidateInputs()
        except Exception as e:
            assert str(e) == "Incorrect inputs. 2 dimensional matrix required"


    def test10(self):
        x = None
        algo = Algorithm(x)

        try:
            algo.ValidateInputs()
        except Exception as e:
            assert str(e) == "Incorrect inputs. 2 dimensional matrix required"

