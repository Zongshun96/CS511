from z3 import *
s = Optimize()


CPTs = [["x", [[],["x","True"],0.7]], ["x", [[],["x","False"],0.3]], ["y",[[["x", "True"]],["y","True"],0.1]], ["y",[[["x", "False"]],["y","False"],0.9]], ["y",[[["x", "True"]],["y","False"],0.8]], ["y",[[["x", "False"]],["y","True"],0.2]]]
Os = [["x", "False"]]


RV_dict = {}

for CPT in CPTs:
    if CPT[1][0] == []:
        if CPT[0] not in RV_dict:
            temp = Int(CPT[0])
            RV_dict[CPT[0]] = temp
        if CPT[1][1][1] == "True":
            s.add_soft(RV_dict[CPT[0]] == 1, CPT[1][2])
        if CPT[1][1][1] == "False":
            s.add_soft(RV_dict[CPT[0]] == 0, CPT[1][2])
    else:
        for dependants in CPT[1][0]:
            # s.add_soft(RV_dict[dependants[0]] == eval(dependants[1]))
            if dependants[1] == "True":
                s.add_soft(RV_dict[dependants[0]] == 1, CPT[1][2])
            if dependants[1] == "False":
                s.add_soft(RV_dict[dependants[0]] == 0, CPT[1][2])
        if CPT[0] not in RV_dict:
            temp = Int(CPT[0])
            RV_dict[CPT[0]] = temp
        if CPT[1][1][1] == "True":
            s.add_soft(RV_dict[CPT[0]] == 1, CPT[1][2])
        if CPT[1][1][1] == "False":
            s.add_soft(RV_dict[CPT[0]] == 0, CPT[1][2])


unobserved_RV_name_list = list(RV_dict.keys())
observed_RV_name_list = []
for O in Os:
    observed_RV_name_list.append(O[0])
    s.add(RV_dict[O[0]] == eval(O[1]))

unobserved_RV_name_list = [e for e in unobserved_RV_name_list if e not in observed_RV_name_list]

objective = 1
for RV_name, RV in RV_dict.items():
    objective = objective*RV

h = s.maximize(objective)
print(s.check())
print(s.model())
print(h.value())


# x, y, z = Ints('x y z')

# s = Optimize()
# s.add(x > y)
# s.add(y > z)
# s.add(z > 0)
# s.add_soft(x > y +1)
# h = s.minimize(x)
# print(s.check())
# print(s.model())
# print(h.value())

# s = Optimize()
# s.add(x > y)
# s.add(y > z)
# s.add(z > 0)
# h = s.minimize(x)
# s.add_soft(x > y +1)
# print(s.check())
# print(s.model())
# print(h.value())

