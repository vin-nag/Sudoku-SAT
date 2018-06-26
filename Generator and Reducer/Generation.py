from sudoku import Sudoku
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

    def generate(self):
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

        print("Generated Board: ")
        self.print_board()

        # Store the generated values using pickle
        with open(self.path, 'wb') as fp:
            pickle.dump(result, fp)
        return


    def print_board(self):
        """
        This method prints out the Sudoku board in a readable format
        :return: None
        """
        row = [str(x) for x in range(1,self.size+1)]

        # this part prints out the board in a human readable format
        for i,r in enumerate(row):
            if i in [3,6]:
                print('------+-------+------')
            for j,c in enumerate(row):
                if j in [3,6]:
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

