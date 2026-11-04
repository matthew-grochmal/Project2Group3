import heapq

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.frequency = 0


class TrieAutocomplete:
    def __init__(self):
        self.root = TrieNode()
        self.query_count = 0


    def insert(self, word, frequency):

        word = word.lower()
        current = self.root

        # checking each character, nonexistent = create, if so then moves to that spot
        for character in word:

            if character not in current.children:
                current.children[character] = TrieNode()

            current = current.children[character]

        # checks the end and marks it
        if not current.is_end:
            self.query_count += 1
        current.is_end = True
        current.frequency += frequency


    #def search(self, prefix, k=5):


    #sorts by frequency then by lexicon
    def sort_results(self, item):
        return (-item[1], item[0])


    def size(self):
        return self.query_count
