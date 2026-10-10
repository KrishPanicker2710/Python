def f(n):
    return 1 if n <= 1 else n * f(n - 1)
n = int(input("Number: "))
print(f(n) if n >= 0 else "Invalid")