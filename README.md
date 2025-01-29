# LU Decomposition Solver (Python)

This Python program solves a system of linear equations using LU decomposition. It takes the coefficients of the equations and their corresponding answers as input from the user, constructs the matrices L (lower triangular) and U (upper triangular), and then calculates the solutions for the variables (x1, x2,..., xn).

## Description

The program implements LU decomposition, a method for factoring a matrix A into the product of a lower triangular matrix L and an upper triangular matrix U.  This decomposition simplifies the process of solving the linear equation system Ax = b. The program first obtains the matrix A (coefficients) and the vector b (answers) from user input. It then calculates the L and U matrices.  After the decomposition, it solves the system in two steps:

1.  **Solve Ly = b for y:**  This step involves forward substitution.
2.  **Solve Ux = y for x:** This step involves backward substitution.

The resulting vector x contains the solutions to the original system of linear equations.

## Build Instructions

This program is written in Python and requires a Python interpreter.  It should work with Python 3.x.  To run the program:

1.  **Save:** Save the code as a `.py` file (e.g., `lu_decomposition.py`).
2.  **Run:** Open a terminal or command prompt, navigate to the directory where you saved the file, and run the program using the command: `python lu_decomposition.py`

## Usage

When you run the program, it will prompt you to enter the following information:

1.  **Number of equations:** The number of linear equations in your system.
2.  **Answers:** The constant value (answer) for each equation.
3.  **Coefficients:** The coefficients of each variable (x1, x2,..., xn) in each equation.

The program will then calculate the solutions and print the values of x1, x2,..., xn.

## Example
