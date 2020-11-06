# please use the same format as in the sample lists, and make sure the working directory has the readin file
# to run: python3 q5.py


import ast
from z3 import *
opt = Optimize() # find min

variable_d = {}
neg_var_d = {}


w = [100, 100, 100, 1, 100]
c = [[0, 7, 1, 0, 8],
[7, 0, 5, 4, 3],
[1, 5, 0, 2, 6],
[0, 4, 2, 0, 1],
[8, 3, 6, 1, 0]]

print(c)
# try:
#     filename = input("type the filename or use default input: ")
#     with open("./"+filename, 'r') as f:
#         input_list = ast.literal_eval(f.read())
# except Exception as e:
#     print(e)
#     print("go with default")




x_list = Ints(['x'+str(i) for i in range(len(w))])
not_x_list = Ints(['not_x'+str(i) for i in range(len(w))])

for i in range(len(w)):
    opt.add(Or(x_list[i] == 0, x_list[i] == 1))
    opt.add(Or(not_x_list[i] == 0, not_x_list[i] == 1))
    opt.add(Not(not_x_list[i] == x_list[i]))

exp = 0
# weight of S
for i in range(len(w)):
    exp = exp + w[i]*x_list[i]

# capacity of edge in S
temp = 0
for i in range(len(c)):
    for j in range(len(c[i])):
        temp = temp + c[i][j]*x_list[i]*x_list[j]

# if there are edges in S, penalize the weight.
exp = exp - (1+max(w))*temp



opt.maximize(exp)
check_result = opt.check()  
print(check_result)
print(check_result==sat)
print(opt.model())
