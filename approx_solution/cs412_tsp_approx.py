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






# same inputs on min spanning tree and then analysis. good for error bounding. 
# Know that answer might not be completely right, but you know how much it can be wrong by
#     may have to create a whole bunch of test cases. 
#     run lower lound and approx solution on a bunch of test cases that the exact solution will not run on.



# add lightest remaining edge that isnt in the mst after it completes. needs enough edges to make full cycle. 
# changes from v-1 to v. look up mst approx for tsp. 
# you add lightest because you dont actually know which one to add and this is a lower bound



# start at random nodes and run a greedy approach. 
# repeat this multiple times while under a certain time limit and return the best greedy approach.