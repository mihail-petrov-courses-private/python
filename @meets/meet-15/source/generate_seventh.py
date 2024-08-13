import util
import profile

def generate():

    if (    util.is_even(profile.get_first()) and   
            util.is_even(profile.get_third()) and 
            util.is_even(profile.get_fifth())):
        return 0

    if (    util.is_odd(profile.get_first()) and   
            util.is_odd(profile.get_third()) and 
            util.is_odd(profile.get_fifth())):
        return 1
    
    if (    util.is_even(profile.get_first()) or   
            util.is_even(profile.get_third()) or 
            util.is_even(profile.get_fifth())):
        return 2


    if (   
            (
                util.is_even(profile.get_first()) and   
                util.is_even(profile.get_second())
            )
                or
            (
                util.is_even(profile.get_third()) and   
                util.is_even(profile.get_forth()) and
                util.is_even(profile.get_fifth())
            )
        ):
        return 3
    
    if (
        profile.get_first()     == 
        profile.get_second()    == 
        profile.get_third()     == 
        profile.get_forth()     == 
        profile.get_fifth()     == 
        profile.get_sixth()
    ):
        return 4
    
    if (
        profile.get_first()     < 
        profile.get_second()    < 
        profile.get_third()     < 
        profile.get_forth()     < 
        profile.get_fifth()     < 
        profile.get_sixth()
    ):
        return 5

    generate_digit_sum =(   profile.get_first()     + 
                            profile.get_second()    + 
                            profile.get_third()     + 
                            profile.get_forth()     + 
                            profile.get_fifth()     + 
                            profile.get_sixth()     )
    
    if generate_digit_sum < 10:
        return 6
    
    if generate_digit_sum > 10:
        return 7

    return 9