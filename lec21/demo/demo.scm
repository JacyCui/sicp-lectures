; Definitions
(define (square x) (* x x))

(define (average x y) (/ (+ x y) 2))

(define pi 3.14)

(define (abs x)
    (if (< x 0) (- x) x )
)

(define sum-square
    (lambda (x y) (+ (square x) (square y)))
)

(define (fib n)
    (cond ((= n 0) 0)
        ((= n 1) 1)
        (else (+ (fib (- n 1)) (fib (- n 2))))
    )
)

; cons = construction
(define a (cons 1 (cons 2 (cons 3 (cons 4 nil)))))

; car = content of the address register
; get the first element of a linked list
(define a1 (car a))

; cdr = content of the decrement register
; get the rest of a linked list
(define b (cdr a))

; the first of a linked list can be a linked list
(define c (cons 0 (cons (cons 1 (cons 2 (cons 3 nil))) (cons 4 (cons 5 nil)))))

(define (sum-while starting-x while-condition add-to-total update-x)
    `(begin
        (define (f x total)
            (if ,while-condition
                (f ,update-x (+ total ,add-to-total))
                total
            )
        )
        (f ,starting-x 0)
    )
)
; (eval (sum-while 2 '(< x 10) '(* x x) '(+ x 2))) => 120
; (eval (sum-while 1 '(< (* x x) 50) 'x '(+ x 1))) => 28

