def run(n):
    if n == 0:
        return
    print("UL")
    run(n-1)
    print(n)

n = 3
run(n)
print("completed")
