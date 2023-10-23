def run(n):
    if n == 0:
        return
    print("b_n =",n)
    n = n - 1 
    print("N = ",n)
    run(n)
    run(n)
    print("a_n =",n)

run(3)