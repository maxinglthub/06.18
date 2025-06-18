sumUpFactorsOf = int(input("Pls enter a number: "))
n = 0
factor = 2
limit = sumUpFactorsOf
stop = True

if factor == limit:
    print(n)
elif sumUpFactorsOf % factor == 0:
    n = sumUpFactorsOf
    factor = factor + 1


while stop == True:
    if sumUpFactorsOf % factor == 0:
        n = n + sumUpFactorsOf
        if factor == limit:
            print(n)
            stop = False
    
    factor = factor + 1
    #hfueuoboe