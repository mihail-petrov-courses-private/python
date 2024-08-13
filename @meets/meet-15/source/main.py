import profile

import generate_first
import generate_second
import generate_third
import generate_forth
import generate_fifth
import generate_sixth

first_digit     = generate_first.generate()
profile.set_first(first_digit)
second_digit    = generate_second.generate()
profile.set_second(second_digit)
third_digit     = generate_third.generate()
profile.set_third(third_digit)
forth_digit     = generate_forth.generate() 
profile.set_forth(forth_digit)
fifth_digit     = generate_fifth.generate()
profile.set_fifth(fifth_digit)

sixth_digit     = generate_sixth.generate() 
profile.set_sixth(sixth_digit)


print('Първа')
print(first_digit)

print('Втора')
print(second_digit)

print('Трета')
print(third_digit)

print('Четвърта')
print(forth_digit)

print('Пета')
print(fifth_digit)

print("Шест")
print(sixth_digit)