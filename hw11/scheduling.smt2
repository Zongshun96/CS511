;; 2020-09-16 Z3 script by Assaf Kfoury

(set-logic QF_LIA)
(set-option :produce-models true)

(declare-fun A () Int)
(assert (>= A 0))
(declare-fun At () Int)
(assert (= At 2))
(declare-fun B () Int)
(assert (>= B 0))
(declare-fun Bt () Int)
(assert (= Bt 1))
(declare-fun C () Int)
(assert (>= C 0))
(declare-fun Ct () Int)
(assert (= Ct 2))
(declare-fun D () Int)
(assert (>= D 0))

(declare-fun Dt () Int)
(assert (= Dt 2))
(declare-fun E () Int)
(assert (>= E 0))
(declare-fun Et () Int)
(assert (= Et 7))
(declare-fun F () Int)
(assert (>= F 0))
(declare-fun Ft () Int)
(assert (= Ft 5))

(declare-fun End () Int)
(assert (= End 14))

(assert (or (<= (+ A At) C) (<= (+ C Ct) A)))
(assert (or (<= (+ B Bt) D) (<= (+ D Dt) B)))
(assert (or (<= (+ B Bt) E) (<= (+ E Et) B)))
(assert (or (<= (+ D Dt) E) (<= (+ E Et) D)))
(assert (and (<= (+ D Dt) F) (<= (+ E Et) F)))
(assert (<= (+ A At) B))
(assert (<= A (- End At)))
(assert (<= B (- End Bt)))
(assert (<= C (- End Ct)))
(assert (<= D (- End Dt)))
(assert (<= E (- End Et)))
(assert (<= F (- End Ft)))

(check-sat)

(get-model)

(get-value (A B C D E F))

