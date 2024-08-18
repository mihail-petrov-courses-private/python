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

age_collection = [11, 55, 18, 5, 24]
for element in age_collection:
    print(element)







first_digit     = first.generate()
profile.add_next_card_digit(first_digit)
second_digit    = second.generate()
profile.add_next_card_digit(second_digit)
third_digit     = third.generate()
profile.add_next_card_digit(third_digit)
forth_digit     = forth.generate() 
profile.add_next_card_digit(forth_digit)
fifth_digit     = fifth.generate()
profile.add_next_card_digit(fifth_digit)
sixth_digit     = sixth.generate() 
profile.add_next_card_digit(sixth_digit)

seventh_digit     = seventh.generate() 
profile.add_next_card_digit(seventh_digit)

eith_digit     = eith.generate() 
profile.add_next_card_digit(eith_digit)

ninth_digit     = ninth.generate() 
profile.add_next_card_digit(ninth_digit)

for card_number in profile.card_number_collection:
    print(card_number)

# print(f'Първа {first_digit}') 
# print(f'Втора {second_digit}')
# print(f'Трета {third_digit}')
# print(f'Четвърта {forth_digit}')
# print(f'Пета {fifth_digit}')
# print(f"Шест {sixth_digit}")
# print(f"Седем {seventh_digit}")
# print(f"Осем {eith_digit}")
# print(f"Девет {ninth_digit}")


bar_code = ['*','!','@','#','$','%','^','&','/', '+']

print("========================================")
print(f'Баркод Първа {bar_code[first_digit]}') 
print(f'Баркод Втора {bar_code[second_digit]}')
print(f'Баркод Трета {bar_code[third_digit]}')
print(f'Баркод Четвърта {bar_code[forth_digit]}')
print(f'Баркод Пета {bar_code[fifth_digit]}')
print(f"Баркод Шест {bar_code[sixth_digit]}")
print(f"Баркод Седем {bar_code[seventh_digit]}")
print(f"Баркод Осем {bar_code[eith_digit]}")
print(f"Баркод Девет {bar_code[ninth_digit]}")
