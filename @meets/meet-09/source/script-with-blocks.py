# Общт цикъл
OPERATION_FLAG = 1

while True:

    plan_id

    # Операция 1 - Избор на планове
    if OPERATION_FLAG == 1:

        while True:

            print("Избери си пакет")
            print("ENTRY")
            print("PREMIUM")
            print("VIP")
            print("EXIT")
            customer_plan = input("избери: ")
            is_customer_plan_valid = (
                                        customer_plan == 'ENTRY' or
                                        customer_plan == 'PREMIUM' or
                                        customer_plan == 'VIP'
            )

            if is_customer_plan_valid:
                OPERATION_FLAG = 2


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

    # Избор на период - стойност
    if OPERATION_FLAG == 3:

        while True:

            is_plan_value_valid     = False
            is_applicable_for_price = False

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