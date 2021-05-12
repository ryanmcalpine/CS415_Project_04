# by Nicholas Keng and Ryan McAlpine

def dynamic_traditional( capacity, weights, values, num_items ):
    print("\n-------- Task 1a --------")

    # Initialize operation counter
    num_ops = 0

    # Initialize a 2D array for our table
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
    for i in range(num_items + 1):
        for j in range(capacity + 1):
            if i == 0:
                i += 1
            if j == 0:
                j += 1
            if table[i][j] != table[i-1][j] and table[i][j] != table[i][j-1]:
                print(f"F({i}, {j}) = {table[i][j]}")
            num_ops += 1
    print(f"(Subset found in {num_ops} operations.)\n")

    return

if __name__ == "__main__":
    dynamic_traditional(50, [10, 20, 30], [60, 100, 120], 3)