import functools
from z3 import *




(m,n) = (6,10) # grid dimensions
PierP = [(1,1),(2,7),(3,3),(3,8),(6,8)] # pier positions
BlockedP = [(2,3),(2,5),(2,8),(4,4),(4,5),(4,9),(5,5),(6,1)] # blocked positions

s = Optimize()

map = []
for i in range(m):
    map.append(Bools(['x'+str(i) for i in range(n)]))

for pp in PierP:
    s.add(map[pp[0]-1][pp[1]-1])    # C1
    # C3
    if pp[0]-1-1 < 0: # touch upper bound
        if pp[1]-1-1 < 0:   # touch left bound
            s.add(Or(map[pp[0]-1][pp[1]-1+1],map[pp[0]-1+1][pp[1]-1]))
            s.add(And(Implies(map[pp[0]-1][pp[1]-1+1], Not(map[pp[0]-1+1][pp[1]-1])), Implies(map[pp[0]-1+1][pp[1]-1], Not(map[pp[0]-1][pp[1]-1+1]))))
        elif pp[1]-1+1 >= n:   # touch right bound
            s.add(Or(map[pp[0]-1][pp[1]-1-1],map[pp[0]-1+1][pp[1]-1]))
            s.add(And(Implies(map[pp[0]-1][pp[1]-1-1], Not(map[pp[0]-1+1][pp[1]-1])), Implies(map[pp[0]-1+1][pp[1]-1], Not(map[pp[0]-1][pp[1]-1-1]))))
        else:
            s.add(Or(map[pp[0]-1][pp[1]-1+1],map[pp[0]-1][pp[1]-1-1],map[pp[0]-1+1][pp[1]-1]))
            s.add(And(Implies(map[pp[0]-1][pp[1]-1+1], And(Not(map[pp[0]-1][pp[1]-1-1]), Not(map[pp[0]-1+1][pp[1]-1]))), Implies(map[pp[0]-1][pp[1]-1-1], And(Not(map[pp[0]-1][pp[1]-1+1]), Not(map[pp[0]-1+1][pp[1]-1]))), Implies(map[pp[0]-1+1][pp[1]-1], And(Not(map[pp[0]-1][pp[1]-1+1]), Not(map[pp[0]-1][pp[1]-1-1])))))
    elif pp[0]-1+1 >= m:    # touch lower bound
        if pp[1]-1-1 < 0:   # touch left bound
            s.add(Or(map[pp[0]-1][pp[1]-1+1],map[pp[0]-1-1][pp[1]-1]))
            s.add(And(Implies(map[pp[0]-1][pp[1]-1+1], Not(map[pp[0]-1-1][pp[1]-1])), Implies(map[pp[0]-1-1][pp[1]-1], Not(map[pp[0]-1][pp[1]-1+1]))))
        elif pp[1]-1+1 >= n:   # touch left bound
            s.add(Or(map[pp[0]-1][pp[1]-1-1],map[pp[0]-1-1][pp[1]-1]))
            s.add(And(Implies(map[pp[0]-1][pp[1]-1-1], Not(map[pp[0]-1-1][pp[1]-1])), Implies(map[pp[0]-1-1][pp[1]-1], Not(map[pp[0]-1][pp[1]-1-1]))))
        else:
            s.add(Or(map[pp[0]-1][pp[1]-1+1],map[pp[0]-1][pp[1]-1-1],map[pp[0]-1-1][pp[1]-1]))
            s.add(And(Implies(map[pp[0]-1][pp[1]-1+1], And(Not(map[pp[0]-1][pp[1]-1-1]), Not(map[pp[0]-1-1][pp[1]-1]))), Implies(map[pp[0]-1][pp[1]-1-1], And(Not(map[pp[0]-1][pp[1]-1+1]), Not(map[pp[0]-1-1][pp[1]-1]))), Implies(map[pp[0]-1-1][pp[1]-1], And(Not(map[pp[0]-1][pp[1]-1+1]), Not(map[pp[0]-1][pp[1]-1-1])))))
    
    
    elif pp[1]-1-1 < 0: # touch left bound
        if pp[0]-1-1 < 0:   # touch upper bound
            s.add(Or(map[pp[0]-1][pp[1]-1+1], map[pp[0]-1+1][pp[1]-1]))
            s.add(And(Implies(map[pp[0]-1][pp[1]-1+1], Not(map[pp[0]-1+1][pp[1]-1])), Implies(map[pp[0]-1+1][pp[1]-1], Not(map[pp[0]-1][pp[1]-1+1]))))
        elif pp[0]-1+1 >= n:   # touch lower bound
            s.add(Or(map[pp[0]-1][pp[1]-1+1], map[pp[0]-1-1][pp[1]-1]))
            s.add(And(Implies(map[pp[0]-1][pp[1]-1+1], Not(map[pp[0]-1-1][pp[1]-1])),
                    Implies(map[pp[0]-1-1][pp[1]-1], Not(map[pp[0]-1][pp[1]-1+1]))))
        else:
            s.add(Or(map[pp[0]-1][pp[1]-1+1], map[pp[0]-1-1][pp[1]-1], map[pp[0]-1+1][pp[1]-1]))
            s.add(And(Implies(map[pp[0]-1][pp[1]-1+1], And(Not(map[pp[0]-1-1][pp[1]-1]), Not(map[pp[0]-1+1][pp[1]-1]))),
                    Implies(map[pp[0]-1-1][pp[1]-1], And(Not(map[pp[0]-1][pp[1]-1+1]), Not(map[pp[0]-1+1][pp[1]-1]))),
                    Implies(map[pp[0]-1+1][pp[1]-1], And(Not(map[pp[0]-1][pp[1]-1+1]), Not(map[pp[0]-1-1][pp[1]-1])))))
    elif pp[1]-1+1 >= m:    # touch right bound
        if pp[0]-1-1 < 0:   # touch upper bound
            s.add(Or(map[pp[0]-1][pp[1]-1-1], map[pp[0]-1+1][pp[1]-1]))
            s.add(And(Implies(map[pp[0]-1][pp[1]-1-1], Not(map[pp[0]-1+1][pp[1]-1])),
                Implies(map[pp[0]-1+1][pp[1]-1], Not(map[pp[0]-1][pp[1]-1-1]))))
        elif pp[0]-1+1 >= n:   # touch lower bound
            s.add(Or(map[pp[0]-1][pp[1]-1-1], map[pp[0]-1-1][pp[1]-1]))
            s.add(And(Implies(map[pp[0]-1][pp[1]-1-1], Not(map[pp[0]-1-1][pp[1]-1])),
                Implies(map[pp[0]-1-1][pp[1]-1], Not(map[pp[0]-1][pp[1]-1-1]))))
        else:
            s.add(Or(map[pp[0]-1][pp[1]-1-1], map[pp[0]-1-1][pp[1]-1], map[pp[0]-1+1][pp[1]-1]))
            s.add(And(Implies(map[pp[0]-1][pp[1]-1-1], And(Not(map[pp[0]-1-1][pp[1]-1]), Not(map[pp[0]-1+1][pp[1]-1]))),
                Implies(map[pp[0]-1-1][pp[1]-1], And(Not(map[pp[0]-1][pp[1]-1-1]), Not(map[pp[0]-1+1][pp[1]-1]))),
                Implies(map[pp[0]-1+1][pp[1]-1], And(Not(map[pp[0]-1][pp[1]-1-1]), Not(map[pp[0]-1-1][pp[1]-1])))))
    else:
        s.add(Or(map[pp[0]-1][pp[1]-1+1], map[pp[0]-1][pp[1]-1-1], map[pp[0]-1-1][pp[1]-1], map[pp[0]-1+1][pp[1]-1]))
        s.add(And(Implies(map[pp[0]-1][pp[1]-1+1], And(Not(map[pp[0]-1][pp[1]-1-1]), Not(map[pp[0]-1-1][pp[1]-1]), Not(map[pp[0]-1+1][pp[1]-1]))),
                Implies(map[pp[0]-1][pp[1]-1-1], And(Not(map[pp[0]-1][pp[1]-1+1]), Not(map[pp[0]-1-1][pp[1]-1]), Not(map[pp[0]-1+1][pp[1]-1]))),
                Implies(map[pp[0]-1-1][pp[1]-1], And(Not(map[pp[0]-1][pp[1]-1+1]), Not(map[pp[0]-1][pp[1]-1-1]), Not(map[pp[0]-1+1][pp[1]-1]))),
                Implies(map[pp[0]-1+1][pp[1]-1], And(Not(map[pp[0]-1][pp[1]-1+1]), Not(map[pp[0]-1][pp[1]-1-1]), Not(map[pp[0]-1-1][pp[1]-1])))))

for i in range(m): # C4
    for j in range(n):
        if (i,j) not in PierP and (i,j) not in BlockedP:
            if i-1 < 0: # touch upper bound
                if j-1 < 0:   # touch left bound
                    s.add(Or(
                        Implies(map[i][j], And(map[i+1][j], map[i][j+1])),
                        Implies(map[i][j], And(map[i][j+1], map[i+1][j]))))
                elif j+1 >= n:   # touch right bound
                    s.add(Or(
                        Implies(map[i][j], And(map[i+1][j], map[i][j-1])), 
                        Implies(map[i][j], And(map[i][j-1], map[i+1][j]))))
                else:
                    s.add(Or(
                        Implies(map[i][j], And(map[i+1][j], map[i][j+1])), Implies(map[i][j], And(map[i+1][j], map[i][j-1])),
                        Implies(map[i][j], And(map[i][j+1], map[i+1][j])), Implies(map[i][j], And(map[i][j+1], map[i][j-1])),
                        Implies(map[i][j], And(map[i][j-1], map[i+1][j])), Implies(map[i][j], And(map[i][j-1], map[i][j+1]))))
             
            elif i+1 >= m:    # touch lower bound
                if j-1 < 0:   # touch left bound
                    s.add(Or(
                        Implies(map[i][j], And(map[i-1][j], map[i][j+1])),
                        Implies(map[i][j], And(map[i][j+1], map[i-1][j]))))
                elif j+1 >= n:   # touch left bound
                    s.add(Or(
                        Implies(map[i][j], And(map[i-1][j], map[i][j-1])),
                        Implies(map[i][j], And(map[i][j-1], map[i-1][j]))))
                else:
                    s.add(Or(
                        Implies(map[i][j], And(map[i-1][j], map[i][j+1])), Implies(map[i][j], And(map[i-1][j], map[i][j-1])),
                        Implies(map[i][j], And(map[i][j+1], map[i][j-1])), Implies(map[i][j], And(map[i][j+1], map[i-1][j])),
                        Implies(map[i][j], And(map[i][j-1], map[i][j+1])), Implies(map[i][j], And(map[i][j-1], map[i-1][j]))))


            elif j-1 < 0: # touch left bound
                if i-1 < 0:   # touch upper bound
                    s.add(Or(
                        Implies(map[i][j], And(map[i+1][j], map[i][j+1])),
                        Implies(map[i][j], And(map[i][j+1], map[i+1][j]))))
                elif i+1 >= m:   # touch lower bound
                    s.add(Or(
                        Implies(map[i][j], And(map[i-1][j], map[i][j+1])),
                        Implies(map[i][j], And(map[i][j+1], map[i-1][j]))))
                else:
                    s.add(Or(
                        Implies(map[i][j], And(map[i+1][j], map[i][j+1])), Implies(map[i][j], And(map[i+1][j], map[i-1][j])),        
                        Implies(map[i][j], And(map[i-1][j], map[i][j+1])), Implies(map[i][j], And(map[i-1][j], map[i+1][j])),
                        Implies(map[i][j], And(map[i][j+1], map[i+1][j])), Implies(map[i][j], And(map[i][j+1], map[i-1][j]))))
             
            elif j+1 >= n:    # touch right bound
                if i-1 < 0:   # touch upper bound
                    s.add(Or(
                        Implies(map[i][j], And(map[i+1][j], map[i][j-1])), 
                        Implies(map[i][j], And(map[i][j-1], map[i+1][j]))))
                elif i+1 >= m:   # touch lower bound
                    s.add(Or(
                        Implies(map[i][j], And(map[i-1][j], map[i][j-1])),
                        Implies(map[i][j], And(map[i][j-1], map[i-1][j]))))
                else:
                    s.add(Or(
                        Implies(map[i][j], And(map[i+1][j], map[i][j-1])), Implies(map[i][j], And(map[i+1][j], map[i-1][j])),        
                        Implies(map[i][j], And(map[i-1][j], map[i][j-1])), Implies(map[i][j], And(map[i-1][j], map[i+1][j])),
                        Implies(map[i][j], And(map[i][j-1], map[i+1][j])), Implies(map[i][j], And(map[i][j-1], map[i-1][j]))))
                
            else:
                s.add(Or(
                        Implies(map[i][j], And(map[i+1][j], map[i][j+1])), Implies(map[i][j], And(map[i+1][j], map[i][j-1])), Implies(map[i][j], And(map[i+1][j], map[i-1][j])),        
                        Implies(map[i][j], And(map[i-1][j], map[i][j+1])), Implies(map[i][j], And(map[i-1][j], map[i][j-1])), Implies(map[i][j], And(map[i-1][j], map[i+1][j])),
                        Implies(map[i][j], And(map[i][j+1], map[i+1][j])), Implies(map[i][j], And(map[i][j+1], map[i][j-1])), Implies(map[i][j], And(map[i][j+1], map[i-1][j])),
                        Implies(map[i][j], And(map[i][j-1], map[i+1][j])), Implies(map[i][j], And(map[i][j-1], map[i][j+1])), Implies(map[i][j], And(map[i][j-1], map[i-1][j]))))
                
    
for bp in BlockedP: # C2
    s.add(Not(map[bp[0]-1][bp[1]-1]))


for i in range(m): # C5
    for j in range(n):
        if (i,j) not in PierP and (i,j) not in BlockedP:
            s.add_soft(Not(map[i][j]), weight = 0.2)



map_ = []
for i in range(m):
    map_.append(Ints(['x_'+str(i) for i in range(n)]))
for i in range(m):
    for j in range(n):
        s.add(Or(And(map[i][j], map_[i][j] == 1), And(Not(map[i][j]), map_[i][j] == 0)))

    
objective = Int("dummy")
s.add(objective == 0)
# lst = []
for i in range(m): # C4
    for j in range(n):
        # s.add(Or(map[i][j] == 0, map[i][j] == 1))
        objective = objective+map_[i][j]
        # lst.append(map_[i][j])
# objective = functools.reduce()
s.maximize(objective)
print(s.check())
print(s.model())


