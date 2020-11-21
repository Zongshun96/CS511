import functools
from z3 import *

def MAP(CPTs, Os, Vs):
    s = Optimize()

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

    step = 0
    while not len(CPTs) == len(RV_dict):  # make sure all RV are parsed
        for V,T in CPTs:
            for entry in T:
                if not entry[0] == []:
                    depandancy = []
                    conditional_prob = 1
                    for dependants in entry[0]:
                        if not dependants[0] in RV_dict:    # in case some conditional RV hasn't been parsed
                            break
                        if dependants[1] == "1":
                            depandancy.append(RV_dict[dependants[0]] == 1)
                            conditional_prob = conditional_prob*RV_prob_dict[dependants[0]]
                        if dependants[1] == "0":
                            depandancy.append(RV_dict[dependants[0]] == 0)
                            conditional_prob = conditional_prob*RV_prob_dict[dependants[0]]
                    if entry[1][0] not in RV_dict:
                        temp = Int(entry[1][0])
                        RV_dict[entry[1][0]] = temp
                    s.add_soft(functools.reduce(And, depandancy, RV_dict[entry[1][0]] == eval(entry[1][1])), entry[2]*conditional_prob)
        
        step = step + 1
        if step > 10000:
            raise ValueError('A very specific bad thing happened.')
            return

    # unobserved_RV_name_list = list(RV_dict.keys())
    observed_RV_name_list = []
    try:
        for O in Os:
            observed_RV_name_list.append(O[0])
            s.add(RV_dict[O[0]] == eval(O[1]))
    except Exception as e:
        pass
        # print(e)

    # unobserved_RV_name_list = [e for e in unobserved_RV_name_list if e not in observed_RV_name_list]

    objective = 1
    for RV_name in Vs:
        objective = objective*RV_dict[RV_name]

    s.maximize(objective)
    print(s.check())
    print(s.model())

if __name__ == "__main__":
    # CPTs = [["x", [[[],["x","1"],0.3], [[],["x","0"],0.7]]], 
    #         ["y", [[[["x", "1"]],["y","1"],0.2], [[["x", "0"]],["y","0"],0.2], [[["x", "1"]],["y","0"],0.8], [[["x", "0"]],["y","1"],0.8]]]]
    # Os = [["x", "1"]]
    # Vs = ["x"]

    CPTs = [
        ["V1", [[[], ["V1", "1"], 0.3], [[], ["V1", "0"], 0.7]]],
        ["V2", [[[], ["V2", "1"], 0.2], [[], ["V2", "0"], 0.8]]],
        ["V3", [[[], ["V3", "1"], 0.9], [[], ["V3", "0"], 0.1]]],
        ["V4", [[[["V1", "1"], ["V2", "1"]], ["V4", "1"], 0.2],
            [[["V1", "1"], ["V2", "1"]], ["V4", "0"], 0.8],
            [[["V1", "1"], ["V2", "0"]], ["V4", "1"], 0.9],
            [[["V1", "1"], ["V2", "0"]], ["V4", "0"], 0.1],
            [[["V1", "0"], ["V2", "1"]], ["V4", "1"], 0.1],
            [[["V1", "0"], ["V2", "1"]], ["V4", "0"], 0.9],
            [[["V1", "0"], ["V2", "0"]], ["V4", "1"], 0.4],
            [[["V1", "0"], ["V2", "0"]], ["V4", "0"], 0.4]]],
        ["V5", [[[["V2", "1"], ["V2", "1"]], ["V5", "1"], 0.5],
            [[["V2", "1"], ["V3", "1"]], ["V5", "0"], 0.5],
            [[["V2", "1"], ["V3", "0"]], ["V5", "1"], 0.6],
            [[["V2", "1"], ["V3", "0"]], ["V5", "0"], 0.4],
            [[["V2", "0"], ["V3", "1"]], ["V5", "1"], 0.3],
            [[["V2", "0"], ["V3", "1"]], ["V5", "0"], 0.7],
            [[["V2", "0"], ["V3", "0"]], ["V5", "1"], 0.1],
            [[["V2", "0"], ["V3", "0"]], ["V5", "0"], 0.9]]],
        ["V6", [[[["V5", "0"]], ["V6", "0"], 0.1],
            [[["V5", "0"]], ["V6", "1"], 0.9],
            [[["V5", "0"]], ["V6", "0"], 0.5],
            [[["V5", "0"]], ["V6", "1"], 0.5]]],
        ["V7", [[[["V4", "0"]], ["V7", "0"], 0.7],
            [[["V4", "0"]], ["V7", "1"], 0.3],
            [[["V4", "0"]], ["V7", "0"], 0.4],
            [[["V4", "0"]], ["V7", "1"], 0.6]]],     
        ["V8", [[[["V4", "1"], ["V5", "1"]], ["V8", "1"], 0.4],
            [[["V4", "1"], ["V5", "1"]], ["V8", "0"], 0.6],
            [[["V4", "1"], ["V5", "0"]], ["V8", "1"], 0.5],
            [[["V4", "1"], ["V5", "0"]], ["V8", "0"], 0.5],
            [[["V4", "0"], ["V5", "1"]], ["V8", "1"], 0.6],
            [[["V4", "0"], ["V5", "1"]], ["V8", "0"], 0.4],
            [[["V4", "0"], ["V5", "0"]], ["V8", "1"], 0.7],
            [[["V4", "0"], ["V5", "0"]], ["V8", "0"], 0.3]]]

    ]
    Os = [["V1", "1"]]
    Vs = ["V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8"]



    MAP(CPTs, Os, Vs)