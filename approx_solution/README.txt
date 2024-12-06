Approximate Solution for the Traveling Salesman Problem (TSP)
=======================================================

This folder contains a randomness and a greedy approach to approximating
TSP in polynomial time.

How to Run the Program
======================
Run All Test Cases
   Execute the following command from the terminal within the approx_solution directory:

chmod +x run_test_cases.sh
./run_test_cases.sh

This will:
- Run the TSP approximation for all test cases in the `test_cases` directory.
- Log results and runtime in the `test_results` directory.


Run Non-Optimal Test Case:

chmod +x run_nonopt_cases.sh
./run_nonopt_cases.sh


Run Wall Clock

chmod +x compute_approx_wallclock.sh
./compute_approx_wallclock.sh





Test Cases
==========
- '03-12_nodes.txt`: Standard test cases.
- `13_nodes.txt`: A test case labeled with a comment in `run_test_cases.sh`
indicating it takes more than 20 minutes to complete.