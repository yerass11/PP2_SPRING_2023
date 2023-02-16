n = int(input())
def foo(n):
    for i in range(n):
        for j in range(2 * n):
            if j >= n - i and j <= n + i:
                print("*", end="")
            else:
                print(" ", end="")
        print()
foo(n)


