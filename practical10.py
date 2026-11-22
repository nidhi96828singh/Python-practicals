n = int(input("Enter n: "))

cubes = {}
for i in range(1, n + 1):
    cubes[i] = i**3
print("Dictionary:", cubes)

# Using dictionary comprehension
print("Comprehension:", {i: i**3 for i in range(1, n + 1)})

for k, v in cubes.items():
    print(k, "->", v)
