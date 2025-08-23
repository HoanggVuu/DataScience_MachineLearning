'''
The pandas.Series.str accessor provides vectorized string operations 
for Series and Index objects containing string data. 

It's one of pandas' most powerful features for text processing, 
offering over 50 methods that mirror Python's built-in string methods 
while handling missing values automatically and operating efficiently on entire Series at once.


Flow of contents:

0. pandas.Series.str accessor: "lazy" transform to string type

1. Slicing and Indexing:
   - .slice(start, stop, step)
   - .slice_replace(start, stop, repl)
   - .get(index)

2. Basic Transformations:
   - Case transformations: .lower(), .upper(), .title(), .capitalize(), .swapcase()
   - Information retrieval: .len(), .count(pattern)
   - Stripping: .strip(), .lstrip(), .rstrip()

3. Checking methods (Boolean returns):
   - Character type checks: .isalpha(), .isdigit(), .isnumeric(), .isdecimal(), .isalnum(), .isspace()
   - Case checks: .isupper(), .islower(), .istitle()
   - Pattern checks: .startswith(prefix), .endswith(suffix), .contains(pattern)

4. Split and Partion:
   - Spliting: .split(delimiter), .rsplit(delimiter)
   - Partioning: .partition(separator), .rpartition(separator)
   
5. Joinning: .join(delimiter)

6. Replacement, Removal, Repeat, Wrap:
   - .replace(old, new)
   - .removeprefix(prefix)
   - .removesuffix(suffix)
   - .repeat(n)
   - .wrap(width)

7. RegEx, Matching, Finding, Extracting:
   - Matching: .match(pattern), .fullmatch(pattern), .contains(pattern, regex=True)
   - Finding: .find(pattern), .rfind(pattern), .findall(pattern), .index(pattern), .rindex(pattern)
   - Extracting: .extract(pattern), .extractall(pattern)

8. Concatenation: .cat(others=None, sep='', na_rep=None)

9. Padding and Alignment:
   - Padding: .pad(width, side='left', fillchar=' ')
   - Alignment: .ljust(), .rjust(), .center()
   - Zero-fill: .zfill(width)

10. Categorical Encoding: pd.factorize(), pd.get_dummies()

11. Unicode and Encoding:
    - .normalize(form='NFC')
    - .encode(encoding='utf-8', errors='strict')
    - .decode(encoding='utf-8', errors='strict')

12. Real applications:
    - Data cleaning
    - Email processing
'''

import pandas as pd
import numpy as np


#--------------------------------------------------------------------------------------------------------#
#----------------------------------- 0. pandas.Series.str accessor --------------------------------------#
#--------------------------------------------------------------------------------------------------------#

'''
The pandas.Series.str accessor provides a convenient way to apply string manipulation methods 
to each element of a Pandas Series containing string data.

 It acts as a specialized namespace, allowing you to use methods that are similar to Python's built-in string methods 
 (like lower(), upper(), contains(), split(), replace(), etc.) directly on the Series.
'''

#############################
## With string-type series ##
#############################

s = pd.Series(['hello', 'world'])

print(s.upper())
'''AttributeError: 'Series' object has no attribute 'upper'''

print(s.str.upper())
# 0    HELLO
# 1    WORLD
# dtype: object


#######################################################
## With numeric series, must convert to string first ##
#######################################################

s_nums = pd.Series([1, 2, 3, np.nan, 5])

print(s_nums.astype(str))
# 0    1.0
# 1    2.0
# 2    3.0
# 3    nan
# 4    5.0
# dtype: object

'''
NOTE: After using .astype(str), all the numeric values have the format with a decimal point (e.g., '1.0', '2.0', etc.),
      and the NaN value is represented as the string 'nan'.
'''

print(s_nums.astype(str).str.fullmatch(r"\d+\.\d+"))
# 0     True
# 1     True
# 2     True
# 3    False
# 4     True
# dtype: bool


#---------------------------------------------------------------------------------------------------------#
#--------------------------------------- 1. Slicing and Indexing -----------------------------------------#
#---------------------------------------------------------------------------------------------------------#

s_heroes = pd.Series(
    data = ["Tony_Stark", "Steve_Rogers", "Bruce_Banner", "Pietro_Maximoff"],
    index = ["Ironman", "CaptainAmerica", "Hulk", "Quicksilver"]
)

#####################
## .slice() method ##
#####################

'''
.str.slice(start=None, stop=None, step=None)
'''

print(s_heroes.str.slice(start = 0, stop = 4, step = 1))
# Ironman           Tony
# CaptainAmerica    Stev
# Hulk              Bruc
# Quicksilver       Piet
# dtype: object

print(s_heroes.str.slice(start = 5))
# Ironman                 Stark
# CaptainAmerica        _Rogers
# Hulk                  _Banner
# Quicksilver        o_Maximoff
# dtype: object

print(s_heroes.str.slice(stop = 3))
# Ironman           Ton
# CaptainAmerica    Ste
# Hulk              Bru
# Quicksilver       Pie
# dtype: object

print(s_heroes.str.slice(step = 2))
# Ironman              Tn_tr
# CaptainAmerica      SeeRgr
# Hulk                BueBne
# Quicksilver       Per_aiof
# dtype: object


#############################
## .slice_replace() method ##
#############################

'''
.str.slice_replace(start=None, stop=None, repl=None)
'''

print(s_heroes.str.slice_replace(start = 0, stop = 4, repl = "Dr"))
# Ironman                Dr_Stark
# CaptainAmerica       Dre_Rogers
# Hulk                 Dre_Banner
# Quicksilver       Drro_Maximoff
# dtype: object


###################
## .get() method ##
###################

'''
.str.get(i) (works like .str[i] but handles out-of-bounds gracefully)
'''

print(s_heroes.str.get(0))
# Ironman           T
# CaptainAmerica    S
# Hulk              B
# Quicksilver       P
# dtype: object

print(s_heroes.str.get(-2))
# Ironman           r
# CaptainAmerica    r
# Hulk              e
# Quicksilver       f
# dtype: object

print(s_heroes.str.get(20))  # Out-of-bounds
# Ironman          NaN
# CaptainAmerica   NaN
# Hulk             NaN
# Quicksilver      NaN
# dtype: float64

#----------
## With dictionary-type series
#----------

s_ff4_dict = pd.Series(
    data = [
         {"name": "Reed_Richards", "code": "MrFantastic"},
         {"name": "Johnny_Storm", "code": "HumanTorch"},
         {"name": "Susan_Storm", "code": "InvisibleWoman"},
         {"name": "Ben_Grimm", "code": "TheThing"}
    ],
    name = "Fantastic Four"
)

print(s_ff4_dict)
# 0     {'name': 'Reed_Richards', 'code': 'MrFantastic'}
# 1       {'name': 'Johnny_Storm', 'code': 'HumanTorch'}
# 2    {'name': 'Susan_Storm', 'code': 'InvisibleWoman'}
# 3            {'name': 'Ben_Grimm', 'code': 'TheThing'}
# Name: Fantastic Four, dtype: object

print(s_ff4_dict.str.get("name"))
# 0    Reed_Richards
# 1     Johnny_Storm
# 2      Susan_Storm
# 3        Ben_Grimm
# Name: Fantastic Four, dtype: object

print(s_ff4_dict.str.get("code"))
# 0       MrFantastic
# 1        HumanTorch
# 2    InvisibleWoman
# 3          TheThing
# Name: Fantastic Four, dtype: object


#---------------------------------------------------------------------------------------------------------#
#------------------------------------- 2. Basic Transformations ------------------------------------------#
#---------------------------------------------------------------------------------------------------------#

##########################
## Case transformations ##
##########################

s_mixed = pd.Series(['Hello World', 'pandas is FUN', 'Data Science 101'])

#-----------
## .lower()
#-----------

print(s_mixed.str.lower())
# 0         hello world
# 1       pandas is fun
# 2    data science 101
# dtype: object

#-----------
## .upper()
#-----------

print(s_mixed.str.upper())
# 0         HELLO WORLD
# 1       PANDAS IS FUN
# 2    DATA SCIENCE 101
# dtype: object

#-----------
## .title()
#-----------

print(s_mixed.str.title())
# 0         Hello World
# 1       Pandas Is Fun
# 2    Data Science 101
# dtype: object

#--------------
## .capitalize()
#--------------

print(s_mixed.str.capitalize())
# 0         Hello world
# 1       Pandas is fun
# 2    Data science 101
# dtype: object

#--------------
## .swapcase()
#--------------

print(s_mixed.str.swapcase())
# 0         hELLO wORLD
# 1       PANDAS IS fun
# 2    dATA sCIENCE 101
# dtype: object

'''Swap case means converting uppercase letters to lowercase and vice versa.'''


###########################
## Information retrieval ##
###########################

#-----------
## .len()
#-----------

print(s_mixed.str.len())
# 0    11
# 1    13
# 2    16
# dtype: int64

#--------------
## .count(pattern)
#--------------

print(s_mixed.str.count('a'))
# 0    0
# 1    2
# 2    2
# dtype: int64

print(s_mixed.str.count(r'\d'))  # Count digits
# 0    0
# 1    0
# 2    3
# dtype: int64


######################
##     Stripping    ##
######################

s_spaced = pd.Series(['  hello  ', '  pandas  ', '  data science  '])

#-----------
## .strip()
#-----------
# Remove leading and trailing whitespace

print(s_spaced.str.strip())
# 0           hello
# 1          pandas
# 2    data science
# dtype: object

print(s_spaced.str.strip().to_list())
# ['hello', 'pandas', 'data science']

#------------
## .lstrip()
#------------
# Remove leading whitespace only

print(s_spaced.str.lstrip().to_list())
# ['hello  ', 'pandas  ', 'data science  ']

#------------
## .rstrip()
#------------
# Remove trailing whitespace only

print(s_spaced.str.rstrip().to_list())
# ['  hello', '  pandas', '  data science']


#---------------------------------------------------------------------------------------------------------#
#---------------------------------------- 3. Checking methods --------------------------------------------#
#---------------------------------------------------------------------------------------------------------#

###########################
## Character type checks ##
###########################

s_check = pd.Series(['Hello', 'WORLD', '123', '225.2', '⅕', '³', 'Hello123', '   ', ''])

#-----------
## .isalpha()
#-----------
# Check if all characters are alphabetic

print(s_check.str.isalpha())
# 0     True ('Hello')
# 1     True ('WORLD')
# 2    False
# 3    False
# 4     True
# 5    False
# 6    False
# 7    False
# 8    False
# dtype: bool

#-----------
## .isdigit()
#-----------
# Check if all characters are digits

print(s_check.str.isdigit())
# 0    False
# 1    False
# 2     True ('123')
# 3    False
# 4    False
# 5    True ('³')
# 6    False
# 7    False
# 8    False
# dtype: bool

#-----------
## .isnumeric()
#-----------
# Check if all characters are numeric (includes digits and numeric characters like fractions)

print(s_check.str.isnumeric())
# 0    False
# 1    False
# 2     True ('123')
# 3    False
# 4     True ('⅕')
# 5     True ('³')
# 6    False
# 7    False
# 8    False
# dtype: bool

#-----------
## .isdecimal()
#-----------
# Checks for characters used to form numbers in base 10

print(s_check.str.isdecimal())
# 0    False
# 1    False
# 2     True ('123')
# 3    False
# 4    False
# 5    False
# 6    False
# 7    False
# 8    False
# dtype: bool

#-----------
## .isalnum()
#-----------
# Check if all characters are alphanumeric (letters and numbers)

print(s_check.str.isalnum())
# 0     True ('Hello')
# 1     True ('WORLD')
# 2     True ('123')
# 3    False 
# 4     True ('⅕')
# 5     True ('³')
# 6     True ('Hello123')
# 7    False
# 8    False
# dtype: bool

#-----------
## .isspace()
#-----------
# Check if all characters are whitespace

print(s_check.str.isspace())
# 0    False
# 1    False
# 2    False
# 3    False
# 4    False
# 5    False
# 6    False
# 7     True ('   ')
# 8    False
# dtype: bool


#####################
##   Case checks   ##
#####################

s_check = pd.Series(['Hello', 'WORLD', 'Hello World', 'hello123', '   ', ''])

#-----------
## .isupper()
#-----------
# Check if all characters are uppercase

print(s_check.str.isupper())
# 0    False
# 1     True ('WORLD')
# 2    False
# 3    False
# 4    False
# 5    False
# dtype: bool

#-----------
## .islower()
#-----------
# Check if all characters are lowercase

print(s_check.str.islower())
# 0    False
# 1    False
# 2    False
# 3     True ('hello123')
# 4    False
# 5    False
# dtype: bool

#-----------
## .istitle()
#-----------
# Check if the string is titlecased (first letter of each word is uppercase)

print(s_check.str.istitle())
# 0     True ('Hello')
# 1    False
# 2     True  ('Hello World')
# 3    False
# 4    False
# 5    False
# dtype: bool


############################
##     Pattern checks     ##
############################

#-----------
## .startswith(prefix)
#-----------
# Check if strings start with the specified prefix

s_start = s = pd.Series(['bat', 'Bear', 'cat', np.nan])

print(s_start.str.startswith('b'))
# 0     True ('bat')
# 1    False
# 2    False
# 3      NaN
# dtype: object

print(s_start.str.startswith(pat = ('b', 'B'), na = False)) # Treat NaN as False
# 0     True
# 1     True
# 2    False
# 3    False
# dtype: bool

#-----------
## .endswith(suffix)
#-----------
# Check if strings end with the specified suffix

s_end = pd.Series(['bat', 'bear', 'caT', np.nan])

print(s_end.str.endswith('t'))
# 0     True ('bat')
# 1    False
# 2    False
# 3      NaN
# dtype: object

print(s_end.str.endswith(pat = ('t', 'T'), na = False)) # Treat NaN as False
# 0     True ('bat')
# 1    False 
# 2     True ('caT')
# 3    False
# dtype: bool

#-----------
## .contains(pattern)
#-----------
# Check if strings contain the specified pattern (can be a substring or regex)

s_contain = pd.Series(['Mouse', 'dog', 'house and parrot', '23', np.nan])

print(s_contain.str.contains(pat = 'og', regex = False))
# 0    False
# 1     True ('dog')
# 2    False
# 3    False
# 4      NaN
# dtype: object

print(s_contain.str.contains(pat = 'oG', regex = False))
# 0    False
# 1    False
# 2    False
# 3    False
# 4      NaN
# dtype: object

print(s_contain.str.contains(pat = 'oG', case = False, regex = False, na = False)) # Case insensitive, Treat NaN as False
# 0    False
# 1     True ('dog')
# 2    False
# 3    False
# 4    False
# dtype: bool

print(s_contain.str.contains(pat = r"\d|parrot|Mo", regex = True, na = False)) # Regex pattern, Treat NaN as False
# 0     True ('Mouse' contains 'Mo')
# 1    False
# 2     True ('house and parrot' contains 'parrot')
# 3     True ('23' contains digit '\d')
# 4    False
# dtype: bool


#---------------------------------------------------------------------------------------------------------#
#--------------------------------------- 4. Split and Partion --------------------------------------------#
#---------------------------------------------------------------------------------------------------------#

#######################
##     Splitting     ##
#######################

s_split = pd.Series(['apple_banana_cherry', 'dog_cat', 'one_two_three_four', np.nan])

#-----------
## .split(delimiter)
#-----------
# Split strings by the specified delimiter
# By default, pat='\s+' (whitespace) and n=-1 (all occurrences)

print(s_split.str.split('_'))
# 0    [apple, banana, cherry]
# 1                 [dog, cat]
# 2    [one, two, three, four]
# 3                        NaN
# dtype: object

print(s_split.str.split(pat = '_', n = 2))  # Split up to 2 delimiters only (results in at most 3 parts)
# 0    [apple, banana, cherry]
# 1                 [dog, cat]
# 2     [one, two, three_four]
# 3                        NaN
# dtype: object

print(s_split.str.split(pat = '_', expand= True))  # Expand into separate columns
#        0       1       2     3
# 0  apple  banana  cherry  None
# 1    dog     cat    None  None
# 2    one     two   three  four
# 3    NaN     NaN     NaN   NaN

#------------
## .rsplit(delimiter)
#------------
# Split strings by the specified delimiter from the right
# By default, pat='\s+' (whitespace) and n=-1 (all occurrences)

print(s_split.str.rsplit('_'))
# 0    [apple, banana, cherry]
# 1                 [dog, cat]
# 2    [one, two, three, four]
# 3                        NaN
# dtype: object

print(s_split.str.rsplit(pat = '_', n = 2))  # Split up to 2 delimiters only from the right (results in at most 3 parts)
# 0    [apple, banana, cherry]
# 1                 [dog, cat]
# 2     [one_two, three, four]
# 3                        NaN
# dtype: object

'''
.str.split() => [one, two, three_four]
.str.rsplit() => [one_two, three, four]
'''

print(s_split.str.rsplit(pat = '_', n = 2, expand= True))  # Expand into separate columns
#          0       1       2
# 0    apple  banana  cherry
# 1      dog     cat    None
# 2  one_two   three    four
# 3      NaN     NaN     NaN


#########################
##     Partioning      ##
#########################

s_partition = pd.Series(['apple-banana-cherry', 'dog-cat', 'one-two-three-four', np.nan])

#--------------
## .partition(separator)
#--------------
# Split strings at the first occurrence of the specified separator
# By default, sep=' ' (whitespace)

print(s_partition.str.partition('-'))
#        0    1               2
# 0  apple    -   banana-cherry
# 1    dog    -             cat
# 2    one    -  two-three-four
# 3    NaN  NaN             NaN

print(s_partition.str.partition(sep = 'a'))  # Split at first 'a'
#                     0    1                   2
# 0                        a  pple-banana-cherry
# 1               dog-c    a                   t
# 2  one-two-three-four                         
# 3                 NaN  NaN                 NaN

print(s_partition.str.partition(sep = '-', expand = False)) # Return as tuples, not expanded DataFrame
# 0    (apple, -, banana-cherry)
# 1                (dog, -, cat)
# 2     (one, -, two-three-four)
# 3                          NaN
# dtype: object

#----------------
## .rpartition(separator)
#----------------
# Split strings at the last occurrence of the specified separator
# By default, sep=' ' (whitespace)

print(s_partition.str.rpartition('-'))
#                0    1       2
# 0   apple-banana    -  cherry
# 1            dog    -     cat
# 2  one-two-three    -    four
# 3            NaN  NaN     NaN

print(s_partition.str.rpartition(sep = 'a'))  # Split at last 'a'
#              0    1                   2
# 0  apple-banan    a             -cherry
# 1        dog-c    a                   t
# 2                    one-two-three-four
# 3          NaN  NaN                 NaN

print(s_partition.str.rpartition(sep = '-', expand = False)) # Return as tuples, not expanded DataFrame
# 0    (apple-banana, -, cherry)
# 1                (dog, -, cat)
# 2     (one-two-three, -, four)
# 3                          NaN
# dtype: object


#---------------------------------------------------------------------------------------------------------#
#------------------------------------------ 5. Joinning --------------------------------------------------#
#---------------------------------------------------------------------------------------------------------#

'''
join(separator) - Join list elements with separator
'''

s_join = pd.Series([['apple', 'banana', 'cherry'], ['dog', 'cat'], ['one', 'two', 'three', 'four'], np.nan])

print(s_join.str.join('-'))
# 0    apple-banana-cherry
# 1                dog-cat
# 2     one-two-three-four
# 3                    NaN
# dtype: object

print(s_join.str.join(sep = ' || '))
# 0      apple || banana || cherry
# 1                     dog || cat
# 2    one || two || three || four
# 3                            NaN
# dtype: object


#---------------------------------------------------------------------------------------------------------#
#--------------------------------------- 12. Real applications -------------------------------------------#
#---------------------------------------------------------------------------------------------------------#

###################
## Data cleaning ##
###################

# Clean messy name data
messy_names = pd.Series(['  john doe  ', 'JANE SMITH', 'bob-johnson'])
clean_names = (messy_names
               .str.strip()
               .str.replace('-', ' ')
               .str.title()
               .str.replace(r'\s+', ' ', regex=True))


######################
## Email processing ##
######################

emails = pd.Series(['user@example.com', 'ADMIN@SITE.ORG', 'invalid.email'])
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Validate and extract components
is_valid = emails.str.match(email_pattern)
domains = emails.str.extract(r'@([^.]+\..*)')
usernames = emails.str.extract(r'^([^@]+)@')
