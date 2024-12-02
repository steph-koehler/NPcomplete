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


def gen_rand(graph, map) :
    #get random starting value from the map
    #pick random edges
    pass


def main():  # change this so that the input is in a file.
    vertices, edges = map(int, input().strip().split())  # assigns ints to vertices and edges
    graph = {i: {} for i in range(vertices)}
    vertex_map = {} 
    rev_map = {}
    for _ in range(edges):  # for every edge
        u, v, weight = input().strip().split()  # from node, to node, edge weight
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
    
    idk = 100
    for _ in range(idk) :  #dropping the different starting points.
        gen_rand(graph, rev_map) #change this to separate getting random edges and getting random starting values ?

    
if __name__ == '__main__':
    main()