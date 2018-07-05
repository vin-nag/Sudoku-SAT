import pickle
import numpy as np
import itertools as it

class Reducer():
    """
    This class take as an input a name of a file containing an instance of our Sudoku problem and
    produces a file with a CNF formula encoding of this instance in .cnf format.
    """

    def __init__(self, path='output', size=9, k_value=13):
        """
        Standard Initializer
        :param path: path of the file created by our Generator
        :param size: size of the Sudoku board
        :param k_value: number of random values generated
        """
        self.size = size
        self.k_value = k_value
        self.path = path
        self.cnf = ""
        return

    def return_cnf_data(self):

        self.get_Sudoku_cnf_constraints()

        # Update the cnf string with the generated board
        # self.get_generated_data()

        # Update the header value from info generated
        cnf_header = self.create_cnf_header()

        return cnf_header + self.cnf

    def create_cnf_file(self):
        """
        This method creates the cnf file
        :return: None
        """
        # Update the cnf string with all the Sudoku constraints in cnf form
        self.get_Sudoku_cnf_constraints()

        # Update the cnf string with the generated board
        self.get_generated_data()

        # Update the header value from info generated
        cnf_header = self.create_cnf_header()

        # print all values to a .cnf format file
        with open(self.path+'.cnf', 'w') as f:
            f.write(cnf_header)
            f.write(self.cnf)
        return


    def get_generated_data(self):
        """
        This method gets the generated board data and updates to cnf string
        :return: None
        """
        # Get the values of the generated board
        with open(self.path, 'rb') as fp:
            itemlist = pickle.load(fp)

        # update the string
        for item in itemlist:
            self.cnf += (''.join(map(str, item)) + ' 0\n')
        return


    def create_cnf_header(self):
        """
        This method creates a header
        :return: cnf header as a string
        """
        # add info to the comments
        cnf_comment = 'c Sudoku-SAT cnf file by Bishop, Robert; Graves, Caleb; and Nagisetty, Vineel \n'
        cnf_comment += 'c Size of board =' + str(self.size) + " by " + str(self.size) + ' \n'
        cnf_comment += 'c k Value = ' + str(self.k_value) + ' \n'

        # find number of clauses
        clause_count = str.count(self.cnf, "\n")

        var_count = str(self.size) + str(self.size) + str(self.size)
        # add variable number, clause number to problem line
        cnf_p_line = 'p cnf ' + var_count + ' ' + str(clause_count) + '\n'
        return cnf_comment + cnf_p_line


    def get_Sudoku_cnf_constraints(self):
        """
        This method updates the cnf string with all of the Sudoku game constraints
        :return: None
        """
        self.cnf += self.cell_definedness()
        self.cnf += self.cell_uniqueness()
        self.cnf += self.row_definedness()
        self.cnf += self.row_uniqueness()
        self.cnf += self.column_definedness()
        self.cnf += self.column_uniqueness()
        self.cnf += self.block_definedness()
        self.cnf += self.block_uniqueness()
        return


    def cell_definedness(self):
        """
        This method updates the cnf string with the cell definedness constraint
        :return: cell definedness constraint as a string
        """
        line = ""
        for row in range(self.size):
            for column in range(self.size):
                for value in range(self.size):
                    line += "{}{}{} ".format(row+1, column+1, value+1)
                line+= " 0\n"
        return line


    def cell_uniqueness(self):
        """
        This method updates the cnf string with the cell uniqueness constraint
        :return: cell uniqueness constraint as a string
        """
        line = ""
        for row in range(self.size):
            for column in range(self.size):
                for vi, vj in it.combinations(range(self.size), 2):
                    line += "-{}{}{} -{}{}{} 0\n".format(row + 1, column + 1, vi + 1, row + 1, column + 1, vj + 1)
        return line


    def row_definedness(self):
        """
        This method updates the cnf string with the row definedness constraint
        :return: row definedness constraint as a string
        """
        line = ""
        for row in range(self.size):
            for value in range(self.size):
                for column in range(self.size):
                    line += "{}{}{} ".format(row + 1, column + 1, value + 1)
                line += " 0\n"
        return line


    def row_uniqueness(self):
        """
         This method updates the cnf string with the row uniqueness constraint
        :return: row uniqueness constraint as a string
        """
        line = ""
        for row in range(self.size):
            for value in range(self.size):
                for ci, cj in it.combinations(range(self.size), 2):
                    line += "-{}{}{} -{}{}{} 0\n".format(row + 1, ci + 1, value + 1, row + 1, cj + 1, value + 1)
        return line


    def column_definedness(self):
        """
         This method updates the cnf string with the column definedness constraint
        :return: column definedness constraint as a string
        """
        line = ""
        for column in range(self.size):
            for value in range(self.size):
                for row in range(self.size):
                    line += "{}{}{} ".format(row + 1, column + 1, value + 1)
                line += " 0\n"
        return line


    def column_uniqueness(self):
        """
         This method updates the cnf string with the column uniqueness constraint
        :return: column uniqueness constraint as a string
        """
        line = ""
        for column in range(self.size):
            for value in range(self.size):
                for ri, rj in it.combinations(range(self.size), 2):
                    line += "-{}{}{} -{}{}{} 0\n".format(ri + 1, column + 1, value + 1, rj + 1, column + 1, value + 1)
        return line


    def block_definedness(self):
        """
         This method updates the cnf string with the block definedness constraint
        :return: block definedness constraint as a string
        """
        line = ""
        rootn = int(np.sqrt(self.size))
        for roff in range(rootn):
            for coff in range(rootn):
                for value in range(self.size):
                    for row in range(rootn):
                        for column in range(rootn):
                            line += "{}{}{} ".format(roff * rootn + row + 1, coff * rootn + column + 1, value + 1)
                    line += ' 0\n'
        return line


    def block_uniqueness(self):
        """
         This method updates the cnf string with the block uniqueness constraint
        :return: block uniqueness constraint as a string
        """
        line=""
        rootn = int(np.sqrt(self.size))
        for r in range(rootn):
            for c in range(rootn):
                for v in range(self.size):
                    square = []
                    for r1 in range(rootn):
                        for c1 in range(rootn):
                            square.append("{}{}".format(r * rootn + r1 + 1, c * rootn + c1 + 1))
                    for s1, s2 in it.combinations(square, 2):
                        line += "-{}{} -{}{} 0\n".format(s1, v + 1, s2, v + 1)
        return line