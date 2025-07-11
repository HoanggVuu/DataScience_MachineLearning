'''
================================================================================

                CORE IDEAS AND EXAMPLE OF QUASICONVEX FUNCTIONS

================================================================================

## Definition
A function f: ℝⁿ → ℝ is quasiconvex if for all x, y ∈ dom(f) and all λ ∈ [0,1]:
    f(λx + (1–λ)y) ≤ max{f(x), f(y)}  

Equivalently, all its sublevel sets     
    C_α(f) = {x ∈ dom(f) : f(x) ≤ α}  
are convex for every α ∈ ℝ [1][2].


## Geometric Interpretation
Quasiconvexity means “no valleys” deeper than the higher of two endpoints. 
Any line segment through the graph never rises above the maximum of its endpoints. 
Sublevel sets form nested convex regions.


## Relation to Convexity
- Every convex function is quasiconvex, but not vice versa.  
- A quasiconvex function need not satisfy the first-order support condition ∇f(x)ᵀ(y–x) ≥ 0.


## First-Order Characterization (Differentiable Case)
If f is differentiable, f is quasiconvex if and only if for all x, y:
    f(y) ≤ f(x) ⇒ ∇f(x)ᵀ(y–x) ≤ 0  
Gradient at x points “uphill” away from any lower-value point.


## Example: Ratio of Affine Functions:  
    f(x) = (aᵀx + b)/(cᵀx + d), dom(f) = {x : cᵀx + d > 0}  

This function is quasiconvex when cᵀx + d > 0 and denominator positive, since its sublevel sets  
    {x : (aᵀx + b)/(cᵀx + d) ≤ α} ⇔ {x : aᵀx + b – α(cᵀx + d) ≤ 0}  
are halfspaces, hence convex.


## Key Properties
1. **Preservation under Monotone Transformations**: 
   If φ is nondecreasing and f is quasiconvex, then φ∘f is quasiconvex.  

2. **Maximum of Quasiconvex Functions**: 
   The pointwise maximum of any family of quasiconvex functions is quasiconvex. 

3. **Quasiconcavity Dual**: 
   –f is quasiconcave whenever f is quasiconvex.

   
## Why It Matters
Quasiconvex functions arise in fractional programming, economics (utility ratios), and robustness analysis. 
They allow efficient level-set methods and generalized gradient algorithms even when convexity fails.

================================================================================

'''