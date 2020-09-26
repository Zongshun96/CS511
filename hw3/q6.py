from z3 import *

s = Solver()

# CostFunc = Function('CostFunc', IntSort(), IntSort(), IntSort())
# x = Int('x')
# y = Int('y')
# s.add(x==1)
# s.add(y==1)
# s.add(CostFunc(x,y)==x*2+y*4)
# s.add(CostFunc(y,x)==y*4+x*2)
# # s.add(CostFunc(x,y)>=100)
# print(s.check())
# n = 1
# results = []
# while s.check() == sat and n <= 20 :
#     m = s.model()
#     results.append (m)
#     s.add ( x != m[x] )
#     n = n+1
#
# # print models
# for p in range (len (results)) :
#     print("================================== model", p, "==================================")
#     print(results[p])






# readin = "(1, 2, [ 2, 3, 4, 5 ])\n(2, 4, [ 1, 4 ])\n(3, 4, [ 1, 5 ])\n(4, 7, [ 1, 2, 5 ])\n(5, 7, [ 1, 3, 4 ])"
# readin = "(1, 2, [ 2 ])\n(2, 4, [ 1 ])"
readin = "(1, 2, [ 2, 3 ])\n(2, 4, [ 1 ])\n(3, 4, [ 1 ])"

lineList = readin.split("\n")
for i in range(len(lineList)):
    lineList[i] = eval(lineList[i])

print(len(lineList))

# for name,_,_ in lineList:
#     print(name)
#     print(chr(name+64))

ParamList = [[i, Int(chr(i+64)),w, adjlist] for i,w,adjlist in lineList]
for i1, p1, w1, adjlist in ParamList:
    s.add(p1 == 1)

CostFunc = Function('CostFunc', IntSort(), IntSort(), IntSort())
for i1, p1, w1, adjlist in ParamList:
    for i2 in adjlist:
        print(p1, ParamList[i2-1][1], p1 * w1 + ParamList[i2-1][1] * ParamList[i2-1][2])
        s.add(CostFunc(p1, ParamList[i2-1][1]) == p1 * w1 + ParamList[i2-1][1] * ParamList[i2-1][2])
    # for i in range(len(lineList[i1][2])):
        # s.add(CostFunc(p1[0], ParamList[lineList[i1-1][2][i]-1][1][0]) == p1[0]*w1+ParamList[lineList[i1-1][2][i]-1][1][0]*ParamList[lineList[i1-1][2][i]-1][2])



print(s.check())

n = 1
results = []
while s.check() == sat and n <= 20 :
    m = s.model()
    results.append (m)
    s.add ( ParamList[0][1] != m[ParamList[0][1]] )
    n = n+1

# print models
for p in range (len (results)) :
    print("================================== model", p, "==================================")
    print(results[p])