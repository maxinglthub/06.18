#part a
def sumUpFactorsOf(n):
    total = 0
    for i in range(1, n + 1):
        if n % i == 0:
            total += i
    return total

#top level
n = int(input("how many integers?: "))

largestNum = int(input("Enter integer: "))
largestSum = sumUpFactorsOf(largestNum)

for i in range (n - 1):
    num = int(input("Enter integer: "))
    factors = sumUpFactorsOf(num)
    if factors > largestSum:
        largestNum = num
        largestSum = factors
print(largestNum, "ha the largest sum of factors:", largestSum)