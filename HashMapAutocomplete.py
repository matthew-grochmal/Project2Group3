class HashMapAutocomplete:

#need to init a empy dict to store data
    def __init__(self):
        self.data = {}


#insert the query and its freq to hashmap
    def insert(self, word, frequency):
        word =word.lower()

        if word in self.data:
            self.data[word]+= frequency
        else:
            self.data[word]=frequency

    def search(self, prefix, k =5):
        results = []
#o(n)
        for word in self.data:
            if word.startswith( prefix.lower()):
                results.append((word,self.data[word]))

        results.sort(key=self.sort_results)

        return results[:k]

    def sort_results(self, item):
        return (-item[1], item[0])
