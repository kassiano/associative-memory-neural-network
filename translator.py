import numpy as np

weights = np.loadtxt('weights.txt')

#print(weights)

word = input('Enter the word?\n') 

array_ascii = list(word.encode('ascii'))

num_zeros = 10 - len(array_ascii)
if num_zeros > 0:
    array_ascii = [0] * num_zeros + array_ascii

word_array = np.array([array_ascii])

print(word_array)

prediction = np.dot(word_array, weights)

result = ''.join(chr(round(i)) for i in prediction[0])

print(prediction)
print(result)