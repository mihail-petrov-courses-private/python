# Въвеждаме си паролата - от конзолата
# * Ако паролата е вярна - ВСИЧКО е точно и спираме да караме клиента да въвежда. 
# * Ако я объркаме три пъти - тогава системата ни заключва акаунта и ни спира възможността
# да въвеждаме повече

true_password           = "password"
password_input_attempt  = 0

while True:
    input_password = input("Въведете парола: ")

    if input_password == true_password:
        print("Успешен вход")
        break

    # Приемам че ако не си успял да влезеш, автоматично„
    # паролата ти е объркана
    # password_input_attempt = password_input_attempt + 1
    password_input_attempt += 1
    
    if password_input_attempt == 3:
        print("Вашия акаунт е заключен")
        break
    else:
        print("Въведохте грешна парола. Остават ви " + str(3 - password_input_attempt) + " опита")


# Вариант на цикъла с брояч
true_password           = "password"
password_attempt_fail   = 0

while password_attempt_fail <= 3:

    password_input = input("въведи парола")

    if password_input == true_password:
        print("Добре дошли")
        break
    
    password_attempt_fail += 1
    print("Грешна парола")

    if password_attempt_fail == 3:
        print("Акаунта е заключен")
