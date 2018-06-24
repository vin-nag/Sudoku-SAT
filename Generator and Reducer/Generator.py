from sudoku import Sudoku
import pickle


class Generator2:
    """
    A class that generates random instances of our sudoku board problem.
    It takes in a size, and random_numbers value and generates a list based on this.
    """

    def __init__(self, size=9, k_value=13, path='output'):
        self.size = size
        self.k_value = k_value
        self.board = Sudoku(self.size)
        self.path = path

    def generate(self):
        self.board.randomize_board(self.k_value)
        result = self.board.regular_output()
        print(result)

        with open(self.path, 'wb') as fp:
            pickle.dump(result, fp)

    def print_board(self, result):
        for row in range(self.size):
            print(" ")
            for column in range (self.size):
                if row in result[:][:][0] and column in result[:][:][1]:
                    print(result[:][:][:][2], end= " ")
                else:
                    print("x", end= " ")

generate = Generator2()
generate.generate()

