'''
1. Binding:
  + dr.bind_rows()
  + dr.bind_cols()

2. Joining:
  + dr.inner_join()
  + dr.left_join()
  + dr.right_join()
  + dr.full_join()
  + multi-column joins
  + dr.semi_join()
  + dr.anti_join()
  + dr.cross_join()
  + dr.nest_join()
'''

import datar.all as dr
from datar import f
import pandas as pd

# Suppress specific warnings from pipda
import warnings
from pipda.utils import PipeableCallCheckWarning
warnings.filterwarnings("ignore", category=PipeableCallCheckWarning)


#-----------------------------------------------------------------------------------------------------------#
#----------------------------------------------- 1. Binding ------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------#

# Create sample DataFrames
df_origin = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'C': ['C0', 'C1', 'C2', 'C3']
})

df_ver_1 = pd.DataFrame({
    'A': ['A4', 'A5', 'A6', 'A7'],
    'B': ['B4', 'B5', 'B6', 'B7'],
    'C': ['C4', 'C5', 'C6', 'C7']
})

df_ver_2 = pd.DataFrame({
    'A': ['A8', 'A9', 'A10', 'A11'],
    'B': ['B8', 'B9', 'B10', 'B11'],
    'C': ['C8', 'C9', 'C10', 'C11']
})

df_hor_1 = pd.DataFrame({
    'D': ['D0', 'D1', 'D2', 'D3'],
    'E': ['E0', 'E1', 'E2', 'E3'],
    'F': ['F0', 'F1', 'F2', 'F3']
})

df_hor_2 = pd.DataFrame({
    'G': ['G0', 'G1', 'G2', 'G3'],
    'H': ['H0', 'H1', 'H2', 'H3'],
    'I': ['I0', 'I1', 'I2', 'I3']
})

####################
## dr.bind_rows() ##
####################

# Original DataFrame
print(df_origin)
#     A   B   C
# 0  A0  B0  C0
# 1  A1  B1  C1
# 2  A2  B2  C2
# 3  A3  B3  C3

df_bind_rows = dr.bind_rows(df_origin, df_ver_1)
print(df_bind_rows)
#          A        B        C
#   <object> <object> <object>
# 0       A0       B0       C0
# 1       A1       B1       C1
# 2       A2       B2       C2
# 3       A3       B3       C3
# 4       A4       B4       C4
# 5       A5       B5       C5
# 6       A6       B6       C6
# 7       A7       B7       C7

df_bind_rows = dr.bind_rows(df_origin, df_ver_1, df_ver_2)
print(df_bind_rows)
#          A        B        C
#    <object> <object> <object>
# 0        A0       B0       C0
# 1        A1       B1       C1
# 2        A2       B2       C2
# 3        A3       B3       C3
# 4        A4       B4       C4
# 5        A5       B5       C5
# 6        A6       B6       C6
# 7        A7       B7       C7
# 8        A8       B8       C8
# 9        A9       B9       C9
# 10      A10      B10      C10
# 11      A11      B11      C11

####################
## dr.bind_cols() ##
####################

# Original DataFrame
print(df_origin)
#     A   B   C
# 0  A0  B0  C0
# 1  A1  B1  C1
# 2  A2  B2  C2
# 3  A3  B3  C3

df_bind_cols = dr.bind_cols(df_origin, df_hor_1)
print(df_bind_cols)
#          A        B        C        D        E        F
#   <object> <object> <object> <object> <object> <object>
# 0       A0       B0       C0       D0       E0       F0
# 1       A1       B1       C1       D1       E1       F1
# 2       A2       B2       C2       D2       E2       F2
# 3       A3       B3       C3       D3       E3       F3

df_bind_cols = dr.bind_cols(df_origin, df_hor_1, df_hor_2)
print(df_bind_cols)
#          A        B        C        D        E        F        G        H        I
#   <object> <object> <object> <object> <object> <object> <object> <object> <object>
# 0       A0       B0       C0       D0       E0       F0       G0       H0       I0
# 1       A1       B1       C1       D1       E1       F1       G1       H1       I1
# 2       A2       B2       C2       D2       E2       F2       G2       H2       I2
# 3       A3       B3       C3       D3       E3       F3       G3       H3       I3