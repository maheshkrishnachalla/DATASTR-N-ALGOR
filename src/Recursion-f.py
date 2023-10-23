def run(n):
    if n == 0:
        return
    print("b_n =",n)
    run(n - 1)
    print("a_n =",n)
    run(n - 1)

run(3)