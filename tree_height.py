# python3

import sys
import threading
import numpy as np


def height_c(n, parents):


    heigts = np.zeros(int(n))
    max_height = 0

    for i in range(int(n)):
        if heigts[i] > 0:
            continue
        height = 0
        j = i
        while j != -1:
            if heigts[j] > 0:

                height += heigts[j]
                break
            else:

                height += 1
                j = int(parents[j])
        heigts[i] = height
        if height > max_height:
            max_height = height

    return max_height


def read_input():
    input_type = input().strip()
    if input_type == "F":
        file_path = input().strip()
        try:
            with open(file_path, 'r') as f:
                n = f.readline().strip()
                parents = f.readline().strip().split()
        except:
            print("Invalid input")
            return None, None
    elif input_type == "I":
        n = input().strip()
        parents = input().strip().split()
    else:
        
        return None, None
    return n, parents


def main():
    
    n, parents = read_input()
    if n and parents:
        height = height_c(n, parents)
        print(int(height))


if __name__ == "__main__":
    
    
    sys.setrecursionlimit(10 ** 7)
    threading.stack_size(2 ** 27)
    threading.Thread(target=main).start()