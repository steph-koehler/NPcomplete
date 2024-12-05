# file for approx solution
# not optimal--much faster runtime complexity class

# something greedy with a graph
    # two for-loops once you have the edges



# Develop Python code that provides a reasonable approximation of the solution. 
# Your approximation must run in polynomial time and process large problems (n > 1000) 
# quickly. Some popular strategies are:

# Make greedy local choices, breaking ties randomly
# utilize randomness coupled with an anytime algorithm

# Your program must execute without arguments (so that it works on gradescope), 
# but you can incorporate optional command line arguments to augment the function 
# of your program (for example, output wall clock timings or override the runtime for 
# an anytime approach).


# start at random nodes and run a greedy approach. 
# repeat this multiple times while under a certain time limit and return the best greedy approach?

# input will always be a complete graph


# way to prove: known that not-complete graph is np-complete. how can you prove that a complete graph is also np-complete. you can add edges with infinite weight. Not used for this tho 

# Ask:
# is the difference that i repeat multiple times using a random starting point each time and select the best
# and macy runs it once using a given starting node?


# dont use 

# start at vert a and end at a, 

# use iterative improvement. make small changes at a time. just see if making random changes make the cost better. there are k^2 swaps.
# drives down to some minimum value. 
# pick a set amount of time that we will be runnign this over. Drop enough random starts.


# use simulated annealing
# How it works:
# Start with a random solution (tour) and iteratively make small random modifications.
# If a new solution has a shorter path, accept it.
# If it's worse, accept it with a probability that decreases over time.
# Why it works:
# It balances exploration (finding new paths) and exploitation (improving on known paths).
# Key Parameters:
# Initial temperature
# Cooling schedule (how the probability of accepting worse solutions decreases over iterations).
import random
import sys
import time


def random_tour(graph, vertices):  # O(n)
    tour = list(range(vertices))
    random.shuffle(tour)  # shuffles the vertices to get a random order
    tour.append(tour[0])  # back to start

    total_weight = sum(graph[tour[i]][tour[i+1]] for i in range(vertices))
    #print(f"rand: {total_weight}")

    return tour, total_weight


def adjust(tour, graph, weight, vertices):
    if vertices > 500 :
        sample_fraction = 0.2
    elif vertices > 200 :
        sample_fraction = 0.5
    else :
        sample_fraction = 1.0

    best_tour = tour[:]
    best_weight = weight
    # print(f"adjust: {best_weight}")
    improved = True
    n = len(tour)

    while improved:
        improved = False
        # subset of edge pairs
        all_pairs = [(i, j) for i in range(1, n - 2) for j in range(i + 1, n - 1)]
        # print(f"all pairs: {all_pairs}")
        sampled_pairs = random.sample(all_pairs, int(len(all_pairs) * sample_fraction))

        for i, j in sampled_pairs: # runs n or 20% of n times
            new_tour = best_tour[:i] + best_tour[i:j+1][::-1] + best_tour[j+1:]
            new_weight = calculate_tour_weight_incremental(tour, graph, weight, i, j)
            # check if the new tour is better
            if new_weight < best_weight:
                best_tour = new_tour
                best_weight = new_weight
                improved = True

    return best_tour, best_weight


def calculate_tour_weight_incremental(tour, graph, weight, i, j):
    # get rid of old edges
    weight -= graph[tour[i-1]][tour[i]]
    weight -= graph[tour[j]][tour[j+1]]
    # add new edges
    weight += graph[tour[i-1]][tour[j]]
    weight += graph[tour[i]][tour[j+1]]

    return weight


def main():
    data = sys.stdin.read().strip().split("\n")
    vertices, edges = map(int, data[0].strip().split())
    graph = {i: {} for i in range(vertices)}
    vertex_map = {}
    rev_map = {}

    for line in data[1:]:
        u, v, weight = line.strip().split()
        weight = float(weight)
        if u not in vertex_map:
            vertex_map[u] = len(vertex_map)
            rev_map[vertex_map[u]] = u
        if v not in vertex_map:
            vertex_map[v] = len(vertex_map)
            rev_map[vertex_map[v]] = v
        u_idx, v_idx = vertex_map[u], vertex_map[v]
        graph[u_idx][v_idx] = weight
        graph[v_idx][u_idx] = weight

    best_weight = float('inf')
    best_tour = None
    start_time = time.time()
    counter = 0
    # if file is too big to run in 45 seconds, cap it at that time
    while not (time.time() - start_time > 45 or counter > vertices):
        counter += 1
        
        tour, weight = random_tour(graph, vertices)
        tour, weight = adjust(tour, graph, weight, vertices) 
        if weight < best_weight:
            best_weight = weight
            best_tour = tour

    print(f"{best_weight:.4f}")
    mapped_tour = [rev_map[vertex] for vertex in best_tour]
    print(' '.join(mapped_tour))


if __name__ == '__main__':
    main()
