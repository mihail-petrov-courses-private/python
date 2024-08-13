import profile

def generate():

    controll_sum =  (profile.get_first()    + 
                    profile.get_second()    +
                    profile.get_third()     + 
                    profile.get_forth()     +
                    profile.get_fifth())

    print(controll_sum)

    if controll_sum <= 9:
        return controll_sum
    



    first_controll_digit    = int(controll_sum / 10)
    second_controll_digit   = controll_sum % 10 

    return ( first_controll_digit + second_controll_digit )