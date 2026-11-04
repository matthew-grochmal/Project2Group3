import matplotlib.pyplot as ply
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("results.csv")
df = df.sort_values("Dataset_size")

plt.figure(figsize = (10,6))

#Plotting Tries
plt.plot(df["Dataset_size"], df["Trie_times"], label = "Trie", linewidth=2, marker = "o")

#Plotting Hash
plt.plot(df["Dataset_size"], df["Hashmap_times"], label = "Hashmap", linewidth=2, marker = "o")

#Formatting
plt.title("Trie v. Hashmap Performance", fontsize = 14, fontweight="bold")
plt.xlabel("Dataset Size (Num. Queries)", fontsize = 12, fontweight="bold")
plt.ylabel("Search Time (ms)", fontsize = 12, fontweight="bold")
plt.grid(True, linestyle = "-", color = "0.9", alpha = 0.3)
plt.legend()
plt.tight_layout()
plt.show()