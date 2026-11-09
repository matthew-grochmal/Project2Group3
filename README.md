# Autocomplete Using Tries & Query Frequency Engine

## Summary
This project makes use of an auto-completion algorithm that uses two different data structures, namely, Trie and Hashmap. Given a prefix entered by a user, the algorithm returns the top K queries based on their frequencies. The project also compares the search time of both algorithms.

## Requirements
- Python 3
- Matplotlib
- Pandas

Install the required libraries:
pip install matplotlib pandas


## How to Run
1. Clone the repository.
2. Ensure that `unigram_freq.csv` exists within the project directory.
3. Start a terminal window in the project directory.

**Run the autocomplete GUI:**
python main.py

## Performance Analysis

To run the performance benchmarks:
python benchmarks.py

To generate the performance graphs:
python graphs.py

This creates a `results.csv` file with the recorded search time measurements.

## Dataset
This project makes use of `unigram_freq.csv` which has the words and their respective frequencies. This CSV file should have `word` and `count` columns.

## Group Members
- Matthew Grochmal
- Nakshatra Elango
- Arjun Suresh
