# Sudoku as a SAT Problem #
## Bishop, Robert; Graves, Caleb; and Nagisetty, Vineel ##
<center> <img src="https://github.com/vin-nag/Sudoku-SAT/blob/master/Results/sudoku.png" alt="Unsolved Sudoku Grid" width="300px"/> </center>

## Table of Contents
* Introduction
* Usage
* Report

## Introduction
Sudoku is a popular number game played all over the world. In this report, we generate different random instances of varying sized Sudoku boards, reduce to solve using a SAT solver, consider the chance a randomly generated Sudoku board is satisfiable, and build our own Sudoku solver. This report is created for the course COMP 6902.

## Usage
You are free to clone, run and modify this file as you see fit. 

### Source Code
The model of the project is found in the `/Model/` directory and run using the main.py file. 

### Reproduce Results
The various experiments are found in the `/Experiments/` directory as Jupyter Notebook files. 

Please note that you would need to install [minisat solver](http://minisat.se/ "minisat") to run these files. If you wish to use any of the many other [SAT solvers](http://www.satcompetition.org/) that take in a DIMACS formatted file as input, you can change the bash command to suit that solver. 

## Report
The final report for this project is found [here](https://github.com/vin-nag/Sudoku-SAT/blob/master/WriteUps/6902_Report.pdf).

