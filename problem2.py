#Problem 2
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

x, y, r = sp.symbols('x y r')

#initial values
A = 2
B = 3
C = 2
D = 1
r_value = 10
                                    #Ellipse: (x^2)/a^2 + (y^2)/b^2 = 1
a = np.abs(sp.sqrt(r_value/(A)))    #Ax^2 + Bx^2 = r
b = np.abs(sp.sqrt(r_value/(B)))    #(A/r)x^2 + (B/r)x^2 = 1
print(f"a = {a}")                   #(A/r) = 1/a^2, (B/r) = 1/b^2
print(f"b = {b}")                   #   a = +-sqrt(r/A), b = +-sqrt(r/B)

eq1 = A*x**2 + B*y**2 - r
eq2 = y - (C*x + D)


#point of intersection
solutions =  sp.solve([eq1, eq2], [x, y])
sol =[]
for s in solutions:
    sol.append({x: s[0], y: s[1]})
print(sol)

#for the specific value of "r"
sol_r = []
for s in sol:
    x_val = s[x].subs(r, r_value)
    y_val = s[y].subs(r, r_value)
    sol_r.append({x: x_val, y: y_val})
print(sol_r)

x_val = []
y_val = []
for s in range(len(sol_r)):
    x_val.append(sol_r[s][x])
    y_val.append(sol_r[s][y])
print(f"\nValues of x: {x_val}")
print(f"Values of y: {y_val}\n")

#parametric representation
t = np.linspace(-1*np.pi, np.pi, 100)
y_vals_eq2_graph = C * t + D

#plot
plt.plot( a*np.cos(t) , b*np.sin(t), label=f'${A}x^2 + {B}y^2 = {r_value}$' )
plt.plot(t, y_vals_eq2_graph, label=f'$y = {C}x + {D}$')

plt.scatter(x_val, y_val, color='red', zorder=3, label=f'Solution Point(r={r_value})')

#additional info: a, b
plt.text(1, -4, f'$a = \\sqrt{{\\frac{{{r_value}}}{{{A}}}}}$', fontsize=14, ha='center')
plt.text(2.5, -4, f'$b = \\sqrt{{\\frac{{{r_value}}}{{{B}}}}}$', fontsize=14, ha='center')


plt.xlabel('x')
plt.ylabel('y')
plt.title(r'$System\ of\ Equations  \quad \frac{x^2}{a^2} + \frac{y^2}{b^2} = r$',fontsize=14)
plt.legend()
plt.grid(color='lightgray',linestyle='--')
plt.savefig('Problem2.pdf')
plt.show()