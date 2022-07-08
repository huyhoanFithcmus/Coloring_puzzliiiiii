# Coloring_puzzliiiiii

## PROJECT 2: Coloring Puzzle

### You are asked to build a coloring puzzle solver by using the first order logic to CNF as described below:
* Given a matrix of size 𝑚×𝑛, where each cell will be a non-negative integer or zero (empty cell). Each cell is considered to be adjacent to itself and 8 surrounding cells.
* Your puzzle needs to color all the cells of the matrix with either blue or red, so that thenumber inside each cell corresponds to the number of blue squares adjacent to that cell (see Figure 1)
* Figure 1 An example of input matrix (left) and output matrix (right)

### In order to solve this problem, you can consider some steps:
1. A logical variable is assigned to each cell of the matrix (If the logical variable of
that cell is True, it will be colored blue, otherwise it will be red)
2. (Report) Write constraints for cells containing numbers to obtain a set of
constraint clauses in CNF (note that you need to remove duplicate clauses)
3. (Implement) Generate CNFs automatically.
4. (Implement) Using the pysat library to find the value for each variable and
infer the result.
5. (Implement) Apply A*, students asked to design the application with the
interface as shown that allows users to browse the input file as well as
enter the delay time for each step (default is 0.5s). See Figure 2.

### REQUIREMENTS:
6. (Implement) Program brute-force and backtracking algorithm to compare
their speed (by measuring running time which is how long it takes for a
computer to perform a specific task) and their performance with A* .
Figure 2 A Sample GUI for coloring puzzle
o When the user presses the Start button, runs the A* algorithm, at each step,
the state of the current State is displayed on the form, the step order and the
current State's heuristic value are also displayed on the form.
o Students can use Python's tkinter library to create GUI
