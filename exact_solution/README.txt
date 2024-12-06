Exact Solution for the Traveling Salesman Problem (TSP)
=======================================================

This folder contains a brute-force solution to the Traveling Salesman Problem (TSP),
which finds the shortest route visiting all cities exactly once.

Why This Problem Is Important
=============================
The Traveling Salesman Problem has real-world applications in logistics, route planning,
and network optimization, such as:
- Optimizing delivery routes for e-commerce companies.
- Planning circuit board wiring in electronics.

Files in This Repository
=========================
- cs412_tsp_exact.py: Python script that implements a brute-force solution.
- run_test_cases.sh: Shell script to execute all test cases in the test_cases/ folder.
- test_cases/: Folder containing input files for test cases.
- test_results.log: Log file recording the results and runtime for each test case.

How to Run the Program
======================
1. Run All Test Cases
   Execute the following command from the terminal:

./run_test_cases.sh

This will:
- Run the TSP solution for all test cases in the `test_cases/` folder.
- Log results and runtime in `test_results.log`.

2. Run a Single Test Case
Execute the following command:
python3 cs412_tsp_exact.py < test_cases/<test_case_file>


Test Cases
==========
- '03-12_nodes.txt`: Standard test cases.
- `13_nodes.txt`: A test case labeled with a comment in `run_test_cases.sh`
indicating it takes more than 20 minutes to complete.
