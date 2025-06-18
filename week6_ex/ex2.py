import random

def roll_dice(number):
    total = 0
    for i in range(1, number + 1):
        number = random.randint(1, 7)
        print("the number is: ", number)
        total = total + number
    return total


n = int(input("Enter the number: "))
ans = roll_dice(n)
print(ans)