from z3 import *
s = SolverFor("QF_LIA")
# (set-logic QF_LIA)
s.set("model.completion", True)
# (set-option :produce-models true)
# s = Solver()

out_a0, in_a0, out_a1, out_a2, out_b0, in_b0 = Ints('out_a0 in_a0 out_a1 out_a2 out_b0 in_b0')

phi_0 = in_a0==in_b0
phi_a = And(And((out_a0==in_a0), out_a1==out_a0 * in_a0), out_a2==out_a1*in_a0)
phi_b = out_b0 == (in_b0*in_b0)*in_b0
phi_1 = out_a2 == out_b0

s.add(Not(Implies(And(And(phi_0, phi_a), phi_b), phi_1)))

print(s.check())
