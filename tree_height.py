# python3

import sys
import threading
import numpy as np

def compute_height(n, parents):
    children = [[] for _ in range(n)]
    for i, p in enumerate(parents):
        if p == -1:
            root = i
        else:
            children[p].append(i)
    heights = np.zeros(n, dtype=np.int32)
    def compute_height_util(node):
        if not children[node]:
            return 0
        child_heights = [compute_height_util(child) for child in children[node]]
        heights[node] = 1 + np.max(child_heights)
        return heights[node]
    compute_height_util(root)
    return np.max(heights)

def main():
    input_type = input("Enter input type (I for keyboard, F for file): ")
    if input_type == "I":
        n = int(input())
        parents = np.array(list(map(int, input().split())))
    elif input_type == "F":
        filename = input("Enter filename (don't use letter a): ")
        if 'a' in filename:
            print("Invalid filename")
            return
        with open(f"folder/{filename}") as file:
            n = int(file.readline())
            parents = np.array(list(map(int, file.readline().split())))
    else:
        print("Invalid input type")
        return
    print(compute_height(n, parents))

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()