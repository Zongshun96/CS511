import functools
from z3 import *
s = Optimize()

CPTs = [["x", [[[],["x","1"],0.7], [[],["x","0"],0.3]]], 
        ["y", [[[["x", "1"]],["y","1"],0.2], [[["x", "0"]],["y","0"],0.2], [[["x", "1"]],["y","0"],0.8], [[["x", "0"]],["y","1"],0.8]]]]

Os = [["x", "1"]]


RV_dict = {}
RV_prob_dict = {}

for V,T in CPTs:
    for entry in T: # base RV
        if entry[0] == []:
            if entry[1][0] not in RV_dict:
                temp = Int(entry[1][0])
                RV_dict[entry[1][0]] = temp
            s.add_soft(RV_dict[entry[1][0]] == eval(entry[1][1]), entry[2])
            RV_prob_dict[entry[1][0]] = entry[2]
            # if entry[1][1] == "1":
            #     s.add_soft(RV_dict[entry[1][0]] == 1, entry[2])
            #     RV_prob_dict[entry[1][0]] = entry[2]
            # if entry[1][1] == "0":
            #     s.add_soft(RV_dict[entry[1][0]] == 0, entry[2])
            #     RV_prob_dict[entry[1][0]] = entry[2]

while not len(CPTs) == len(RV_dict):
    for V,T in CPTs:
        for entry in T: # base RV
            if not entry[0] == []:
                depandancy = []
                conditional_prob = 1
                for dependants in entry[0]:
                    if not dependants[0] in RV_dict:
                        break
                # for dependants in entry[0]:
                    if dependants[1] == "1":
                        # s.add_soft(RV_dict[dependants[0]] == 1)
                        depandancy.append(RV_dict[dependants[0]] == 1)
                        conditional_prob = conditional_prob*RV_prob_dict[dependants[0]]
                    if dependants[1] == "0":
                        # s.add_soft(RV_dict[dependants[0]] == 0)
                        depandancy.append(RV_dict[dependants[0]] == 0)
                        conditional_prob = conditional_prob*RV_prob_dict[dependants[0]]
                if entry[1][0] not in RV_dict:
                    temp = Int(entry[1][0])
                    RV_dict[entry[1][0]] = temp
                s.add_soft(functools.reduce(And, depandancy, RV_dict[entry[1][0]] == eval(entry[1][1])), entry[2]*conditional_prob)
                # if entry[1][1] == "1":
                #     s.add_soft(functools.reduce(And, depandancy, RV_dict[entry[1][0]] == 1), entry[2]*conditional_prob)
                # if entry[1][1] == "0":
                #     s.add_soft(functools.reduce(And, depandancy, RV_dict[entry[1][0]] == 0), entry[2]*conditional_prob)

unobserved_RV_name_list = list(RV_dict.keys())
observed_RV_name_list = []
for O in Os:
    observed_RV_name_list.append(O[0])
    s.add(RV_dict[O[0]] == eval(O[1]))

unobserved_RV_name_list = [e for e in unobserved_RV_name_list if e not in observed_RV_name_list]

objective = 1
for RV_name, RV in RV_dict.items():
    objective = objective*RV

s.maximize(objective)
print(s.check())
print(s.model())

