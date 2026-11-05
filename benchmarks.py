import csv
import time
import statistics

from TrieAutocomplete import TrieAutocomplete
from HashMapAutocomplete import HashMapAutocomplete

dataset_sizes = [1000, 10000, 50000, 100000]
prefixes = ["app", "comp", "messag", "search"]
repititions = 100
words = []

with open("english_word_frequency.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    columns = reader.fieldnames
    word_column = next(c for c in columns if c.lower() in ["word", "query", "term"]), None)
    frequency_column = next(c for c in columns if c.lower() in ["frequency", "count", "term"]), None)
    if word_column is None or frequency_column is None:
        raise ValueError("No word or frequency column")
    for row in reader:
        word = row[word_column].strip()
        if word:
            frequency = int(row[frequency_column])
            words.append(word, frequency)
