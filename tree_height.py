# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Create an array to store the height of each node
    heights = [-1] * n

    # Find the root node
    root = None
    for i in range(n):
        if parents[i] == -1:
            root = i
            break

    # Define a recursive function to compute the height of each node
    def dfs(node):
        if heights[node] != -1:
            return heights[node]

        if parents[node] == -1:
            heights[node] = 1
        else:
            heights[node] = 1 + dfs(parents[node])

        return heights[node]

    # Compute the height of each node starting from the root
    dfs(root)

    # Return the maximum height
    return max(heights)


def main():
    # Read input from keyboard or file
    input_type = input("Enter input type (K for keyboard, F for file): ")
    if input_type == "K":
        n = int(input())
        parents = list(map(int, input().split()))
    elif input_type == "F":
        file_name = input("Enter file name (without the letter a): ")
        if "a" in file_name:
            print("File name cannot contain the letter a.")
            return
        try:
            with open(f"./input/{file_name}", "r") as f:
                n = int(f.readline())
                parents = list(map(int, f.readline().split()))
        except FileNotFoundError:
            print("File not found.")
            return
    else:
        print("Invalid input type.")
        return

    # Compute the height of the tree and output the result
    print(compute_height(n, parents))


sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
