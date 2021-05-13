# by Nicholas Keng and Ryan McAlpine

def dynamic_traditional( capacity, weights, values, num_items ):
    print("\n-------- Task 1a --------")

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
    print(f"(Subset found in {num_ops} operations.)\n")

    return

def dynamic_memory( capacity, weights, values, num_items ):
    # This function helps get the logic for task 1b started and prints the results
    print("\n-------- Task 1b --------")

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
    print(f"(Subset found in {dpm_struct[1]} operations.)\n")

    return


def dynamic_memory_recursive( dpm_struct, capacity, weights, values, num_items ):
    if dpm_struct[0][num_items][capacity] < 0:
        value = 0
        if capacity < weights[num_items-1]:
            value = dynamic_memory_recursive(dpm_struct, capacity, weights, values, num_items - 1)
        else:
            value = max(
                dynamic_memory_recursive(dpm_struct, capacity, weights, values, num_items - 1)[0][num_items - 1][capacity], (values[num_items - 1] + dynamic_memory_recursive(dpm_struct, capacity - weights[num_items - 1], weights, values, num_items - 1)[0][num_items - 1][capacity - weights[num_items - 1]]))
        dpm_struct[0][num_items][capacity] = value
        dpm_struct[1] += 1

    return dpm_struct


if __name__ == "__main__":
    dynamic_traditional(50, [10, 20, 30], [60, 100, 120], 3)
    dynamic_memory(50, [10, 20, 30], [60, 100, 120], 3)