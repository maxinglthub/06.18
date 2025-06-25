def largestFibLessThan(N):
    save = 0
    number = 0
    ram = 0
    add = 1
    
    for i in range(1, N - 1):
        number = add + ram
        if number >= N:
            save = add
            return save
        ram = add
        add = number

ans = largestFibLessThan(30)
print("The ans is: ", ans)