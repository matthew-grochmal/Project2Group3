import csv
import time
import statistics

from TrieAutocomplete import TrieMapAutocomplete
from HashMapAutocomplete import HashMapAutocomplete

dataset_sizes = [1000, 10000, 50000, 100000]
prefixes = ["app", "comp", "messag", "search"]
repetitions = 100
words = []

with open("unigram_freq.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    columns = reader.fieldnames
    word_column = next((c for c in columns if c.lower() in ["word", "query", "term"]), None)
    frequency_column = next((c for c in columns if c.lower() in ["frequency", "count", "term"]), None)
    if word_column is None or frequency_column is None:
        raise ValueError("No word or frequency column")
    for row in reader:
        word = row[word_column].strip()
        if word:
            frequency = int(row[frequency_column])
            words.append((word, frequency))
print("Total words loaded: ", len(words))

tested_sizes = [size for size in dataset_sizes if len(words) >= size]

if not tested_sizes: raise ValueError("Not enough words for benchmark.")

results = []

for size in tested_sizes:
    print("\nTesting dataset size: ", size)
    data = words[:size]
    trie = TrieMapAutocomplete()
    hash = HashMapAutocomplete()
    for word, frequency in data:
        trie.insert(word, frequency)
        hash.insert(word, frequency)
    for prefix in prefixes:
        trie_time = []
        hash_time = []
        for _ in range(repetitions):
            start = time.perf_counter()
            trie.search(prefix, 5)
            end = time.perf_counter()
            trie_time.append((end - start)*1000)
            start = time.perf_counter()
            hash.search(prefix, 5)
            end = time.perf_counter()
            hash_time.append((end - start)*1000)
        avg_trie = statistics.mean(trie_time)
        avg_hash = statistics.mean(hash_time)
        results.append((size, prefix, avg_trie, avg_hash))
        print(f"Prefix: {prefix} | " f"Trie: {avg_trie:.6f} ms | " f"Hash Map: {avg_hash:.6f} ms")
with open("results.csv", "w", newline = "") as f:
    writer = csv.writer(f)
    writer.writerow(("Dataset_size", "Prefix", "Trie_times", "Hashmap_times"))
    writer.writerows(results)
print("\nBenchmark results now saved to results.csv.")