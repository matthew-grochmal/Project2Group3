import tkinter as tk
from tkinter import ttk
import csv

from HashMapAutocomplete import HashMapAutocomplete
from TrieAutocomplete import TrieMapAutocomplete

def load_data(filename, hashmap, trie):

    with open(filename, "r") as file:
        reader=csv.DictReader(file)
        for row in reader:

            word = row["word"]
            count = int(row["count"])
            hashmap.insert(word, count)
            trie.insert(word, count)

#Create both autocomplete
hashmap = HashMapAutocomplete()
trie = TrieMapAutocomplete()
load_data("unigram_freq.csv", hashmap, trie)

def search():

    prefix = search_entry.get().strip()
    try:
        k = int(k_entry.get())
        if k <= 0:
            raise ValueError
    except ValueError:
        result_label.config(text="Enter a valid positive K.")
        return

    hashmap_results = hashmap.search(prefix, k)
    trie_results = trie.search(prefix, k)

    #Clearprev results
    hashmap_list.delete(0, tk.END)
    trie_list.delete(0, tk.END)

    #Display hashmap results
    for word, frequency in hashmap_results:
        hashmap_list.insert(
            tk.END,
            f"{word} | Frequency: {frequency}"
        )

    # Display trie results
    for word, frequency in trie_results:
        trie_list.insert(
            tk.END,
            f"{word} | Frequency: {frequency}"
        )

    result_label.config(
        text=f"Showing top {k} suggestions for '{prefix}'"
    )


def add_word():

    word = new_word_entry.get().strip()

    try:
        frequency = int(new_frequency_entry.get())

        if not word or frequency < 0:
            raise ValueError

    except ValueError:
        result_label.config(text="Enter a valid word and frequency.")
        return

    hashmap.insert(word, frequency)
    trie.insert(word, frequency)

    new_word_entry.delete(0, tk.END)
    new_frequency_entry.delete(0, tk.END)

    result_label.config(
        text=f"Successfully added frequency for '{word}'."
    )

    search()

window = tk.Tk()

window.title("Prefix Autocomplete System")
window.geometry("850x600")


#heading win
title = tk.Label(
    window,
    text="Prefix Autocomplete",
    font=("Arial", 22, "bold")
)

title.pack(pady=15)


#search the section
search_frame = tk.Frame(window)

search_frame.pack(pady=10)

tk.Label(
    search_frame,
    text="Enter Prefix:",
    font=("Arial", 12)
).grid(row=0, column=0, padx=5)

search_entry = tk.Entry(
    search_frame,
    font=("Arial", 12),
    width=20
)

search_entry.grid(row=0, column=1, padx=5)

tk.Label(
    search_frame,
    text="Top K:"
).grid(row=0, column=2, padx=5)

k_entry = tk.Entry(
    search_frame,
    width=5
)

k_entry.insert(0, "5")
k_entry.grid(row=0, column=3, padx=5)

search_button = tk.Button(
    search_frame,
    text="Search",
    command=search
)

search_button.grid(row=0, column=4, padx=5)

#result
results_frame = tk.Frame(window)
results_frame.pack(pady=20, fill="both", expand=True)


#hashmap results
hashmap_frame = tk.LabelFrame(
    results_frame,
    text="Hash Map Results",
    font=("Arial", 12, "bold")
)

hashmap_frame.pack(
    side="left",
    padx=15,
    fill="both",
    expand=True
)

hashmap_list = tk.Listbox(
    hashmap_frame,
    font=("Arial", 11),
    bg = "#ffcccc",
     fg = "black"
)

hashmap_list.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)


#hrie results
trie_frame = tk.LabelFrame(
    results_frame,
    text="Trie Results",
    font=("Arial", 12, "bold")
)

trie_frame.pack(
    side="right",
    padx=15,
    fill="both",
    expand=True
)

trie_list = tk.Listbox(
    trie_frame,
    font=("Arial", 11),
    bg = "#cce5ff",
fg = "black"
)

trie_list.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)


# to add new word
add_frame = tk.LabelFrame(
    window,
    text="Add/Update Search Query"
)

add_frame.pack(pady=10, padx=20, fill="x")

tk.Label(
    add_frame,
    text="Word:"
).grid(row=0, column=0, padx=5, pady=10)

new_word_entry = tk.Entry(add_frame)

new_word_entry.grid(row=0, column=1, padx=5)

tk.Label(
    add_frame,
    text="Frequency: "
).grid(row=0, column=2, padx=5)

new_frequency_entry = tk.Entry(add_frame, width=10)

new_frequency_entry.grid(row=0, column=3, padx=5)

tk.Button(
    add_frame,
    text="Add / Update",
    command=add_word
).grid(row=0, column=4, padx=10)

result_label = tk.Label(
    window,
    text="Enter a prefix to begin.",
    font=("Arial", 11)
)

result_label.pack(pady=10)


# Enter key also enable search
search_entry.bind(
    "<Return>",
    lambda event: search()
)




window.mainloop()
