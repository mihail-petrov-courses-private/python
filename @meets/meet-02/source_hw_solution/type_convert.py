# Трансформиране на типове данни с помоща на функциите
# int() -> превръща ТЕКСТ в ЦЯЛО ЧИСЛО
# float() -> превръща ТЕКСТ в ДРОБНО ЧИСЛО
# str() -> превръща НЕЩО в ТЕКСТ
weight_string = input('колко тежиш') # 100
weight_number = float(weight_string)

weight_increase = input('с колко искаш да напълнееи') # 10
weight_increase_number = int(weight_increase)

weight_decrease = input('с колко искаш да отслабнеш') # 20
weight_decrease_number = int(weight_decrease)

weight_increase_sum     = weight_number + weight_increase_number
weight_increase_string  = str(weight_increase_sum)

print("Резултат "  + weight_increase_string) # 110
print(weight_number - weight_decrease_number) # 80

# Да разпишем горната програма малко по кратко 
# Този вариант е НАПЪЛНО функционален
weight          = float(input('колко тежиш')) # 100
weight_increase = int(input('с колко искаш да напълнееи')) # 10
weight_decrease = int(input('с колко искаш да отслабнеш')) # 20

print("Резултат "  + str(weight + weight_increase)) # 110


#  ФУНКЦИИТЕ - могат да трансофрират ТИПОВЕТЕ ДАННИ от един в друг
#  Една стойност може да прилича на ЧИСЛО но да е дефакто ТЕКСТ
#  ако искам да превърна ТЕКСТ в цяло число ->  int(ТЕКСТ) и връща ЦЯЛО ЧИСЛО
