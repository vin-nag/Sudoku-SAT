from sudoku import Sudoku
import math
import pickle

class Generator:
    """
    A class that generates random instances of our sudoku board problem.
    It takes in a size, k_value and path and generates a random sudoku board based on this.
    """

    def __init__(self, path='output', size=9, k_value=13):
        """
        Standard Initializer
        :param path: filename path to store the generated board
        :param size: size of the Sudoku board
        :param k_value: The number of random values to generate
        """
        self.size = size
        self.k_value = k_value
        self.board = Sudoku(self.size)
        self.path = path
        self.d = dict()
        return

    def generate(self, print_board=True, save=True):
        """
        This method generates a random Sudoku board using a method from Sudoku class
        :return: None
        """
        # Generate random Sudoku board
        self.board.randomize_board(self.k_value)

        # record the random values generated in a list
        result = self.board.regular_output()

        # Store the generated values in a dictionary
        for item in result:
            item[0]+=1
            item[1]+=1
            key = str(item[0]) + str(item[1])
            value = str(item[2])
            self.d[key] = value

        if print_board:
            print("Generated Board: ")
            self.print_board()

        # Store the generated values using pickle
        if save:
            with open(self.path, 'wb') as fp:
                pickle.dump(result, fp)
        return


    def print_board(self):
        """
        This method prints out the Sudoku board in a readable format
        :return: None
        """
        row = [str(x) for x in range(1,self.size+1)]
        cutoff = {x for x in range(2,self.size) if x%math.sqrt(self.size)==0}

        line = '-' * int(math.sqrt(self.size)) + '+' + '-'*int(math.sqrt(self.size))

        # this part prints out the board in a human readable format
        for i,r in enumerate(row):
            if i in cutoff:
                print(line*int(math.sqrt(self.size)))
            for j,c in enumerate(row):
                if j in cutoff:
                    print('|',end=" ")
                if r+c in self.d:
                    print (self.d[r + c], end=" ")
                else:
                    print(0, end = " ")
            print(" ")
        return


    def print_solution(self, lst):
        """
        This method prints out the solution of a Sudoku board
        :param lst:
        :return: None
        """
        self.d.clear()

        for item in lst:
            temp = str(item)
            key = temp[0] + temp[1]
            value = temp[2]
            self.d[key] = value

        self.print_board()
        return

