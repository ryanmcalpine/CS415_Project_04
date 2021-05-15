# CS415 Project 4 - Knapsack
### by Nicholas Keng and Ryan McAlpine

--------------------------------------
### About
This program takes as input from the user an integer 1-8, then uses the associated test data file to solve the 
Knapsack Problem by various means. The resulting values and required number of operations are displayed after 
solving the knapsack problem by using four different methods:
- dynamic programming (traditional)
- dynamic programming (memory function)
- greedy technique using sorting
- greedy technique using max-heap

After the results of processing the selected file are displayed, the program runs through each of the 8 test 
files and graphs the number of operations required for each file's data by each of the four logical approaches.

### Comparison of Algorithms
Viewing the charted results of Tasks 1a and 1b, it is evident that the memory function approach to solving the 
knapsack problem with dynamic programming is far more efficient than using the traditional dynamic programming 
approach. This is because the traditional approach involves calculating an entire table of values, whereas the
memory function approach works backwards from the maximum value, calculating only the steps used along the way.

