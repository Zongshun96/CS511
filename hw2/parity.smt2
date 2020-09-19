;;;;   execute at the linux prompt by issuing the command:
;;;;   > z3 parity.smt2

(declare-const p1 Bool)
(declare-const p2 Bool)
(declare-const p3 Bool)
(declare-const p4 Bool)

(declare-fun phi (Bool Bool Bool Bool) Bool)
(assert (= (phi p1 p2 p3 p4)
           (and (or (not p1) p2 p3 p4) (or p1 (not p2) p3 p4) (or p1 p2 (not p3) p4) (or p1 p2 p3 (not p4))
            (or (not p1) (not p2) (not p3) p4) (or (not p1) (not p2) p3 (not p4)) (or (not p1) p2 (not p3) (not p4)) (or p1 (not p2) (not p3) (not p4)))))

(declare-fun psi (Bool Bool Bool Bool) Bool)
(assert (= (psi p1 p2 p3 p4)
           (or (and p1 p2 p3 p4) (and (not p1) (not p2) (not p3) (not p4)) (and p1 p2 (not p3) (not p4)) (and (not p1) (not p2) p3 p4)
            (and (not p1) p2 (not p3) p4) (and (not p1) p2 p3 (not p4)) (and p1 (not p2) (not p3) p4) (and p1 (not p2) p3 (not p4)))))

(declare-fun theta (Bool Bool Bool Bool) Bool)
(assert (= (theta p1 p2 p3 p4)
           (= p1 (= p2 (= p3 p4)))))
           ;;(= p1 p2 p3 p4)))


;; constraint: check sat for not equal
(assert (not (= (phi p1 p2 p3 p4) (psi p1 p2 p3 p4))))
(assert (not (= (phi p1 p2 p3 p4) (theta p1 p2 p3 p4))))
(assert (not (= (psi p1 p2 p3 p4) (theta p1 p2 p3 p4))))
(check-sat)
