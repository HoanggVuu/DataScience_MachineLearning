'''
Pandas Series is a one-dimensional labeled array capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.). 
It is similar to a column in a spreadsheet or a SQL table.

Sometimes, can consider it as a dictionary-like structure where each element has a unique label (index).
Or like numpy 1D array with additional features like labels.


Flow of contents
1. Creating a Series: from a list, dictionary, ndarray or scalar value; with indexing.
2. Accessing elements: using index labels or positions.
'''

import pandas as pd

#-------------------------------------------------------------------------------------------------------------#
#---------------------------------------- 1. Creating a Series -----------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#

#################
## From a list ##
#################

#---------------
## Without index labels, 
## pandas will create a default integer index starting from 0.
#----------------

s = pd.Series(data = [1, 2, 3, 4, 5])

print(s)
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64

#----------------
## With custom index labels
#----------------

s = pd.Series(data = [1, 2, 3, 4, 5], index = ['one', 'two', 'three', 'four', 'five'])

print(s)
# one      1
# two      2
# three    3
# four     4
# five     5
# dtype: int64


####################
## From a ndarray ##
####################

import numpy as np

s = pd.Series(data = np.random.rand(5), index = ['a', 'b', 'c', 'd', 'e'])

print(s)
# a    0.503145
# b    0.622401
# c    0.766209
# d    0.962831
# e    0.794495
# dtype: float64


#######################
## From a dictionary ##
#######################

# The keys will be used as index labels, and the values will be the data in the Series.
s = pd.Series(data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

print(s)
# a    1
# b    2
# c    3
# d    4
# e    5
# dtype: int64


#########################
## From a scalar value ##
#########################

s = pd.Series(data = 5, index = ['a', 'b', 'c', 'd', 'e'])

print(s)
# a    5
# b    5
# c    5
# d    5
# e    5
# dtype: int64


#--------------------------------------------------------------------------------------------------------------#
#---------------------------------------- 2. Accessing elements -----------------------------------------------#
#--------------------------------------------------------------------------------------------------------------#

s_index = pd.Series(data = [10, 20, 30, 40, 50], index = ['a', 'b', 'c', 'd', 'e'])

###################
## Using .iloc() ##
###################

# .iloc[] is used for integer-location based indexing, 
# which means you can access elements by their integer position.

s_index.iloc[0]  # Accessing the first element
# np.int64(10)

s_index.iloc[1:3]  # Accessing a range of elements
# b    20
# c    30
# dtype: int64

s_index.iloc[:3] # Accessing from the start to the 2-indexed element (first three elements)
# a    10
# b    20
# c    30
# dtype: int64

s_index.iloc[2:]  # Accessing from the 2-indexed element to the end (third element and beyond)
# c    30
# d    40
# e    50
# dtype: int64

s_index.iloc[-1]  # Accessing the last element
# np.int64(50)

s_index.iloc[-3:]  # Accessing the last three elements
# c    30
# d    40
# e    50
# dtype: int64

s_index.iloc[[0, 2, 4]]  # Accessing specific elements by their integer positions
# a    10
# c    30
# e    50
# dtype: int64


############################
## Using dictionary style ##
############################

s_index['a']  # Accessing by index label
# np.int64(10)

s_index[['a', 'c', 'e']]  # Accessing multiple elements by index labels
# a    10
# c    30
# e    50
# dtype: int64

s_index['b':'e']  # Accessing a range of elements by index labels (inclusive)
# b    20
# c    30
# d    40
# e    50
# dtype: int64

s_index['c':]  # Accessing from a specific index label to the end
# c    30
# d    40
# e    50
# dtype: int64

s_index[:'c']  # Accessing from the start to a specific index label (inclusive)
# a    10
# b    20
# c    30
# dtype: int64

s_index["f"] # Raises KeyError because "f" is not in the index
# KeyError: 'f'

s_index.get('d', 'Not Found')  # Using get() to access an element with a default value if not found
# np.int64(40)

s_index.get('z', 'Not Found')  # Accessing a non-existent index label with a default value
# 'Not Found'

s_index.get('z') # Accessing a non-existent index label without a default value returns None
# None

s_index.get(['a', 'c', 'e'])  # Accessing multiple elements using get()
# a    10
# c    30
# e    50
# dtype: int64


##########################################
## NOTE on default integer index Series ##
##########################################

s_no_index = pd.Series(data = [2, 3, 5, 7, 11])

print(s_no_index)
# 0     2
# 1     3
# 2     5
# 3     7
# 4    11
# dtype: int64

s_no_index.iloc[0]  # Accessing the first element
# np.int64(2)

s_no_index[0]  # Accessing the first element using index label
# np.int64(2)

'''
These two methods result in the same output.
However, they are fundamentally different:
- .iloc[] is used for positional indexing, which means it accesses elements based on their integer position in the Series.
- Using index labels (like 0) accesses elements based on their label

This case is just a coincidence because the default index labels are integers starting from 0.
If the Series had a different index, using .iloc[] would still work based on position,
while using index labels would require the exact label to be present.
'''

s_index[0]
# <stdin>:1: FutureWarning: Series.__getitem__ treating keys as positions is deprecated. 
#            In a future version, integer keys will always be treated as labels (consistent with DataFrame behavior). 
#            To access a value by position, use `ser.iloc[pos]`
# np.int64(10)

'''
Here, the s_index series has a custom index, and using an integer key (like 0) raises a FutureWarning.
This is because in future versions of pandas, using integer keys will always be treated as labels,
not positions, to maintain consistency with DataFrame behavior.
'''

