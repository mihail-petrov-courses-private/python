import customer.profile as profile

def generate():

    controll_sum =  profile.sum_card_digits_so_far()

    if controll_sum <= 9:
        return controll_sum
    
    first_controll_digit    = int(controll_sum / 10)
    second_controll_digit   = controll_sum % 10 
    result_sum              = first_controll_digit + second_controll_digit

    if result_sum == 10:
        return 1
    
    return result_sum