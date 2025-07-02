def indexOfLongest():

    strlist = ["cmpt", "120", "!"]
    max_index = 0
    largest = strlist[0]

    if len(strlist) == 0:
        return 0

    for i in range(1, len(strlist)):
        if len(strlist[i]) > len(strlist[i-1]):
            largest = strlist[i]
            max_index = i
    
    return max_index
        
indexOfLongest()