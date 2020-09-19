(declare-const x Bool)
(declare-const y Bool)
(declare-const z Bool)

;; (x \land y) \lor (x \land z) \lor (y \land z)
(declare-fun phi (Bool Bool Bool) Bool)
(assert (= (phi x y z)
           (or (and x y) (or (and x z) (and y z)))))

;; (x \lor y) \land (x \lor z) \land (y \lor z)
(declare-fun psi (Bool Bool Bool) Bool)
(assert (= (psi x y z)
           (and (or x y) (and (or x z) (or y z)))))

;; constraint: check sat for not equal
(assert (not (= (phi x y z) (psi x y z))))

(check-sat)
