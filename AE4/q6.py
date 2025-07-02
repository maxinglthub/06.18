def commonChars():
    string_1 = input("Enter the first string: ")
    string_2 = input("Enter the second string: ")
    for char in string_1:
        if char in string_2:
            print(char, end = " ")

commonChars()