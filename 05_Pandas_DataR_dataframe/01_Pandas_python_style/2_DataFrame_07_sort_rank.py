'''
1. Sort:
   + df.sort_values(by=..., ascending=..., inplace=...)
   + df.sort_index(axis=..., ascending=..., inplace=...)

2. Rank:
   + df.rank(method = "average", ascending = True, axis = 1)
   + df.rank(method = "min", ascending = True, axis = 1)
   + df.rank(method = "max", ascending = True, axis = 1)
   + df.rank(method = "first", ascending = True, axis = 1)
   + df.rank(method = "dense", ascending = True, axis = 1)
   + df.rank(pct = True)
'''

import pandas as pd

#--------------------------------------------------------------------------------------------------------#
#-------------------------------------------- 1. Sort ---------------------------------------------------#
#--------------------------------------------------------------------------------------------------------#

df_raw_sort = pd.DataFrame(
    {
        "name": ["Alice", "Alice", "Alice", "Bob", "Bob", "Charlie"],
        "subject": ["Math", "English", "Science", "Math", "English", "Math"],
        "score": [85, 90, 78, 92, 88, 95],
        "age": [20, 20, 20, 22, 22, 23],
    }
)

df_raw_idx = pd.DataFrame(
    {
        "Numbers":[1, 2, 3, 4, 5],
        "Letters":["a", "b", "c", "d", "e"]
    }, 
    index=[100, 29, 234, 1, 150],
)

########################
##  df.sort_values()  ##
########################

#---------------
## Sort by single column
#---------------

df_sorted = df_raw_sort.sort_values(by="score", ascending=False, inplace=False)
print(df_sorted)
#       name  subject  score  age
# 5  Charlie     Math     95   23
# 3      Bob     Math     92   22
# 1    Alice  English     90   20
# 4      Bob  English     88   22
# 0    Alice     Math     85   20
# 2    Alice  Science     78   20

#---------------
## Sort by multiple columns and orders
#---------------

df_sorted = df_raw_sort.sort_values(by=["name", "score"], ascending=[False, True], inplace=False)
print(df_sorted)
#       name  subject  score  age
# 5  Charlie     Math     95   23
# 4      Bob  English     88   22
# 3      Bob     Math     92   22
# 2    Alice  Science     78   20
# 0    Alice     Math     85   20
# 1    Alice  English     90   20

#######################
##  df.sort_index()  ##
#######################

print(df_raw_idx)
#      Numbers Letters
# 100        1       a
# 29         2       b
# 234        3       c
# 1          4       d
# 150        5       e

#---------------
## Sort by axis=0 (row names), ascending=True
#---------------

df_sorted = df_raw_idx.sort_index(axis=0, ascending=True, inplace=False)

print(df_sorted)
#      Numbers Letters
# 1          4       d
# 29         2       b
# 100        1       a
# 150        5       e
# 234        3       c

#---------------
## Sort by axis=1 (column names), ascending=False
#---------------

df_sorted = df_raw_idx.sort_index(axis=0, ascending=False, inplace=False)

print(df_sorted)
#      Numbers Letters
# 234        3       c
# 150        5       e
# 100        1       a
# 29         2       b
# 1          4       d

#---------------
## Sort by axis=1 (column names), ascending=True
#---------------

df_sorted = df_raw_idx.sort_index(axis=1, ascending=True, inplace=False)

print(df_sorted)
#     Letters  Numbers
# 100       a        1
# 29        b        2
# 234       c        3
# 1         d        4
# 150       e        5

#--------------------------------------------------------------------------------------------------------#
#-------------------------------------------- 2. Rank ---------------------------------------------------#
#--------------------------------------------------------------------------------------------------------#

df_raw_rank = pd.DataFrame(
    {
        "name": ["Alice", "Bob", "Charlie", "David", "Eva", "Freddy", "George", "Hannah"],
        "score": [85, 92, 85, 88, 90, 66, 66, 66]
    }
)

