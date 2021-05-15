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

Similarly, when comparing Tasks 2a and 2b, it is clear that the greedy technique utilizing a max-heap is quite
a bit faster than the greedy technique with the ratio list. This is because the heap does not require sorting
after it is constructed.

### Known Issues
- The optimal value returned by the greedy technique for Task 2a seems to be coming up short, despite using very
similar logic to Task 2b (which appears to be working as intended).
- The number of operations required by Task 2b is shown much lower than it should be. This is because we are still
using a built-in heap function and are unable to account for the number of operations it requires.