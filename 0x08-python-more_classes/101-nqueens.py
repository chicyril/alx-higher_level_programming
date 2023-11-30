#!/usr/bin/python3
"""This module contain a Backtracking Algorithm for solving
the n-queen problem.
"""
import sys


def creeate_board(n):
    """Create an n*n size chess board and initialize all
    positions to zero to indicate no piece is placed yet.

    Args:
        n(int): size of the board.
    """
    if type(n) is not int:
        raise TypeError('n required type: int')

    board = [[0 for col in range(n)] for row in range(n)]
    return board


def place_nqueens(board, n, col, ldiag, rdiag, check_row, solutions):
    """Place n non-attacking queens on the board.

    Args:
        board(list): list of list representation of a chess board.
        n(int): size of the board- n*n.
        col:
            index of current column while recursively placing queens.
            set to 1 if a queen can be placed safely: i.e:
            ldiag[row - col + n -1] = 0, and rdiag[row + col] = 0 and
            check_row[i] = 0, for i in range(n).
        ldiag(list):
            A list of size (atleast) 2*(n-1), set to all zero (all cells = 0).
            Its indexes, by the property of diagonal of matrices represent
            the "left-diagonals" of any position on the board: pos(row, col),
            by ``ldiag[row - col + n - 1]``. If a queen can be safely
            placed in any position on the board, the value of `ldiag`
            for this position should be set to 1, else 0.
        rdiag(list):
            A list of size 2*(n-1) like ldiag. Represints the "right-diagonals"
            of any position on the chess board by ``rdiag[row + col]``.
            Should be set to 1 if ldiag is set to 1.
        check_row(list):
            A list of size n (min). Represent checked rows of the chess board.
            For any `col`, if a queen can be placed, set check_row[row] = 1,
            for row in range(n).
        solutions(list):
            A list containg all the possible solutions. i.e, coordinates of
            different possible configuration of the solution.

    Return:
        bool: True if queens were placed successfully, else False.
    """
    if (type(board) is not list or
        any(type(board[i]) is not list for i in range(len(board))) or
       any(len(board[i]) != len(board[0]) for i in range(len(board)))):

        raise TypeError("Invalid Board: Require- list of list of size n * n.")
    if type(n) is not int or n < 4:
        raise TypeError('n must be int, and greater or equals 4.')
    if type(col) is not int or col < 0:
        raise TypeError('col must be int, and not less than 0')
    if type(ldiag) is not list or len(ldiag) < 2 * (n - 1):
        raise Exception("ldiag must be list of min. size 2*(n-1)")
    if type(rdiag) is not list or len(rdiag) < 2 * (n - 1):
        raise Exception('rdiag must be list of min. size 2*(n-1)')
    if type(check_row) is not list or len(check_row) < n:
        raise TypeError('check_row must be a list of min size n.')
    if type(solutions) is not list:
        raise TypeError('solutions must be a list.')

    for row in range(n):
        if col >= n:
            solutions.append([[row, col] for row in range(n)
                              for col in range(n) if board[row][col]])
            return False

        if ((ldiag[row - col + n - 1] != 1) and (rdiag[row + col] != 1)
           and (check_row[row] != 1)):

            board[row][col] = 1
            ldiag[row - col + n - 1] = rdiag[row + col] = check_row[row] = 1

            if place_nqueens(board, n, col + 1, ldiag,
                             rdiag, check_row, solutions):
                return True

            board[row][col] = 0
            ldiag[row - col + n - 1] = rdiag[row + col] = check_row[row] = 0

    return False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    n = int(sys.argv[1])
    board = creeate_board(n)
    ldiag = [0] * (2 * n)
    rdiag = [0] * (2 * n)
    check_row = [0] * (2 * n)
    solutions = []
    place_nqueens(board, n, 0, ldiag, rdiag, check_row, solutions)
    for solution in solutions:
        print(solution)
