import numpy as np
from sympy import Symbol, Eq, solve, cos, pprint, solveset, oo, nonlinsolve, nsolve, Matrix, sin
import math 

a = Symbol('a')
x = Symbol('x')
b = 150
c = 200 
d = 499
e = 1267
y = 16
j11 = 2*(a+c)-2*d*cos(x) - 2*(a+b)
j12 = 2*(a+b)*d*sin(x)
j21 = 2*(a+c)-2*e*cos(x-y)-2*a
j22 = 2*(a+c)*e*sin(x-y)
f = Matrix([j11, j12])

J = f.jacobian(f)
print(J)

# x, y = symbols('x y')


# eq1 = Eq((a+200)**2 + 499**2 - 2 * (a + 200) * 499 * cos(x) - (a + 150)**2 )
# eq2 = Eq((a + 200)**2 + 1267**2 - 2*(a+200) * 1267 * cos(x - 16) - a**2)



# eq1 = Eq(x + y - 5)
# eq2 = Eq(x - y + 3)





#sol_dict = nonlinsolve((eq1,eq2), (a, x))
# sol_dict = solve((eq1,eq2), (a, x))
# sol_dict = solve((eq1,eq2), (x, y))

# print(sol_dict)



