n = int(input("Enter number of rows: "))

print("\nPattern 1: Right triangle")
for i in range(1, n + 1):
    print("*" * i)

print("\nPattern 2: Inverted triangle")
for i in range(n, n - 1):
    print("*" * i)

print("\nPattern 3: Pyramid")
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

print("\nPattern 4: Inverted pyramid")
for i in range(n, 0, -1):
    print(" " * (n - i) + "* " * i)

print("\nPattern 5: Diamond")
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)
