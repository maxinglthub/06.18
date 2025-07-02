def commonChars():
    string_1 = "Common"
    string_2 = "come"
    for char in string_1:
        if char in string_2:
            return char

commonChars()