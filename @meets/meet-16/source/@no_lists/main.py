import customer.profile as profile

import generators.first    as first
import generators.second   as second
import generators.third    as third
import generators.forth    as forth
import generators.fifth    as fifth
import generators.sixth    as sixth
import generators.seventh  as seventh
import generators.eith     as eith
import generators.ninth    as ninth

first_digit     = first.generate()
profile.set_first(first_digit)
second_digit    = second.generate()
profile.set_second(second_digit)
third_digit     = third.generate()
profile.set_third(third_digit)
forth_digit     = forth.generate() 
profile.set_forth(forth_digit)
fifth_digit     = fifth.generate()
profile.set_fifth(fifth_digit)
sixth_digit     = sixth.generate() 
profile.set_sixth(sixth_digit)

seventh_digit     = seventh.generate() 
profile.set_seventh(seventh_digit)

eith_digit     = eith.generate() 
profile.set_eith(eith_digit)

ninth_digit     = ninth.generate() 

print(f'Първа {first_digit}')
print(f'Втора {second_digit}')
print(f'Трета {third_digit}')
print(f'Четвърта {forth_digit}')
print(f'Пета {fifth_digit}')
print(f"Шест {sixth_digit}")
print(f"Седем {seventh_digit}")
print(f"Осем {eith_digit}")
print(f"Девет {ninth_digit}")


# bar_code = ['*','!','@','#','$','%','^','&',0]
