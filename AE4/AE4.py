#Q1
def GCD():

    number_1 = 4
    number_2 = 9

    CF_number = 1
    Biggest_CF_number = 0

    for i in range(1, min(number_1, number_2) + 1):
        if number_1 % CF_number == 0 and number_2 % CF_number == 0:
            Biggest_CF_number = CF_number
            CF_number = CF_number + 1
        else:
            CF_number = CF_number + 1
    return Biggest_CF_number

#Q2
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

#Q3
def printUniqueThreeDigits():
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if i != j and j != k and i != k:
                    print(f"{i}{j}{k}", end = " ")
    
#Q4
def calculatePI(n):
    function = 0.0
    pn = 1
    
    for i in range(1, n + 1, 2):
        n_function = pn * (1/i)
        pn = pn * -1
    
    function = 4 * n_function
    return function

#Q5
def isUpper(text):
    for char in text:
        if char.isupper():
            return False
    return True

#Q6
def commonChars():
    string_1 = "Common"
    string_2 = "come"
    for char in string_1:
        if char in string_2:
            return char
        
#Q7
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

#Q8
def longest_duplicates():
    nums = [1, 3, 3, 7, 8, 8, 8, 20 ,20, 30]
    max_count = 1
    count = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            count = count + 1
            if count > max_count:
                max_count = count
        else:
            count = 1

    return max_count

#Q9
def remove_primes():
    list_1 = [2, 4, 7, 8, 9, 10]

    for i in range(len(list_1) - 1, -1, -1):
        if check_prime(list_1[i]):
            list_1.remove(list_1[i])
    print(list_1)

def check_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True