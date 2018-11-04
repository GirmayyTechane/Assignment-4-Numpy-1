#Problem 1
#Write a function so that the columns of the output matrix are powers of the input
#vector.
#The order of the powers is determined by the increasing boolean argument. Specifically,
#when increasing is False, the i-th output column is the input vector raised element-wise
#to the power of N - i - 1.

#answer.

def vander(a): # create vander function
    a=np.asarray(a) # define an array 
    n=len(a) # size of array 
    v = np.column_stack([a**(n-1-x) for x in range(n)]) # compute vander matrix 
    return v #return result
    
 e.g 
 a=[1,2,3]
 v
  
Out[65]:
array([[1, 1, 1],
       [4, 2, 1],
       [9, 3, 1]], dtype=int32)
