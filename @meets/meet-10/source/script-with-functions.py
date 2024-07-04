# Функция - която ще проверява дали customer_plan е валиден
# Аргумента - локална променлива, която носи данните 
# от външния свят
def check_is_customer_plan_valid(a):

    is_valid = (a == 'ENTRY'    or
                a == 'PREMIUM'  or
                a == 'VIP')
    
    return is_valid


# Напишете функция която да принтира плановете да очаква входни данни и да ги връща
def print_customer_plan():

    print("Избери си пакет")
    print("ENTRY")
    print("PREMIUM")
    print("VIP")
    print("EXIT")
    customer_plan = input("избери: ")
    return customer_plan


# Общт цикъл
OPERATION_FLAG = 1

while True:

    customer_plan   = ''
    plan_id         = ''
    plan_value      = 0
    price_input     = ''

    is_applicable_for_price = False

    # Операция 1 - Избор на планове
    if OPERATION_FLAG == 1:

        while True:

            # print("Избери си пакет")
            # print("ENTRY")
            # print("PREMIUM")
            # print("VIP")
            # print("EXIT")
            # customer_plan = input("избери: ")
            customer_plan = print_customer_plan()

            # Подабав променливата customer_plan
            # Тя ми носи информацията която трябва да проверя
            is_customer_plan_valid = check_is_customer_plan_valid(customer_plan)

            # is_customer_plan_valid = (
            #                             customer_plan == 'ENTRY' or
            #                             customer_plan == 'PREMIUM' or
            #                             customer_plan == 'VIP'
            # )

            if is_customer_plan_valid:
                OPERATION_FLAG = 2
                break


    # Операция 2 - Избор на период - идентификатор
    if OPERATION_FLAG == 2:

        while True:
            print('Избери идентификатор за период')
            print('1. месеци')
            print('2. години')
            print('0. НАЗАД')
            plan_id          = input('Избери идентификатор на период')
            is_plan_id_valid = (
                                plan_id == "1" or
                                plan_id == "2"
            )

            if plan_id == "0":
                # OPERATION_FLAG = OPERATION_FLAG - 1
                # декрементация
                OPERATION_FLAG -= 1
                break

            if is_plan_id_valid:
                OPERATION_FLAG = 3
                break

    # Избор на период - стойност
    if OPERATION_FLAG == 3:

        while True:

            is_plan_value_valid     = False
            

            if plan_id == "1":
                print("Въведи стойност от 1 - 24")
                plan_value              = int(input("Избери стойност"))
                is_plan_value_valid     = (plan_value >= 1 and plan_value <= 24)
                is_applicable_for_price = (plan_value == 24)
            
            if plan_id == "2":
                print("Въведи стойност от 1 - 2")
                plan_value              = int(input("Избери стойност"))
                is_plan_value_valid     = (plan_value >= 1 and plan_value <= 2)
                is_applicable_for_price = (plan_value == 2)

            #  ОТИДИ НА СТЪПКА 4
            if is_applicable_for_price:
                OPERATION_FLAG = 4
                break

            if is_plan_value_valid:
                OPERATION_FLAG = 5
                break

    # Избор на награда
    if OPERATION_FLAG == 4:

        while True:
            print("Изберете си награда")
            print("1. телевизор")
            print("2. телефон")
            print("0. НАЗАД")
            price_input = input("избери")
            is_price_input_valid = (price_input == "1" or price_input == "2")

            if price_input == "0":
                OPERATION_FLAG = 3
                break

            if is_price_input_valid:
                OPERATION_FLAG = 5
                break

    # Приключваме изпълнението на програмата
    if OPERATION_FLAG == 5:

        # message_id = 'години'
        # if plan_id == "1":
        #     message_id = 'месеци'
        # else:
        #     message_id = 'години'

        # Троен оператор
        message_id = "месеци" if plan_id == "1" else "години"


        price_id = ''
        price_message = ''
        if is_applicable_for_price:

            if price_input == "1":
                price_id = 'телевизор'
            else:
                price_id = 'телефон'

            price_message = ' имате подарък ' + price_id


        # message = "Вие избрахте " + customer_plan + " , за период от " + str(plan_value) + " " + message_id + " " + price_message

        # Интерполация на низове
        message = f"Вие избрахте {customer_plan}, за период от {plan_value} {message_id} {price_message}"
        print(message)
        break
        #  Вие избрахте {ИМЕ НА ПАКЕТА}, за период от {N} {месеци / години } имате подарък.
