#!/bin/bash

# Directory containing the test cases
TEST_CASE_DIR="test_cases"

# Python script to run
PROGRAM="cs412_tsp_approx.py"  # Replace with the actual filename of your Python program

# Output directory for results
RESULTS_DIR="test_results"
mkdir -p $RESULTS_DIR

# Check if the program exists
if [[ ! -f "$PROGRAM" ]]; then
  echo "Error: Python program '$PROGRAM' not found!"
  exit 1
fi

# Iterate through each test case in the directory
for TEST_FILE in "$TEST_CASE_DIR"/*; do
  if [[ -f "$TEST_FILE" ]]; then
    TEST_NAME=$(basename "$TEST_FILE")  # Get the test case name
    echo "Running test case: $TEST_NAME"
    
    # Time the program execution
    START_TIME=$(date +%s.%N)
    python3 "$PROGRAM" < "$TEST_FILE" > "$RESULTS_DIR/$TEST_NAME.out"
    END_TIME=$(date +%s.%N)
    
    # Calculate elapsed time
    ELAPSED_TIME=$(echo "$END_TIME - $START_TIME" | bc)
    echo "Test case $TEST_NAME completed in $ELAPSED_TIME seconds"
    
    # Save timing information
    echo "$TEST_NAME: $ELAPSED_TIME seconds" >> "$RESULTS_DIR/timing.log"
  fi
done

echo "All test cases processed. Results and timing information saved in $RESULTS_DIR."
