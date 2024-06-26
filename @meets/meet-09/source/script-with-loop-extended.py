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
    
    if customer_plan == "EXIT":
        break

    if is_customer_plan_valid:

        # ВТОРО НИВО

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
                break
            
            if is_plan_id_valid:
                pass
            else:
                print("грешка - опитай отново")
    else:
        print("грешка - опитай отново")

    print("Лек ден -- от първи цикъл")

print("Лек ден")