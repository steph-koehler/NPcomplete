# https://www.tutorialspoint.com/data_structures_algorithms/dsa_travelling_salesman_approximation_algorithm.htm 

# same inputs on min spanning tree and then analysis. good for error bounding. 
# Know that answer might not be completely right, but you know how much it can be wrong by
#     may have to create a whole bunch of test cases. 
#     run lower lound and approx solution on a bunch of test cases that the exact solution will not run on.

# add lightest remaining edge that isnt in the mst after it completes. needs enough edges to make full cycle. 
# changes from v-1 to v.
# you add lightest because you dont actually know which one to add and this is a lower bound

# func to find min key, func for mst (prims??)
'''approx: perfrom prims alg on the graph -> in each iteration, find the vertex with the smallest key that hasn't been added to the mst,
          add the vertex to the mst, and then update the key and parent (parent stores the structure of the mst parent[v] is the parent vertex of v)
    -  add root note at the end
    -  calculate the cost, sum the cost
    -  print the order that they are visited, and the cost?'''

# how to analyze the outcome? how does it compare to the output of the approx. solution?
