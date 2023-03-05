# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    nodes = [[] for i in range(n)]
    root = None
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            nodes[parent].append(i)

    height = 0
    q = [root]
    while q:
        height += 1
        new_q = []
        for node in q:
            children = nodes[node]
            for child in children:
                new_q.append(child)
        q = new_q

    return height


def main():
    input_type = input("Enter input type (I for keyboard input, F for file input): ")
    if input_type.lower() == 'i':
        n = int(input("Enter number of nodes: "))
        parents = list(map(int, input("Enter the list of parents of each node: ").split()))
    elif input_type.lower() == 'f':
        file_name = input("Enter file name (excluding .txt extension): ")
        if 'a' in file_name:
            print("File name cannot contain letter a.")
            return
        try:
            with open(f"{file_name}.txt") as file:
                n = int(file.readline())
                parents = list(map(int, file.readline().split()))
        except FileNotFoundError:
            print("File not found.")
            return
    else:
        print("Invalid input type.")
        return

    print(compute_height(n, parents))


sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

