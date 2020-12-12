# python3 q6.py 4

import functools
import sys
from z3 import *
import random
import math

if len(sys.argv) != 2:
    print("usage: ", "python3 q6.py [n]")
    sys.exit()




n = int(sys.argv[1])
# n = 4

qboard = []
for i in range(n):
    row = Bools(['q'+str(i)+str(j) for j in range(n)])
    qboard.append(row)

rboard = []
for i in range(n):
    row = Bools(['r'+str(i)+str(j) for j in range(n)])
    rboard.append(row)

phi_list=[]




# 1
I = random.sample(range(len(qboard)), k=math.ceil(n/3))
temp_row_result = []
for i in I:
    temp_row_result.append(Or(*qboard[i]))
# phi_1 = functools.reduce(And,temp_row_result)
phi_1=And(*temp_row_result)
phi_list.append(phi_1)

#2
N = list(set(range(len(qboard))) - set(I))
temp_row_result = []
for n_ in N:
    temp_row_result.append(Or(*rboard[n_]))
# phi_2 = functools.reduce(And,temp_row_result)
phi_2 = And(*temp_row_result)
phi_list.append(phi_2)

#3
temp_row_result = []
# for i in range(n):
#     print(i)
#     temp_row_result.append(list(map(lambda x, y: Implies(x, Not(y)), qboard[i], rboard[i])))
for i in range(n):
    for j in range(n):
        temp_row_result.append(Implies(qboard[i][j], Not(rboard[i][j])))

# phi_3 = functools.reduce(And,temp_row_result)
phi_3=And(*temp_row_result)
phi_list.append(phi_3)

#4
temp_row_result = []
for i in range(n):
    for j in range(n):
        temp_row_result_1 = []
        for l in range(n):
            if l != j:
                temp_row_result_1.append(Not(qboard[i][l]))
                temp_row_result_1.append(Not(rboard[i][l]))
        # temp_row_result_1 = functools.reduce(And,temp_row_result_1)
        temp_row_result_1=And(*temp_row_result_1)
        temp_row_result.append(Implies(qboard[i][j], temp_row_result_1))
# phi_4 = functools.reduce(And,temp_row_result)
phi_4=And(*temp_row_result)
phi_list.append(phi_4)

#5
temp_row_result = []
for i in range(n):
    for j in range(n):
        temp_row_result_1 = []
        for k in range(n):
            if k != i:
                temp_row_result_1.append(Not(qboard[k][j]))
                temp_row_result_1.append(Not(rboard[k][j]))
        # temp_row_result_1 = functools.reduce(And,temp_row_result_1)
        temp_row_result_1 = And(*temp_row_result_1)
        temp_row_result.append(Implies(qboard[i][j], temp_row_result_1))
# phi_5 = functools.reduce(And,temp_row_result)
phi_5=And(*temp_row_result)
phi_list.append(phi_5)

#6
temp_row_result = []
for i in range(n):
    for j in range(n):
        temp_row_result_1 = []
        for l in range(n):
            if l != j:
                temp_row_result_1.append(Not(qboard[i][l]))
                temp_row_result_1.append(Not(rboard[i][l]))
        # temp_row_result_1 = functools.reduce(And,temp_row_result_1)
        temp_row_result_1 = And(*temp_row_result_1)
        temp_row_result.append(Implies(rboard[i][j], temp_row_result_1))
# phi_6 = functools.reduce(And,temp_row_result)
phi_6=And(*temp_row_result)
phi_list.append(phi_6)

#7
temp_row_result = []
for i in range(n):
    for j in range(n):
        temp_row_result_1 = []
        for k in range(n):
            if k != i:
                temp_row_result_1.append(Not(qboard[k][j]))
                temp_row_result_1.append(Not(rboard[k][j]))
        # temp_row_result_1 = functools.reduce(And,temp_row_result_1)
        temp_row_result_1 = And(*temp_row_result_1)
        temp_row_result.append(Implies(rboard[i][j], temp_row_result_1))
# phi_7 = functools.reduce(And,temp_row_result)
phi_7=And(*temp_row_result)
phi_list.append(phi_7)

#8
temp_row_result = []
for i in range(n):
    for j in range(n):

        temp_row_result_1 = []
        for k in range(n):
            l = k-(i-j)
            if k != i and l != j and k >= 0 and k < n and l>=0 and l < n:
                temp_row_result_1.append(Not(qboard[k][l]))
                temp_row_result_1.append(Not(rboard[k][l]))
        if temp_row_result_1 != []:
            # temp_row_result_1 = functools.reduce(And,temp_row_result_1)
            temp_row_result_1 = And(*temp_row_result_1)
            temp_row_result.append(Implies(qboard[i][j], temp_row_result_1))
        else:
            temp_row_result.append(Implies(qboard[i][j], True))
# phi_8 = functools.reduce(And,temp_row_result)
phi_8=And(*temp_row_result)
phi_list.append(phi_8)

#9
temp_row_result = []
for i in range(n):
    for j in range(n):

        temp_row_result_1 = []
        for k in range(n):
            l = (i+j)-k
            if k != i and l != j and k >= 0 and k < n and l>=0 and l < n:
                temp_row_result_1.append(Not(qboard[k][l]))
                temp_row_result_1.append(Not(rboard[k][l]))
        if temp_row_result_1 != []:
            # temp_row_result_1 = functools.reduce(And,temp_row_result_1)
            temp_row_result_1 = And(*temp_row_result_1)
            temp_row_result.append(Implies(qboard[i][j], temp_row_result_1))
        else:
            temp_row_result.append(Implies(qboard[i][j], True))
# phi_9 = functools.reduce(And,temp_row_result)
phi_9=And(*temp_row_result)
phi_list.append(phi_9)

import copy

for i in range(len(phi_list)):
    s = Solver()
    assumption_list = copy.deepcopy(phi_list)  # fastest way to copy
    conclusion = copy.deepcopy(assumption_list[i])
    del assumption_list[i]
    
    # phi = Implies(And(*assumption_list), conclusion)
    phi = And(And(*assumption_list), Not(conclusion))
    s.add(phi)
    result = s.check()
    print("Check assumption ", i, "the result is ", result != sat)
    if result != sat:
        try:
            s = Solver()
            s.add(And(*assumption_list))
            s.check()
            m = s.model()
            # print(m)
            table = [["None" for i in range(n)] for j in range(n)]
            for i in range(n):
                for j in range(n):
                    if is_true(m[qboard[i][j]]):
                        table[i][j] = "Q"
            for i in range(n):
                for j in range(n):
                    if is_true(m[rboard[i][j]]):
                        table[i][j] = "R"
            from pprint import pprint
            pprint(table)
        except Exception as inst:
            print(inst) 



# # phi = functools.reduce(And,phi_list)
# phi = And(*phi_list)

# s.add(phi)
# print(s.check() == sat)
# m = s.model()
# # print(m)
# table = [["None" for i in range(n)] for j in range(n)]
# for i in range(n):
#     for j in range(n):
#         if is_true(m[qboard[i][j]]):
#             table[i][j] = "Q"
# for i in range(n):
#     for j in range(n):
#         if is_true(m[rboard[i][j]]):
#             table[i][j] = "R"
# from pprint import pprint
# pprint(table)