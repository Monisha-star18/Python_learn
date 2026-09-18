import numpy as np

print(np.__version__)

arr = np.array([1,2,3,4,5])

arr = arr * 2 
# print(arr)
# print(type(arr))

arr1 = np.array('A')
arr2= np.array([[ ['A','B','C'], ['D','E','F'], ['G','H','I']],
               [ ['A','S','C'], ['D','E','F'], ['G','H','I']],
               [ ['A','B','C'], ['D','p','i'], ['G','H','I']]])

#no of dimension of a array
# print(arr1.ndim)
# print(arr2.ndim)

#shape 
# print(arr2.shape)

#chain indexing 
# print(arr2[1][0][1])
# print(arr2[2][1][2])

#multidimenional indexing (much faster than chain indexing)
# print(arr2[1,0,1])

word = arr2[0,0,0] + arr2[1,0,1] + arr2[2,1,2]
# print(word)

newArray = np.array([[1,2,3,4],
                     [5,6,7,8],
                     [9,10,11,12],
                     [13,14,15,16]])

#slice array[start:end:step]
# print(newArray[::2])
# print(newArray[::-1])
# print(newArray[::-2])
# print(newArray[1:3])

#column [row , column ]
# print(newArray[:,1])
# print(newArray[:,0:3])
# print(newArray[:,::2])

# first 2 rows and first 2 columns 
# print(newArray[0:2,0:2])

#Scalar arithmetic
arr4 = np.array([1,2,3])
arr5 = np.array([4,5,6])

# print(arr4+1)
# print(arr4 -2)
# print(arr4 ** 4)

#vectorised math funcs
# print(np.sqrt(arr4))
# print(np.pi)

#find area 
# print(np.pi * arr4 **2 )

#elemne-wise arithmetic 
# print(arr4+arr5)
# print(arr4-arr5)
# print(arr4*arr5)
# print(arr4/arr5)
# print(arr4**arr5)


#comparison opertaor 
scores = np.array ([91,55,100,73,82,64])

# print(scores == 100)
# print(scores < 60)

# scores[scores < 60] =0
# print(scores)


#broadcasting 
array1= np.array([[1,2,3,4]])
array2 = np.array([[1],[2],[3],[4]])

print(array1.shape)
print(array2.shape)

age = np.array([[18,19,14,33,56,99,100,34],[21,17,16,16,45,65,78,20]])

teen = age [age < 18]
adults = age [(age >=18 ) & (age < 65)]
seniors = age [age >=65]
evens = age [age % 2 ==0 ]
odds = age [age % 2 !=0 ]

print(evens , odds)


#to filter at the same time dont flatten the shape of array then 
#syntax where(condition , array , filler )
teenage = np.where(age < 18 , age , 0)
print(teenage)

#random numbers 

#the default random function 
rng = np.random.default_rng()

#random on integer 
print(rng.integers(1,100))
print(rng.integers(low= 1,high=100,size = (2,2)))

#random on float 
print(rng.uniform(low=1,high=3,size=(3,2)))


arrayOriginal = np.array([1,2,3,4,6,7,8,9,10])
#shuffle the array 
rng.shuffle(arrayOriginal)

print(arrayOriginal)

#take one random number 
option = rng.choice(arrayOriginal , size =(3,2))
print(option)