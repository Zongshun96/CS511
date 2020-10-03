# formulas(assumptions).
#
# all x (Wolf(x) -> Animal(x)).
# all x (Fox(x) -> Animal(x)).
# all x (Bird(x) -> Animal(x)).
# all x (Caterpillar(x) -> Animal(x)).
# all x (Snail(x) -> Animal(x)).
# all x (Grain(x) -> Plant(x)).
#
# exists x Wolf(x).
# exists x Fox(x).
# exists x Bird(x).
# exists x Caterpillar(x).
# exists x Snail(x).
# exists x Grain(x).
#
# % All animals either eat all plants or eat all smaller animals
# % that eat some plants.
#
# all x (Animal(x) -> (all y (Plant(y) -> Eats(x,y)))
#                     |
#                     (all z ( Animal(z) &
#                              Smaller(z,x) &
#                              (exists u (Plant(u) & Eats(z,u)))
#                             ->
#                              Eats(x,z)))).
#
# all x all y (Caterpillar(x) & Bird(y) -> Smaller(x,y)).
# all x all y (Snail(x) & Bird(y) -> Smaller(x,y)).
# all x all y (Bird(x) & Fox(y) -> Smaller(x,y)).
# all x all y (Fox(x) & Wolf(y) -> Smaller(x,y)).
# all x all y (Bird(x) & Caterpillar(y) -> Eats(x,y)).
#
# all x (Caterpillar(x) -> (exists y (Plant(y) & Eats(x,y)))).
# all x (Snail(x)       -> (exists y (Plant(y) & Eats(x,y)))).
#
# all x all y (Wolf(x) & Fox(y) -> -Eats(x,y)).
# all x all y (Wolf(x) & Grain(y) -> -Eats(x,y)).
# all x all y (Bird(x) & Snail(y) -> -Eats(x,y)).
#
# end_of_list.
#
# formulas(goals).
#
# % There is an animal that eats {an animal that eats all grains}.
#
# exists x exists y ( Animal(x) &
# 	            Animal(y) &
# 	            Eats(x,y) &
#                     (all z (Grain(z) -> Eats(y,z)))).


from z3 import *

Type = DeclareSort("Type")
# B = DeclareSort("B")
# C = DeclareSort("C")
# D = DeclareSort("D")
A, B, C, D  = Consts('A B C D', Type)

Wolf = Function('Wolf', Type, BoolSort())
Fox = Function('Fox', Type, BoolSort())
Bird = Function('Bird', Type, BoolSort())
Caterpillar = Function('Caterpillar', Type, BoolSort())
Snail = Function('Snail', Type, BoolSort())
Grain = Function('Grain', Type, BoolSort())

Animal = Function('Animal', Type, BoolSort())
Plant = Function('Plant', Type, BoolSort())



Eats = Function('Eats', Type, Type, BoolSort())
Smaller = Function('Smaller', Type, Type, BoolSort())

axioms = [
ForAll(A, Implies(Wolf(A), Animal(A))),
ForAll(A, Implies(Fox(A), Animal(A))),
ForAll(A, Implies(Bird(A), Animal(A))),
ForAll(A, Implies(Caterpillar(A), Animal(A))),
ForAll(A, Implies(Snail(A), Animal(A))),
ForAll(A, Implies(Grain(A), Animal(A))),
Exists(A, Wolf(A)),
Exists(A, Fox(A)),
Exists(A, Bird(A)),
Exists(A, Caterpillar(A)),
Exists(A, Snail(A)),
Exists(A, Grain(A)),


ForAll(A, Implies(Animal(A), Or(ForAll(B, Implies(Plant(B), Eats(A,B))), ForAll(C, And(Animal(C), And(Smaller(C,A), Implies(Exists(D, And(Plant(D),Eats(C,D))), Eats(A,C)))))))),
ForAll([A,B], Implies(And(Caterpillar(A), Bird(B)), Smaller(A,B))),
ForAll([A,B], Implies(And(Snail(A), Bird(B)), Smaller(A,B))),
ForAll([A,B], Implies(And(Bird(A), Fox(B)), Smaller(A,B))),
ForAll([A,B], Implies(And(Fox(A), Wolf(B)), Smaller(A,B))),
ForAll([A,B], Implies(And(Bird(A), Caterpillar(B)), Eats(A,B))),

ForAll(A, Implies(Caterpillar(A), Exists(B, And(Plant(B), Eats(A,B))))),
ForAll(A, Implies(Snail(A), Exists(B, And(Plant(B), Eats(A,B))))),

ForAll([A,B], Implies(And(Wolf(A), Fox(B)), Eats(A,B))),
ForAll([A,B], Implies(And(Wolf(A), Grain(B)), Eats(A,B))),
ForAll([A,B], Implies(And(Bird(A), Snail(B)), Eats(A,B)))
]

s = Solver()
s.add(axioms)
print (s)
print (s.check())
print ("Interpretation for Type:")
print (s.model()[Type])
print ("Model:")
print (s.model())