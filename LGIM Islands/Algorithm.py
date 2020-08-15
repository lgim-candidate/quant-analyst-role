

from collections import deque
import numpy as np

class Algorithm:
    def __init__(self, mat):
        self.matrix = mat
        self.adjacent_rows = [0, 0, -1, 1]
        self.adjacent_cols = [-1, 1, 0, 0]
        self. count_islands = 0
        self.isVisited = [[False for x in range(self.ncol)] for y in range(self.nrow)]

    @property
    def ncol(self):
        try:
            return len(self.matrix[0])
        except:
            return 0

    @property
    def nrow(self):
        try:
            return len(self.matrix)
        except:
            return 0


    def ValidateInputs(self):
        if self.matrix is None :
            raise Exception("Incorrect inputs. 2 dimensional matrix required")

        if len(np.shape(self.matrix)) != 2:
            raise Exception("Incorrect inputs. 2 dimensional matrix required")

        inputs = set(self.matrix.flatten())
        if inputs != set([0, 1]):
            raise Exception("Incorrect inputs. Only 0s and 1s required!")

    def RunSearch(self):
        for i in range(self.nrow):
            for j in range(self.ncol):
                if self.matrix[i][j] == 1 and self.isVisited[i][j] == False:
                    self.count_islands = self.count_islands + 1
                    q = deque()
                    q.append((i, j))
                    self.BFS(i, j, q)
        return self.count_islands

    def BFS(self, i, j, q):
        self.isVisited[i][j] = True

        while len(q) > 0:
            x, y = q.pop()
            for k in range(4):
                if self.AdjascentCellIsUsable(x + self.adjacent_rows[k], y + self.adjacent_cols[k]):
                    self.isVisited[x + self.adjacent_rows[k]][y + self.adjacent_cols[k]] = True
                    q.append((x + self.adjacent_rows[k], y + self.adjacent_cols[k]))

    def AdjascentCellIsUsable(self, i, j):
        if i >= 0 and i < len(self.matrix) and j >= 0 and j < len(self.matrix[0]) and self.matrix[i][j] == 1 and not self.isVisited[i][j] :
            return True
        return False