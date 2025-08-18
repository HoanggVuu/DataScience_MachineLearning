'''
4.3 Formulating constraints in CVXPY. Below we give several convex constraints on scalar variables x, y, and z. 
Express each one as a set of DCP compliant constraints in CVXPY. 

To check DCP compliance, use the .is_DCP() method on each constraint.

(a) 1/x + 1/y ≤ 1,  x ≥ 0,  y ≥ 0.

(b) xy ≥ 1,  x ≥ 0,  y ≥ 0.

(c) (x + y)² / √y ≤ x - y + 5  (with implicit constraint y ≥ 0).

(d) x + z ≤ 1 + √(xy - z²),  x ≥ 0,  y ≥ 0.  Hint.  √(xy - z²) = √( y(x - z² / y) ).
'''

# Disciplined convex programming (DCP) is a system for constructing mathematical expressions 
# with known curvature from a given library of base functions
# CVXPY uses DCP to ensure that the specified optimization problems are convex.

import cvxpy as cp

x = cp.Variable(name = "x")
y = cp.Variable(name = "y")
z = cp.Variable(name = "z")

#--------------------------
## (a) 1/x + 1/y ≤ 1,  x ≥ 0,  y ≥ 0.
#--------------------------

constraints_a = [
    1/x + 1/y <= 1,
    -x <= 0, # x ≥ 0
    -y <= 0, # y ≥ 0
]

for constraint in constraints_a:
    print(f"{constraint} ___ {constraint.is_dcp()} DCP")
# 1.0 / x + 1.0 / y <= 1.0 ___ False DCP
# -x <= 0.0 ___ True DCP
# -y <= 0.0 ___ True DCP