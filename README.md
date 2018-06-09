<h1><center> COMP 6902 Project: Sudoku SAT Solver </h1></center>
<h2><center> Bishop, Robert; Graves, Caleb; and Nagisetty, Vineel </h2></center>

### Problem Definition ###

__Sudoku Verifier:__

*Instance:* An $n^2$ by $n^2$ Sudoku grid, filled with an arbitrary amount of numbers $\in [1,n]$, where $n \in N \setminus \{0\}$

*Accept:* if the Sudoku grid has a solution. A Sudoku grid is said to have a solution if for all rows, columns and nxn sub-grids, the Sudoku grid contains each of the n possible numbers. 

A typical Sudoku grid is 9x9 (or $3^2$ x $3^2$), but we have made our problem an nxn to allow for other sizes of instances of the problem.
