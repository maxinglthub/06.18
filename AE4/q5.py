def isUpper():
    for char in text:
        if char.isupper():
            return False
    return True

text = (input("Enter a string: "))
ans = isUpper()
print(ans)