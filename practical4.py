ch = input("Enter a single character: ")

if len(ch) != 1:
    print("Please enter exactly one character.")
elif ch.isalpha():
    kind = "uppercase" if ch.isupper() else "lowercase"
    if ch.lower() in "aeiou":
        print(ch, "is a", kind, "vowel")
    else:
        print(ch, "is a", kind, "consonant")
elif ch.isdigit():
    print(ch, "is a digit")
elif ch.isspace():
    print("It is a whitespace character")
else:
    print(ch, "is a special character")
