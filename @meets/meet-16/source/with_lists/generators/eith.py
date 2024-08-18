import random
import customer.profile as profile
import util.util as util

def generate():

    if (profile.is_adoult() and
            profile.is_customer_overweight() and
            profile.get_prefered_product_category() == 5 and
            profile.get_prefered_product_frequancy() == 3):
        
        # генерираме случайно нечетно число
        while True:

            result = random.randint(1, 9)
            if util.is_odd(result):
                return result

    if (not profile.is_minor() and
            profile.get_bmi() == 3 and
            profile.get_prefered_product_category() == 1 and
            profile.get_prefered_product_frequancy() == 1):
        
        # генерираме случайно четно число
        while True:

            result = random.randint(1, 9)
            if util.is_even(result):
                return result
    
    return 0



