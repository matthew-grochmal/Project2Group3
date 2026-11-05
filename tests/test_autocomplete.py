from HashMapAutocomplete import HashMapAutocomplete
from TrieAutocomplete import TrieAutocomplete

def test_insert_h():
    hash = HashMapAutocomplete()
    hash.insert("messages", 15000)
    assert hash.data["messages"] == 15000

def test_prefix_search_h():
    hash = HashMapAutocomplete()
    hash.insert("messages", 15000)
    hash.insert("messenger", 12000)
    hash.insert("computer", 20000)
    results = hash.search("mess", 5)
    assert len(results) == 2
    assert ("messages", 15000) in results
    assert ("messenger", 12000) in results

def test_top_k_h():
    hash = HashMapAutocomplete()
    hash.insert("messages", 15000)
    hash.insert("messenger", 12000)
    hash.insert("messaging", 8500)
    results = hash.search("mess", 2)
    assert len(results) == 2
    assert results == [("messages", 15000), ("messenger", 12000)]

def test_duplicate_h():
    hash = HashMapAutocomplete()
    hash.insert("messages", 15000)
    hash.insert("messages", 5000)
    results = hash.search("mess", 5)
    assert results == [("messages", 20000)]

def test_case_insensitive_h():
    hash = HashMapAutocomplete()
    hash.insert("Messages", 15000)
    results = hash.search("MESS", 5)
    assert results == [("messages", 15000)]

def test_no_matched_prefix_h():
    hash = HashMapAutocomplete()
    hash.insert("messages", 15000)
    results = hash.search("xyz", 5)
    assert results == []

def test_no_prefix_h():
    hash = HashMapAutocomplete()
    hash.insert("messages", 15000)
    hash.insert("computer", 20000)
    results = hash.search("", 5)
    assert len(results) == 2

#Trie Testing
def test_insert_t():
    trie = TrieAutocomplete()
    trie.insert("messages", 15000)
    results = trie.search("mess", 5)
    assert results == [("messages", 15000)]

def test_prefix_search_t():
    trie = TrieAutocomplete()
    trie.insert("messages", 15000)
    trie.insert("messenger", 12000)
    trie.insert("computer", 20000)
    results = trie.search("mess", 5)
    assert len(results) == 2
    assert ("messages", 15000) in results
    assert ("messenger", 12000) in results

def test_top_k_t():
    trie = TrieAutocomplete()
    trie.insert("messages", 15000)
    trie.insert("messenger", 12000)
    trie.insert("messaging", 8500)
    results = trie.search("mess", 2)
    assert len(results) == 2
    assert results == [("messages", 15000), ("messenger", 12000)]

def test_duplicate_t():
    trie = TrieAutocomplete()
    trie.insert("messages", 15000)
    trie.insert("messages", 5000)
    results = trie.search("mess", 5)
    assert results == [("messages", 20000)]

def test_case_insensitive_t():
    trie = TrieAutocomplete()
    trie.insert("Messages", 15000)
    results = trie.search("MESS", 5)
    assert results == [("messages", 15000)]

def test_no_matched_prefix_t():
    trie = TrieAutocomplete()
    trie.insert("messages", 15000)
    results = trie.search("xyz", 5)
    assert results == []

def test_no_prefix_t():
    trie = TrieAutocomplete()
    trie.insert("messages", 15000)
    trie.insert("computer", 20000)
    results = trie.search("", 5)
    assert len(results) == 2