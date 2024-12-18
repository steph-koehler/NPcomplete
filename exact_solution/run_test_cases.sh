#!/bin/bash

# Shell script to run test cases for TSP exact solution.
# Developed by Rachel McCoy
# Identifies which test case exceeds 20 minutes and calculates the number of permutations.

RED="\033[0;31m"
GREEN="\033[0;32m"
BLUE="\033[0;34m"
NC="\033[0m"

echo -e "${BLUE}Running all test cases for TSP exact solution...${NC}"

PROG_TO_TEST="cs412_tsp_exact.py"
TEST_CASES_DIR="test_cases"
LOG_FILE="test_results.log"

> $LOG_FILE

# Function to calculate factorial (for permutations)
factorial() {
    num=$1
    fact=1
    for (( i=1; i<=num; i++ )); do
        fact=$((fact * i))
    done
    echo $fact
}

for test_case in ${TEST_CASES_DIR}/*
do
    # Extract number of nodes from the first line of the test case file
    nodes=$(head -n 1 "$test_case" | awk '{print $1}')
    permutations=$(factorial $nodes)

    echo -e "${BLUE}Running test case: $test_case${NC}"
    echo -e "${BLUE}Number of nodes: $nodes, Permutations: $permutations${NC}" | tee -a $LOG_FILE

    start=$(date +%s)
    python3 $PROG_TO_TEST < $test_case > tmp_output.log
    end=$(date +%s)
    runtime=$((end - start))

    if [ $runtime -ge 1200 ]; then
        echo -e "${RED}Test case $test_case exceeded 20 minutes.${NC}" | tee -a $LOG_FILE
    fi

    echo -e "${GREEN}Finished test case: $test_case. Runtime: ${runtime} seconds.${NC}" | tee -a $LOG_FILE
    cat tmp_output.log >> $LOG_FILE
    echo "" >> $LOG_FILE
done

rm tmp_output.log
echo -e "${BLUE}Results logged to $LOG_FILE.${NC}"
