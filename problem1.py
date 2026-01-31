import sympy as sp

#Problem 1
x, y, r = sp.symbols('x y r')


eq1 = 2*x**2 + 3*y**2 - r
eq2 = y - (2*x + 1)

solutions =  sp.solve([eq1, eq2], [x, y])
sol =[]

for s in solutions:
    sol.append({x: s[0], y: s[1]})