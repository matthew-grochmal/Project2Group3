import heapq

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.frequency = 0


class TrieMapAutocomplete:
    
    def __init__( self):
        self.root= TrieNode()
        self.query_count= 0


    def insert(self, word, frequency):

        word =word.lower()
        current =  self.root

        # check each char for its existence
        for character in word:

            if character not in current.children:
                current.children[character] =TrieNode()

            current = current.children[character]
        if not current.is_end:
            self.query_count+= 1
        current.is_end= True
        
        
        current.frequency += frequency


    def search(self, prefix, k=5):
        prefix = prefix.lower()
        current = self.root
        results = []

        #moves to that node
        for character in prefix:

            if character not in current.children:
                return []

            current =current.children[character]

        #dfs
        self.dfs(current, prefix, results)
        results = heapq.nsmallest(
            k, results, key=self.sort_results
        )

        return results

    #def the dfs func
    def dfs(self, node, current_word, results):
        if node.is_end:
            results.append((current_word,node.frequency))


        for character, child in node.children.items():
            self.dfs(child,current_word+character, results)

    def sort_results(self, item):
        return (-item[1], item[0])


    def size(self):
        return self.query_count
