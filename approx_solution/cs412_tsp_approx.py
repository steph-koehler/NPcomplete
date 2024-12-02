# file for approx solution
#added comment

# something greedy with a graph
    # two for-loops once you have the edges

# not optimal--much faster runtime complexity class



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
# repeat this multiple times while under a certain time limit and return the best greedy approach.

# input will always be a complete graph


# way to prove: known that not-complete graph is np-complete. how can you prove that a complete graph is also np-complete. you can add edges with infinite weight. Not used for this tho 