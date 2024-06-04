customer_number = 5555
# Ако номера съдържа повече от 2 цифри клиента е от тип EARLY_ADOPTER
is_customer_early_adopter = customer_number > 99 

# Когато налице са следните оператори за СРАВНЕНИЕ
# >
# <
# >=
# <=
# <>
# ==
# Резултата е БУЛЕВА стойност

# Ако клиентския номер съдържа повече от 6 цифри то клиента е LAGGER
is_customer_lagger = customer_number > 99999

# Ако съдържа 6 цифри значи е NORMAL.
# 100 000 - 999 999
is_greather_or_equal_to_100000  = customer_number >= 100000 # True / False
is_lower_or_equal_to_999999     = customer_number <= 999999 # True / False
is_customer_normal              = is_greather_or_equal_to_100000 and is_lower_or_equal_to_999999

# С конструкцията IF правим проверка дали нещо е ИСТИНА. Ако е ИСТИНА изпълняваме
# кода който се намира в тялото на IF

print(is_customer_early_adopter)
print(is_customer_lagger)
print(is_customer_normal)

if is_customer_early_adopter: # само ако е TRUE
    print("Потребителя е от тип EARLY_ADOPTER")

if is_customer_lagger: # само ако е TRUE
    print("Потребителя е от тип LAGGER")

if is_customer_normal: # само ако е TRUE
    print("Потребителя е от тип NORMAL")

print("Продължаваме работа си .....")
