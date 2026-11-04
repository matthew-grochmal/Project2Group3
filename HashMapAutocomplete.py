

class HashMapAutocomplete:

    def __init__(self):
        self.data = {}

    def insert(self, word, frequency):
        word = word.lower()

        if word in self.data:

          
            self.data[word]+= frequency
        else:
            self.data[word]= frequency

    def search(self, prefix, k=5):
        results =[]

        for word in self.data:
            if word.startswith(prefix.lower()):
                results.append((word, self.data[word]))

        results.sort(key=self.sort_results)

        return results[:k]

    def sort_results(self, item):
        return (-item[1], item[0])
