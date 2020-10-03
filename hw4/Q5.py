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
all x (Animal(x) -> (all y (Plant(y) -> Eats(x,y)))
                    |
                    (all z ( Animal(z) &
                             Smaller(z,x) &
                             (exists u (Plant(u) & Eats(z,u)))
                            ->
                             Eats(x,z)))).
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

A = DeclareSort("A")
Wolf = Function('Wolf', A, BoolSort())
Fox = Function('Fox', A, BoolSort())
Bird = Function('Bird', A, BoolSort())
Caterpillar = Function('Caterpillar', A, BoolSort())
Snail = Function('Snail', A, BoolSort())
Grain = Function('Grain', A, BoolSort())

Animal = Function('Animal', A, BoolSort())
Plant = Function('Plant', A, BoolSort())


B = DeclareSort("B")
Eats = Function('Eats', A, B, BoolSort())
Smaller = Function('Smaller', A, B, BoolSort())


ForAll(A, Implies(Wolf(A), Animal(A)))
ForAll(A, Implies(Fox(A), Animal(A)))
ForAll(A, Implies(Bird(A), Animal(A)))
ForAll(A, Implies(Caterpillar(A), Animal(A)))
ForAll(A, Implies(Snail(A), Animal(A)))
ForAll(A, Implies(Grain(A), Animal(A)))
Exists(A, Wolf(A))
Exists(A, Fox(A))
Exists(A, Bird(A))
Exists(A, Caterpillar(A))
Exists(A, Snail(A))
Exists(A, Grain(A))

C = DeclareSort("C")
ForAll(A, Implies(Animal(A), Or(ForAll(B, Implies(Plant(B), Eats(A,B))), ForAll()  )))