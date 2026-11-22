n = int(input("Enter upper limit: "))

# Using a loop
for i in range(2, n + 1, 2):
    print(i, "->", i**3)

# Using list comprehension
print("Cubes:", [i**3 for i in range(1, n + 1) if i % 2 == 0])
