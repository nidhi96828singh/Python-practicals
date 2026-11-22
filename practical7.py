s = input("Enter the main string: ")
sub = input("Enter the substring: ")

indices = []
start = s.find(sub)
while start != -1:
    indices.append(start)
    start = s.find(sub, start + 1)
    

if indices:
    print("Found at indices:", indices)
    print("Occurrences:", len(indices))
else:
    print("Substring not found.")
