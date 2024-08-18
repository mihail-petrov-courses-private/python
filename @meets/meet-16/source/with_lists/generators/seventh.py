import util.util as util
import customer.profile as profile

def generate():

    if (    util.is_even(profile.get_number_on_position(1)) and   
            util.is_even(profile.get_number_on_position(3)) and 
            util.is_even(profile.get_number_on_position(5))):
        return 0

    if (    util.is_odd(profile.get_number_on_position(1)) and   
            util.is_odd(profile.get_number_on_position(3)) and 
            util.is_odd(profile.get_number_on_position(5))):
        return 1
    
    if (    util.is_even(profile.get_number_on_position(1)) or   
            util.is_even(profile.get_number_on_position(3)) or 
            util.is_even(profile.get_number_on_position(5))):
        return 2


    if (   
            (
                util.is_even(profile.get_number_on_position(1)) and   
                util.is_even(profile.get_number_on_position(2))
            )
                or
            (
                util.is_even(profile.get_number_on_position(3)) and   
                util.is_even(profile.get_number_on_position(4)) and
                util.is_even(profile.get_number_on_position(5))
            )
        ):
        return 3
    
    if (
        profile.get_number_on_position(1)     == 
        profile.get_number_on_position(2)    == 
        profile.get_number_on_position(3)     == 
        profile.get_number_on_position(4)     == 
        profile.get_number_on_position(5)     == 
        profile.get_number_on_position(6)
    ):
        return 4
    
    if (
        profile.get_number_on_position(1)     < 
        profile.get_number_on_position(2)    < 
        profile.get_number_on_position(3)     < 
        profile.get_number_on_position(4)     < 
        profile.get_number_on_position(5)     < 
        profile.get_number_on_position(6)
    ):
        return 5

    # generate_digit_sum =(   profile.get_number_on_position(1)     + 
    #                         profile.get_number_on_position(2)    + 
    #                         profile.get_number_on_position(3)     + 
    #                         profile.get_number_on_position(4)     + 
    #                         profile.get_number_on_position(5)     + 
    #                         profile.get_number_on_position(6)     )
    
    generate_digit_sum = profile.sum_card_digits_so_far()

    if generate_digit_sum < 10:
        return 6
    
    if generate_digit_sum > 10:
        return 7

    return 9