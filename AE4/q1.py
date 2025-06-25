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

ans = GCD()
print("the GCD is: ", ans)
