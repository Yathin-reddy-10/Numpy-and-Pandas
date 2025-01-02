import numpy as np  
import pandas as pd
# a = np.array([[1,2,30],[10,15,4]])  
# b = np.array([[1,2,3],[12, 19, 29]])  
# print("Sum of array a and b\n",a+b)  
# print("Product of array a and b\n",a*b)  
# print("Division of array a and b\n",a/b)  

# d = np.array([1,2,3,4])
# print("array d is",d)

# arr = np.array([1, 2, 3, 4, 5])
# print(arr.sum())     
# print(arr.mean())   
# print(arr.max())    
# print(arr.std()) 
# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6]])

# # Vertical stacking
# print(np.vstack([a, b]))

# # Horizontal stacking
# print(np.hstack([a, b.T]))

# # Python program explaining 
# # vstack() function 

# import numpy as geek 

# # input array 
# in_arr1 = geek.array([ 1, 2, 3] ) 


# in_arr2 = geek.array([ 4, 5, 6] ) 


# # Stacking the two arrays vertically 
# out_arr = geek.hstack((in_arr1, in_arr2)) 
# print ("Output vertically stacked array:\n ", out_arr) 
 
 
# rand = np.random.rand(3)  # Uniform random numbers
# rand_int = np.random.randint(0, 100, (5, 10))  # Random integer
# print(rand)
# print(rand_int)
a = np.array([1, 2, 3])

# Extract the first two rows
# print(a[1:2, :])  # Output: [[1 2 3], [4 5 6]]

# # Extract the second column
# print(a[:, 1])  # Output: [2, 5, 8]
b = pd.Series(a)  
print(b)  