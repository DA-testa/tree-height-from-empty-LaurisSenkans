# python3

import sys
import threading
import numpy as np


def compute_height(n, parents):
    children = [[] for i in range(n)]
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            children[parents[i]].append(i)
    height = 0
    q = [root]
    while q:
        height += 1
        new_q = []
        for node in q:
            new_q += children[node]
        q = new_q
    return height


def main():
    input_type = input()
    if input_type == "I":
        n = int(input())
        parents = np.fromstring(input(), dtype=int, sep=' ')
    elif input_type == "F":
        filename = input("Enter file name: ")
        if 'a' in filename:
            print("Invalid file name. Try again.")
            return
        try:
            with open(f'./{filename}', 'r') as f:
                n = int(f.readline())
                parents = np.fromstring(f.readline(), dtype=int, sep=' ')
        except FileNotFoundError:
            print("File not found. Try again.")
            return
    else:
        print("Invalid input type")
        return
    print(compute_height(n, parents))


sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()