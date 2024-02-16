import numpy as np
import pandas as pd

max_word_size = 10

def ascii_vector(string):
    size = max_word_size
    ascii_list = [0] * size

    for i in range(len(string) -1, -1, -1):
        ascii_list[size-1] = ord(string[i])
        size -= 1
    return ascii_list

dictionary = pd.read_csv("dictionary.csv")

portuguese = dictionary["portuguese"]
english = dictionary["english"]

A = np.empty((0, max_word_size), int)
b = np.empty((0, max_word_size), int)

for item1, item2 in zip(portuguese, english):
    vector1 = ascii_vector(item1)
    vector2 = ascii_vector(item2)
   
    A = np.vstack([A, vector1])    
    b = np.vstack([b, vector2])    
    

pseudo_inv = np.linalg.pinv(A)
x = np.dot(pseudo_inv, b)


np.savetxt('weights.csv', x)