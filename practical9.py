fname = "sample.txt"

with open(fname, "w") as f:
    f.write("Hello, this is the first line.\n")
    f.write("Python file handling practical.\n")

with open(fname, "a") as f:
    f.write("This line was appended.\n")

print("--- File contents ---")
with open(fname, "r") as f:
    content = f.read()
    print(content)

with open(fname, "r") as f:
    lines = f.readlines()
print("Number of lines:", len(lines))
print("Number of words:", len(content.split()))
print("Number of characters:", len(content))
