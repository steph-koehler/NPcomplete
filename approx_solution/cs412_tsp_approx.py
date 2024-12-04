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
import math
import sys


def rand_tour(graph, rev_map) :  # generate the first random tour
    vertices = list(graph)
    start = random.choice(vertices)
    # print(start)
    tour = [start]
    # print(f"Tour: {tour}")
    total_weight = 0
    current = start

    while len(tour) < len(graph):
        neighbors = list(graph[current].items())
        random_edge = random.choice(neighbors)
        next, weight = random_edge
        if next not in tour:
            tour.append(next)
            total_weight += weight
            current = next

    # return to the starting node to complete the cycle
    total_weight += graph[current][start]
    tour.append(start)
    # print(f"Tour: {tour}")
    mapped_tour = [rev_map[vertex] for vertex in tour]  # Map numeric indices to vertex names
    # print(f"Mapped Tour: {mapped_tour}")

    return tour, total_weight

    # u = random starting node
    # total weight = 0
    # for loop (index up to number of edges (+1 maybe))  # runs n times
        # add u to the tour
        # select a random edge leaving u (random pick from map at u)
        # add that edge weight to the totalweight
        # u = v
    #return tour, totalweight


def adjust(tour, graph, weight, vertices):
    # Perform edge swaps (2-opt optimization) to find a better tour
    best_tour = tour[:]
    best_weight = weight
    improved = True

    while improved:
        improved = False
        for i in range(1, len(tour) - 2):  # Avoid the start and end points
            for j in range(i + 1, len(tour) - 1):
                # Generate a new tour by reversing the segment between edges i and j
                new_tour = best_tour[:i] + best_tour[i:j+1][::-1] + best_tour[j+1:]
                new_weight = calculate_tour_weight(new_tour, graph)

                # Check if the new tour is better
                if new_weight < best_weight:
                    best_tour = new_tour
                    best_weight = new_weight
                    improved = True

    return best_tour, best_weight




def calculate_tour_weight(tour, graph):
    weight = 0
    # print(f"Tour: {tour}")
    # print(f"Graph: {graph}")
    for i in range(len(tour) - 1):
        u = tour[i]
        v = tour[i + 1]
        if u not in graph or v not in graph[u]:
            raise ValueError(f"Invalid edge ({u}, {v}) in the tour.")
        weight += graph[u][v]
    return weight


def main():  # change this so that the input is in a file.
    data = sys.stdin.read().strip().split("\n")
    vertices, edges = map(int, data[0].strip().split())  # First line: vertices and edges
    graph = {i: {} for i in range(vertices)}
    vertex_map = {}
    rev_map = {}

    #file_name = 'approx_solution/test2.txt'  # File to read inputs from

    #with open(file_name, 'r') as file:
        #vertices, edges = map(int, file.readline().strip().split())  # First line: vertices and edges
        #graph = {i: {} for i in range(vertices)}
        #vertex_map = {}
        #rev_map = {}

        # vertices, edges = map(int, input().strip().split())  # assigns ints to vertices and edges
        # graph = {i: {} for i in range(vertices)}
        # vertex_map = {} 
        # rev_map = {}
    for line in data[1:]:  # for every edge
        u, v, weight = line.strip().split()  # from node, to node, edge weight
        # print(f"u: {u}")
        # print(f"v: {v}")
        # print(f"weight: {weight}")
        weight = float(weight)
        if u not in vertex_map:
            vertex_map[u] = len(vertex_map)  # maps from node, index of the from node
            rev_map[vertex_map[u]] = u  # reversed map
        if v not in vertex_map: 
            vertex_map[v] = len(vertex_map) # maps to node, index of the to node
            rev_map[vertex_map[v]] = v # reversed map
        u_idx, v_idx = vertex_map[u], vertex_map[v]
        graph[u_idx][v_idx] = weight  # adds the weights to the graph. (makes the graph basically)
        graph[v_idx][u_idx] = weight  # weights in both directions. seen in adjacency list
    
    # print(f"Graph: {graph}")
    # print(f"vertex_map: {vertex_map}")
    # print(f"rev_map: {rev_map}")

    best_weight = float('inf')  # looking for lowest weight
    best_tour = None  # change from None obviously.

    start_graph = 10  # might need to change value (def change the name)
    if start_graph > vertices :
        start_graph = vertices
    for _ in range(start_graph) :
        tour, weight = rand_tour(graph, rev_map)  # generate a random tour
        tour, weight = adjust(tour, graph, weight, vertices)  # tour is now the best tour after the adjustments.
        if weight < best_weight : 
            best_weight = weight
            best_tour = tour  # the best adjusted tour with every random start


    print(f"{best_weight:.4f}")
    # print the best tour
    # print(f"Tour: {best_tour}")
    mapped_tour = [rev_map[vertex] for vertex in best_tour]  # Map numeric indices to vertex names
    # print(f"Mapped Tour: {mapped_tour}")
    print(' '.join(mapped_tour))


if __name__ == '__main__':
    main()