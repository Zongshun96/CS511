# please use the same format as in the sample lists, and make sure the working directory has the readin file
# the solve step was adapted from the hw7 solution.

# to run:    python3 q5.py [inputfilename](at the current working directory or full pathname)


import ast
from z3 import *
opt = Solver()

w = [100, 100, 100, 1, 100]
c = [[0, 7, 1, 0, 8],
[7, 0, 5, 4, 3],
[1, 5, 0, 2, 6],
[0, 4, 2, 0, 1],
[8, 3, 6, 1, 0]]

filename = sys.argv[1]
with open(filename, "r") as f:
    l1 = f.readline().split(" ", 2)[2]
    w = eval(l1)
    l2 = f.read().replace("\n", "").split(" ", 2)[2]
    c = eval(l2)


x_list = Ints(['x'+str(i) for i in range(len(w))])
not_x_list = Ints(['not_x'+str(i) for i in range(len(w))])

for i in range(len(w)):
    opt.add(Or(x_list[i] == 0, x_list[i] == 1))
    opt.add(Or(not_x_list[i] == 0, not_x_list[i] == 1))
    opt.add(Not(not_x_list[i] == x_list[i]))

exp = 0
for i in range(len(c)):
    for j in range(i, len(c[i])):
        exp = exp + c[i][j]*(x_list[i]*not_x_list[j]+not_x_list[i]*x_list[j])
# print(exp)


# Objective function
obj = Int("obj")
opt.add(obj == exp)

# Solve
if opt.check() == unsat:
	print("Unsatisfiable!")
	quit()
while opt.check() == sat:
	model = opt.model()
	opt.add(obj > model[obj])
print(model)