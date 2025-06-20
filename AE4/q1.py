def GCD():

    number_1 = 4
    number_2 = 9

    check = True
    CF_number = 1
    Biggest_CF_number = 0

    while check == True:
        if number_1 % CF_number == 0 and number_2 % CF_number == 0:
            CF_number = CF_number + 1
            Biggest_CF_number = CF_number
        else:
            CF_number = CF_number + 1
        if number_1 // 2 < CF_number or number_2 // 2 < CF_number:
            return Biggest_CF_number

ans = GCD()
print("the GCD is: ", ans)
