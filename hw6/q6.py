from z3 import *
s = SolverFor("QF_LIA")
# (set-logic QF_LIA)
s.set("model.completion", True)
# (set-option :produce-models true)
# s = Solver()

in_a    = 2
m       = 1
in_b    = 2
n       = 1

workfile = input("Enter workfile:(default in_a=2; m=1; in_b=2; n=1)")
try:
    with open("./"+workfile) as f:
        read_data = f.readline()
        in_a = int(read_data)
        read_data = f.readline()
        m = int(read_data)
        read_data = f.readline()
        in_b = int(read_data)
        read_data = f.readline()
        n = int(read_data)
except Exception as err:
    print(err, "go with defualt settings")

in_a_, in_b_ = Ints('in_a_ in_b_')

out_alist = Ints(['Inta'+str(i) for i in range(m+1)])
phi_a_ = (out_alist[0]== in_a_)
for i in range(m):
    phi_a_ = And(phi_a_, out_alist[i+1]==out_alist[i] * in_a_)

out_blist = Ints(['Intb'+str(i) for i in range(n+1)])
phi_b_ = (out_blist[0]==in_b_)
for i in range(n):
    phi_b_ = And(phi_b_, out_blist[i+1]==out_blist[i] * out_blist[i])


s.add(in_a_ == in_a)
s.add(in_b_ == in_b)
s.add(phi_a_)
s.add(phi_b_)
s.add(out_alist[-1] == out_blist[-1])

print(s.check() == sat)
