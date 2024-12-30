# 8_Queens_Py
This repository contains a small Python program to practice working with lists and tuples.
# 8 Queens Problem

## Purpose

This repository contains a small Python program to practice working with **lists** and **tuples**. The problem you will solve is the classic **8 Queens puzzle**:

> *Given a placement of 8 queens on an 8×8 chessboard, determine if at least one pair of queens can attack each other. No two queens should be in the same row, column, or diagonal. If at least one pair can attack each other, print “YES”; otherwise, print “NO”.*

## Problem Statement

1. You will be given 8 lines of input, each containing two integers representing the row and column of a queen on a standard chessboard (rows and columns are numbered from 1 to 8).
2. Your goal is to check if any two queens are positioned such that they can attack each other.
3. Specifically, queens should not share:
   - The same row
   - The same column
   - The same diagonal (the absolute difference between rows equals the absolute difference between columns)

If a conflict exists (i.e., at least one pair of queens can attack each other), output **YES**. Otherwise, output **NO**.

## Example Test Cases

Below are some example inputs and the corresponding outputs:

| Test # | Input (Row, Col for each queen)                               | Output |
|-------:|:------------------------------------------------------------- |:------:|
| **1**  | 1 5<br>2 3<br>3 1<br>4 7<br>5 2<br>6 8<br>7 6<br>8 4           | NO     |
| **2**  | 1 7<br>2 4<br>3 2<br>4 8<br>5 6<br>6 1<br>7 3<br>8 5           | NO     |
| **3**  | 1 8<br>2 7<br>3 6<br>4 5<br>5 4<br>6 3<br>7 2<br>8 1           | YES    |
| **4**  | 3 4<br>8 5<br>4 1<br>7 3<br>6 6<br>1 7<br>5 8<br>2 2           | YES    |
| **5**  | 2 5<br>8 4<br>3 7<br>4 1<br>6 8<br>7 6<br>1 2<br>5 3           | NO     |
| ...    | ...                                                           | ...    |
| **14** | 1 7<br>2 1<br>3 2<br>4 3<br>5 4<br>6 6<br>7 8<br>8 5           | YES    |

*(Note: Additional test cases are provided in the problem description. You can copy/paste them to test the program.)*

## How to Run

1. **Clone or download** this repository.
2. Open a terminal or command prompt in the directory containing the script.
3. Run the script (for example, `python check_queens.py`).
4. **Enter 8 lines of input**, each containing two integers (e.g., `1 5`).
5. The program will output **YES** if at least two queens attack each other, or **NO** if they do not.

## Explanation of the Code

### Function: `check_queens_chessboard(x, y)`

The function iterates through all possible pairs of queens to check if any two queens can attack each other. 

#### Key Steps:
1. **Iterate through all pairs of queens:**
   - Use two nested loops: the outer loop (`i`) starts from the first queen, and the inner loop (`j`) checks all queens after `i`.

2. **Check conditions for conflict:**
   - **Same row:** Check if `x[i] == x[j]`
   - **Same column:** Check if `y[i] == y[j]`
   - **Same diagonal:** Check if `abs(x[i] - x[j]) == abs(y[i] - y[j])`

3. **Return the result:**
   - If any condition is met, return `"YES"` immediately (indicating a conflict).
   - If no conflicts are found after all iterations, return `"NO"`.

## Code

Replace the `...` comments below with your logic (as shown in the snippet), ensuring proper indentation.

```python
def check_queens_chessboard(x, y):
    # Loop over all pairs of queens
    for i in range(8):
        for j in range(i + 1, 8):
            # Check if queens share the same row, column, or diagonal
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                return "YES"
    return "NO"

x = []
y = []

# Read in the 8 pairs of coordinates
for inputs in range(8):
    a_list = [int(s) for s in input().split()]  # Use list comprehension to parse input
    x.append(a_list[0])
    y.append(a_list[1])

# Print the result
print(check_queens_chessboard(x, y))
