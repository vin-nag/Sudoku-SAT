import numpy as np
import itertools as it

class Sudoku:
    """
    A class that represents a Sudoku board
    The board is stored internally as a numpy array
    Zeroes preresent blank spaces
    """

    def __init__(self, degree, matrix=None):
        self.degree = degree
        if matrix is None:
            self.matrix = np.zeros((degree, degree), dtype='int')
        else:
            self.matrix = matrix

    @property
    def rows(self):
        n = 0
        while n < self.degree:
            yield self.matrix[n]
            n += 1

    @property
    def columns(self):
        n = 0
        while n < self.degree:
            yield self.matrix[:, n]
            n += 1

    @property
    def squares(self):
        square = int(np.sqrt(self.degree))
        for i in range(square):
            for j in range(square):
                yield self.matrix[i * square:i * square + square, j * square:j * square + square]

    def num_to_let(num):
        return chr(ord('a') + num - 1)

    def cnf_output(self):
        output = ""
        for i in range(self.degree):
            for j in range(self.degree):
                num = self.matrix[i][j]
                if num == 0: continue
                output += "{}{}{} 0".format(i, j, num)
                output += '\n'
        return output

    def randomize_board(self, num_cells):
        for n in range(num_cells):
            self._draw_random_number()
        return

    def _draw_random_number(self):
        for n in range(10000):  # in case of timeout
            x = np.random.randint(0, self.degree)  # high exclusive
            y = np.random.randint(0, self.degree)
            if self.matrix[x][y] != 0:
                continue
            self.matrix[x][y] = np.random.randint(1, self.degree + 1)
            break
        else:
            raise Exception("Max exceeded")