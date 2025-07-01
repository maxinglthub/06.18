def calculatePI(n):
    function = 0.0
    pn = 1
    
    for i in range(1, n + 1, 2):
        n_function = pn * (1/i)
        pn = pn * -1
    
    function = 4 * n_function
    return function


number = int(input("Enter the N: "))
ans = calculatePI(number)
print("The value of PI is: ", ans)