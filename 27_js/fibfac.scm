;Team Grizzly :: Alex Luo, Stanley Hoo
;SoftDev pd4
;K27 - Basic functions in JavaScript
;2025-01-06m

;Scheme antecedents for JavaScript work


;factorial:
(define fact 
    (lambda (n)
        (if (<= n 1)
                1
                (* n (fact (- n 1))))))


;TEST CALLS
(fact 1) ;"...should be  1"
(fact 2) ;"...should be  2"
(fact 3) ;"...should be  6"
(fact 4) ;"...should be  24"
(fact 5) ;"...should be  120"


;-----------------------------------------------------------------


;fib:

(define fib
    (lambda (n)
        (if (= n 0)
            0
            (if (= n 1)
                1
                (+ (fib(- n 1))(fib(- n 2)))))))


;TEST CALLS
(fib 0) ;"...should be  0"
(fib 1) ;"...should be  1"
(fib 2) ;"...should be  1"
(fib 3) ;"...should be  2"
(fib 4) ;"...should be  3"

;=================================================================