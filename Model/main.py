# Import Generation and Reduction programs and other necessary programs for the Solver
from generation import Generator
from reduction import Reducer
import subprocess
import tempfile

# Declare variables
BOARD_SIZE = int(input("Enter the size of the Sudoku Board: "))  # size of the Sudoku board
K_VALUE = int(input("Enter the number of random values to generate: ")) # number of random values generated
PATH_NAME = 'output' # name of the file to store generated board

# Generate a random Sudoku board using Generation file
generator = Generator(PATH_NAME, BOARD_SIZE, K_VALUE)
generator.generate()

# Pass this file name and reduce to CNF using Reduction file
reducer = Reducer(PATH_NAME)
reducer.create_cnf_file()

# Create a Solver to test if the CNF file is Satisfiable or Unsatisfiable.
# Note that you need minisat on your computer to run this
bashCommand = 'minisat %s %s' # command to run on the terminal

# Our temporary output file
output_file = tempfile.NamedTemporaryFile()

# Call the bash terminal
subprocess.call(bashCommand % (PATH_NAME+".CNF", output_file.name), shell=True, stdout = subprocess.PIPE)

# Print result
result = output_file.read().decode("utf-8")

# Check if unsat
if result[0] == "U":
    print("This board has no solution")

else:
    print("This board has a solution: ")
    generator.print_solution([int(x) for x in result.split(' ') if x.isdigit()])
