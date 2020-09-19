# > python3 parity.py

from z3 import *

p1,p2,p3,p4 = Bools('p1 p2 p3 p4')

s = Solver()

# match F cases in each clause
phi = And(Or(Not(p1), p2, p3, p4), Or(p1, Not(p2), p3, p4), Or (p1, p2, Not(p3), p4), Or(p1, p2, p3, Not(p4)),
            Or(Not(p1), Not(p2), Not(p3), p4), Or(Not(p1), Not(p2), p3, Not(p4)), Or(Not(p1), p2, Not(p3), Not(p4)), Or(p1, Not(p2), Not(p3), Not(p4)))
# match T cases in each clause
psi = Or(And(p1, p2, p3, p4), And(Not(p1), Not(p2), Not(p3), Not(p4)), And(p1, p2, Not(p3), Not(p4)), And(Not(p1), Not(p2), p3, p4),
         And(Not(p1), p2, Not(p3), p4), And(Not(p1), p2, p3, Not(p4)), And(p1, Not(p2), Not(p3), p4), And(p1, Not(p2), p3, Not(p4)))
# same as XOR
theta = p1 == (p2 == (p3 == p4))

# # constraint: check sat for not equal
s.add(Not(phi == theta))
s.add(Not(theta == psi))
s.add(Not(psi == phi))
print (s.check())
