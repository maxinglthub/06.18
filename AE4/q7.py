def indexOfLongest():

    strlist = []

    string = input("Enter a string(y to stop): ")
    while string != "y":
        string = input("Enter a string: ")   
        strlist.append(string)
     
    for char in string:
        if char == " " or char == "y":
            return None
        else:
            longest = max(strlist) 
            print(strlist.index(longest))
            
        
indexOfLongest()