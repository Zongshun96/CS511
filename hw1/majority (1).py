# Execute this script from the Python prompt by issuing:
# >>> execfile ('majority.py')

from z3 import *

# declaring propositional variables x,y
x,y,z = Bools('x y z')

# defining phi - a DNF for the majority function:
phi = Or (And(x,y), And(x,z), And(y,z))

# defining phi - a CNF for the majority function:
psi = And (Or(x,y), Or(x,z), Or(y,z)) 

# adding a constraint that phi and psi are equivalent,
# by negating the equivalence (phi == psi), i.e. (Not (phi == psi))
# should be unsatisfiable:
s = Solver()
s.add(Not (phi == psi))

# check if it is satisfiable
print s.check()
