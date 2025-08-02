# All basic datatypes in Python: https://www.w3schools.com/python/python_datatypes.asp
# Python numbers: int, float, complex -> https://www.w3schools.com/python/python_numbers.asp

# Casting is the act of converting a variable's original datatype into another one
# Casting reference link: https://www.w3schools.com/python/python_casting.asp

## int() to convert into integer number
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

## float() to convert into float number
x = float(1)      # x will be 1.0
y = float(2.8)    # y will be 2.8
z = float("3")    # z will be 3.0
w = float("4.2")  # w will be 4.2
u = float(".2")   # u will be 0.2
v = float("-.51") # v will be -0.51

## complex() to convert into complex number
x = complex(1)       # x will be (1+0j)
y = complex("3+5j")  # y will be (3+5j)

## str() to convert into string
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'


#-----------------------------------------------------------------------------------------------------------------#
#------------------------------------ Exception with "infinity" and "inf" ----------------------------------------#
#-----------------------------------------------------------------------------------------------------------------#

##########################
## float() and infinity ##
##########################

float("infinity") # inf
float("+infinity") # inf
float("-infinity") # -inf

float("inf") # inf
float("+inf") # inf
float("-inf") # -inf

float("inf") == float("+infinity") # True


############################
## complex() and infinity ##
############################

#--------
## real part
#--------

complex("infinity+2j") # (inf+2j)
complex("+infinity+2j") # (inf+2j)
complex("-infinity+2j") # (-inf+2j)

complex("inf+2j") # (inf+2j)
complex("+inf+2j") # (inf+2j)
complex("-inf+2j") # (-inf+2j)


#--------
## image part
#--------

complex("3+infinityj") # (3+infj)
complex("3-infinityj") # (3-infj)

complex("3+infj") # (3+infj)
complex("3-infj") # (3-infj)