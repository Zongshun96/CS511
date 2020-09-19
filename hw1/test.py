from z3 import *

x,y,z = Bools('x y z')

# (x \land y) \lor (x \land z) \lor (y \land z)
phi = Or (And(x,y), And(x,z), And(y,z))

# (x \lor y) \land (x \lor z) \land (y \lor z)
psi = And (Or(x,y), Or(x,z), Or(y,z))

s = Solver()

# constraint: check sat for not equal
s.add(Not (phi == psi))
print (s.check())
