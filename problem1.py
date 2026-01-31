import sympy as sp

### Replace with your own code (begin) ###
x, y, r= sp.symbols('x, y, r')




eq1 = sp.Eq(2*x**2 + 3*y**2, r)
eq2 = sp.Eq(2*x + 1, y)

sol = sp.solve([eq1, eq2], [x, y], dict=True)
### Replace with your own code (end) ###
