Exact Solution for the Traveling Salesman Problem (TSP)
=======================================================

This folder contains a brute-force solution to the TSP, 
which finds the shortest route visiting all cities exactly once.

Files
- cs412_tsp_exact.py: Main program.
- run_test_cases.sh: Shell script to run all test cases.
- test_cases/: Folder with test case files.
- test_results.log: Log of results after running test cases.

How to Run
==========

Run All Test Cases
   ./run_test_cases.sh
- Calculates permutations for each test case.
- Logs runtime and results in test_results.log.
- Flags test cases exceeding 20 minutes.

Run a Single Test Case
   python3 cs412_tsp_exact.py < test_cases/<test_case_file>

