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

remove_primes()