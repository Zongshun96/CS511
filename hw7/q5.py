from z3 import *
opt = Optimize()

variable_d = {}
neg_var_d = {}

input = [
            [ [1,[[0,1]]], [1,[[0,2]]] ] ,
            [ [1,[[0,1],[1,2]]], [2,[[0,2]]], [-3,[[0,1]]], [-1,[]] ] ,
            [ [-1,[[0,1],[1,2]]], [-2,[[0,2]]], [3,[[0,1]]], [1,[]] ]
        ]

# input = [
#             [ [1, [[0,1]]] ] ,
#             [ [1, [[0,1]]] ] ,
#             [ [-1,[[0,1]]] ]
#         ]

for i in range(len(input)):
    # init vars
    if i == 0:
        for term in input[i]:
            # for c, l in term:
            for var in term[1]:
                # if var[0] == 0:
                variable_d[var[1]] = Int("x"+str(var[1]))
                #     opt.add(Or(variable_d[var[1]] == 0, variable_d[var[1]] == 1))
                # if var[0] == 1:
                neg_var_d[var[1]] = Int("x_"+str(var[1]))
                opt.add(Or(variable_d[var[1]] == 0, variable_d[var[1]] == 1))
                opt.add(Or(neg_var_d[var[1]] == 0, neg_var_d[var[1]] == 1))
                opt.add(Not(neg_var_d[var[1]] == variable_d[var[1]]))
    # init minimization
    if i == 0:
        to_minimize = 0
        for term in input[i]:
            term_to_minimize = 1
            # for c, l in term:
            for var in term[1]:
                if var[0] == 0:
                    # variable_d[var[1]] = Int)("x"+str(var[1]))
                    term_to_minimize = term_to_minimize * variable_d[var[1]]
                if var[0] == 1:
                    # neg_var_d[var[1]] = Int)("x"+str(var[1]))
                    to_minimize = term_to_minimize * neg_var_d[var[1]]
            term_to_minimize = term[0] * term_to_minimize
            to_minimize = to_minimize + term_to_minimize
        opt.minimize(to_minimize)
    else:
        new_constraint = 0
        for term in input[i]:
            term_new_constraint = 1
            # for c, l in term:
            for var in term[1]:
                if var[0] == 0:
                    # variable_d[var[1]] = Int)("x"+str(var[1]))
                    term_new_constraint = term_new_constraint * variable_d[var[1]]
                if var[0] == 1:
                    # neg_var_d[var[1]] = Int)("x"+str(var[1]))
                    term_new_constraint = term_new_constraint * neg_var_d[var[1]]
            term_new_constraint = term[0] * term_new_constraint
            new_constraint = new_constraint + term_new_constraint
        opt.add(new_constraint <= 0)
            
print(opt.check())
# print(opt.upper(h))
print(opt.model())





# def max(F, X, M):
#     s = Solver()
#     s.add(F)
#     last_model  = None
#     i = 0
#     while True:
#         r = s.check()
#         if r == unsat:
#             if last_model != None:
#                 return last_model
#             else:
#                 return unsat
#         if r == unknown:
#             raise Z3Exception("failed")
#         last_model = s.model()
#         s.add(X > last_model[X])
#         i = i + 1
#         if (i > M):
#             raise Z3Exception("maximum not found, maximum number of iterations was reached")




# s = SolverFor("QF_LIA")
# # (set-logic QF_LIA)
# s.set("model.completion", True)
# # (set-option :produce-models true)
# # s = Solver()

# out_a0, in_a0, out_a1, out_a2, out_b0, in_b0 = Ints('out_a0 in_a0 out_a1 out_a2 out_b0 in_b0')

# phi_0 = in_a0==in_b0
# phi_a = And(And((out_a0==in_a0), out_a1==out_a0 * in_a0), out_a2==out_a1*in_a0)
# phi_b = out_b0 == (in_b0*in_b0)*in_b0
# phi_1 = out_a2 == out_b0

# s.add(Not(Implies(And(And(phi_0, phi_a), phi_b), phi_1)))

# print(s.check())
