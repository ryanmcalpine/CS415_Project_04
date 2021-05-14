# by Nicholas Keng and Ryan McAlpine
from __future__ import division

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


if __name__ == "__main__":
    main()






