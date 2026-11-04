#ifndef HASH_MAP_AUTOCOMPLETE_H
#define HASH_MAP_AUTOCOMPLETE_H

#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

class HashMapAutocomplete {
private:
    // actual maping of stuff
    unordered_map<string, int> queries;

public:
    //basic insertion
    void insert(string query, int frequency);

    // the output format
    vector<pair<string, int>> autocomplete(string prefix, int k);

    // size of our hashmap
    int size();
};

#endif
