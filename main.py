# by Nicholas Keng and Ryan McAlpine

from __future__ import division
import matplotlib.pyplot as plt

# global operation counter variables
# for use in graphing for task 3
oc1a = []
oc1b = []
oc2a = []
oc2b = []

# Quick sort will take as argument a list
# with a list of values to sort in index 0
# and the operation counter variable in index 1
def quick_sort(values):
    struct = [values, 0, 0]
    quick_sort_r(struct, 0, len(struct[0]) - 1)
    return struct
def quick_sort_r( struct, low, high ):
    if low < high:
        struct = partition(struct, low, high)
        quick_sort_r(struct, low, struct[2] - 1)
        quick_sort_r(struct, struct[2] + 1, high)
    return struct
def partition(struct, low, high):
    struct[2] = low-1
    pivot = struct[0][high]
    for j in range(low, high):
        if struct[0][j] <= pivot:
            struct[2] += 1
            struct[0][struct[2]], struct[0][j] = struct[0][j], struct[0][struct[2]]
            struct[1] += 1
    struct[0][struct[2]+1], struct[0][high] = struct[0][high], struct[0][struct[2]+1]
    struct[1] += 1
    struct[2] += 1
    return struct

def knapsack_Greedy(cap, weights, values) :

    ratios = []
    #w = weights.read().splitlines()
    #weights = []
    #v = values.read().splitlines()
    #values = []

    num_weights = len(weights)
    for i in range(num_weights):
        r = int(values[i]) / int(weights[i])
        ratios.append(r)

    print(ratios)
    return

def main():

    # Read the Capacity file and make it equal to cap
    file_cap = open('./KnapsackTestData/p01_c.txt', 'r')
    cap = file_cap.readlines()

    # Read the weight file
    file_weight = open('./KnapsackTestData/p01_w.txt', 'r')
    w = file_weight.readlines()

    # Read the value file
    file_value = open('./KnapsackTestData/p01_v.txt', 'r')
    v = file_value.readlines()

    knapsack_Greedy(cap, w, v)


def dynamic_traditional( capacity, weights, values, num_items, is_printing ):
    # Initialize operation counter
    num_ops = 0

    # Initialize a 2D array for our table with 0's
    table = [[0 for x in range(capacity+1)] for x in range(num_items + 1)]
    for i in range(num_items + 1):
        for j in range(capacity+1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif weights[i-1] <= j:
                table[i][j] = max( (values[i-1] + table[i-1][j-weights[i-1]]), table[i-1][j] )
            else:
                table[i][j] = table[i-1][j]
            num_ops += 1

    if is_printing == True:
        print("\n-------- Task 1a --------")
        # Print maximum value, stored in last index of table
        print(f"Optimal value: F({num_items}, {capacity}) = {table[num_items][capacity]} (found in {num_ops} operations.)")

        # Find all optimal values and print them as well
        print("Optimal subset: ")
        #for i in range(num_items + 1):
        #    for j in range(capacity + 1):
        #        if i == 0:
        #            i += 1
        #        if j == 0:
        #            j += 1
        #        if table[i][j] != table[i-1][j]:    # and table[i][j] != table[i][j-1]:
        #            print(f"F({i}, {j}) = {table[i][j]}")
        #        num_ops += 1
        s = capacity
        set_str = ""
        for i in reversed(range(num_items + 1)):
            if i != 0:
                if table[i][s] != table[i - 1][s]:
                    if s != capacity:
                        set_str = "\n" + set_str
                    set_str = f"F({i}, {s}) = {table[i][s]}" + set_str
                    s -= weights[i - 1]
                    num_ops += 1
        print(set_str)
        print(f"(Subset found in {num_ops} operations.)")
    else:
        oc1a.append(num_ops)
    return

def dynamic_memory( capacity, weights, values, num_items, is_printing):
    # This function helps get the logic for task 1b started and prints the results

    # Initialize operation counter
    num_ops = 0

    # Initialize a 2D array for our table with -1's
    table = [[-1 for x in range(capacity + 1)] for x in range(num_items + 1)]
    # Top row and left column are 0's
    for i in range(num_items + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                table[i][j] = 0

    # Package our table and operation counter for passing between recursive function
    dpm_struct = [table, num_ops]
    # Now recursive function can handle logic of building table
    dpm_struct = dynamic_memory_recursive(dpm_struct, capacity, weights, values, num_items)

    if is_printing == True:
        print("\n-------- Task 1b --------")
        # Print maximum value, stored in last index of table
        print(f"Optimal value: F({num_items}, {capacity}) = {dpm_struct[0][num_items][capacity]} (found in {dpm_struct[1]} operations.)")

        # Find all optimal values and print them as well
        print("Optimal subset: ")
        set_str = ""
        s = capacity
        for i in reversed(range(num_items+1)):
            if i != 0:
                if dpm_struct[0][i][s] != dpm_struct[0][i-1][s]:
                    if s != capacity:
                        set_str = "\n" + set_str
                    set_str = f"F({i}, {s}) = {dpm_struct[0][i][s]}" + set_str
                    s -= weights[i-1]
                    dpm_struct[1] += 1
        print(set_str)
        print(f"(Subset found in {dpm_struct[1]} operations.)")
    else:
        oc1b.append(dpm_struct[1])
    return

def dynamic_memory_recursive( dpm_struct, capacity, weights, values, num_items ):
    if dpm_struct[0][num_items][capacity] < 0:
        value = 0
        if capacity < weights[num_items-1]:
            value = dynamic_memory_recursive(dpm_struct, capacity, weights, values, num_items - 1)[0][num_items-1][capacity]
        else:
            #a = dynamic_memory_recursive(dpm_struct, capacity, weights, values, num_items - 1)[0][num_items - 1][capacity]
            #z = dynamic_memory_recursive(dpm_struct, capacity - weights[num_items - 1], weights, values, num_items - 1)[0][num_items - 1][capacity - weights[num_items - 1]]
            #b = (values[num_items - 1] + z)
            #value = max(a, b)
            value = max(dynamic_memory_recursive(dpm_struct, capacity, weights, values, num_items - 1)[0][num_items - 1][capacity], (values[num_items - 1] + dynamic_memory_recursive(dpm_struct, capacity - weights[num_items - 1], weights, values, num_items - 1)[0][num_items - 1][capacity - weights[num_items - 1]]))
        dpm_struct[0][num_items][capacity] = value
        dpm_struct[1] += 1

    return dpm_struct

def run_tests( i, is_printing ):
    if str(i).isnumeric() == False:
        print("Invalid input. Enter an integer 0-10")
        return

    if len(str(i)) == 1:
        i = str('0') + str(i)

    if int(i) < 0 or int(i) > 10:
        print("Invalid input. Enter an integer 0-10")
        return

    fc_str = 'KnapsackTestData/p' + i + '_c.txt'
    fw_str = 'KnapsackTestData/p' + i + '_w.txt'
    fv_str = 'KnapsackTestData/p' + i + '_v.txt'

    fc = open(fc_str, 'r')
    fw = open(fw_str, 'r')
    fv = open(fv_str, 'r')

    c = int(fc.read())
    w = []
    for x in fw:
        w.append(int(x))
    v = []
    for x in fv:
        v.append(int(x))
    n = len(w)

    dynamic_traditional(c, w, v, n, is_printing)
    dynamic_memory(c, w, v, n, is_printing)
    knapsack_Greedy(c, w, v)

    return

if __name__ == "__main__":
    # vals = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    # struct = quick_sort(vals)
    # print(vals) #sorted
    # print(struct[0]) #same as print(vals)
    # print(struct[1]) #number of operations
    while True:
        inp = input('\nEnter the number of the test file you would like to use: ')
        run_tests(inp, True)

        print("Calculating values for graph...")
        for i in range(8):
            run_tests(i, False)
        print("Plotting data...")
        fig = plt.figure()
        # Task 1a
        ax1 = fig.add_subplot(2, 2, 1)
        ax1.scatter( range(8), oc1a, label="Task 1a" )
        ax1.set_xlabel('Test Case #')
        ax1.set_ylabel('Number of Operations')
        # Task 1b
        ax2 = fig.add_subplot(2, 2, 2)
        ax2.scatter(range(8), oc1b, label="Task 1a")
        ax2.set_xlabel('Test Case #')
        ax2.set_ylabel('Number of Operations')
        print("Done.")

        plt.show()
