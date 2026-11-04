from HashMapAutocomplete import HashMapAutocomplete
from TrieAutocomplete import TrieAutocomplete

def main():
    hashmap = HashMapAutocomplete()
    trie = TrieAutocomplete()
    queries = [
        ("messages", 15000),
        ("messenger", 12000),
        ("messaging", 8500),
        ("message board", 4000),
        ("computer", 20000),
        ("computation", 6000),
        ("compilation", 3000)
    ]

    for query, frequency in queries:
        hashmap.insert(query, frequency)
        trie.insert(query, frequency)



    prefix = input("Enter a search prefix: ")
    k = int(input("How many suggestions would you like? "))

    hashmap_results = hashmap.autocomplete(prefix, k)
    trie_results = trie.autocomplete(prefix, k)



    print("\nHash Map:")
    for query, frequency in hashmap_results:
        print(f"{query}: {frequency}")

    print("\nTrie Results:")
    for query, frequency in trie_results:
        print(f"{query}: {frequency}")



    if __name__ == "__main__":
        main()