is_app_runnin               = True

# ========================================================
# ПЪРВО НИВО НА ПРОВЕРКА - ПАКЕТ
# ========================================================
while is_app_runnin:

    is_customer_plan_running = True

    print("Избери си пакет")
    print("ENTRY")
    print("PREMIUM")
    print("VIP")
    customer_plan = input("избери: ")
    is_customer_plan_valid = (
                                customer_plan == "ENTRY" or
                                customer_plan == "PREMIUM" or
                                customer_plan == "VIP"
                            )

    if is_customer_plan_valid:
        
        # ========================================================
        # ВТОРО НИВО НА ПРОВЕРКА - ИДЕНТИФИКАТОР ЗА ПЕРИОД
        # ========================================================

        while is_customer_plan_running:

            is_plan_count_running = True

            print("Избери си идентификатор за периода")
            print("1. месеци")
            print("2. години")
            print("0. НАЗАД")
            plan_period_id          = input("избери: ")
            is_plan_period_id_valid = (
                                        plan_period_id == "1" or 
                                        plan_period_id == "2"
                                    ) 

            if plan_period_id == "0":
                is_customer_plan_running = False
            else:

                if is_plan_period_id_valid:
                    
                # ========================================================
                # ТРЕТО НИВО НА ПРОВЕРКА - КОЛИЧЕСТВО
                # ========================================================                

                    while is_plan_count_running:
                        plan_period_count = 0
                        is_plan_period_count_valid = False

                        # Избрал съм месеци
                        if plan_period_id == "1":
                            print("Изберете количество от 1 - 24")
                            print("Или 0 за да се върнете назад")
                            plan_period_count           = int(input("избери: "))
                            is_plan_period_count_valid  =  (
                                                            plan_period_count >= 1 and plan_period_count <= 24
                                                            )
                        
                        if plan_period_id == "2":
                            print("Изберете количество от 1 - 2")
                            print("Или 0 за да се върнете назад")
                            plan_period_count           = int(input("избери: "))
                            is_plan_period_count_valid  = (
                                                            plan_period_count == 1 or
                                                            plan_period_count == 2
                                                        )
                            
                        if plan_period_count == 0:
                            is_plan_count_running = False
                        else:
                            if is_plan_period_count_valid:
                                
                                # ========================================================
                                # ЧЕТВЪРТО НИВО НА ПРОВЕРКА - НАГРАДА
                                # ========================================================                
                                is_applicable_for_price = (
                                                            (plan_period_id == "1" and plan_period_count == 24) or
                                                            (plan_period_id == "2" and plan_period_count == 2)
                                )

                                if is_applicable_for_price:

                                    while is_app_runnin:
                                        print("Изберете си награда")
                                        print("1. Телевизор")
                                        print("2. Телефон")
                                        price_id = input("изберете: ")
                                        is_price_id_valid = price_id == "1" or price_id == "2"

                                        if is_price_id_valid:
                                            
                                            id = ""
                                            if plan_period_id == "1" and plan_period_count == 1:
                                                id = "месец"
                                            elif plan_period_id == "1":
                                                id = "месеци" 
                                            elif plan_period_id == "2" and plan_period_count == 1:
                                                id = "година"
                                            elif plan_period_id == "2":
                                                id = "години"

                                            price_name = ""
                                            if price_id == "1":
                                                price_name = "ТЕЛЕВИЗОР"
                                            elif price_id == "2":
                                                price_name = "ТЕЛЕФОН"

                                            print("Ти избра пакет " + customer_plan + " за период от " + str(plan_period_count) + id + " ти спечели " + price_name )

                                            is_app_runnin = False

                                        else:
                                            print("въведе грешна стойност за награда - дай пак")

                                else:

                                    id = ""
                                    if plan_period_id == "1" and plan_period_count == 1:
                                        id = "месец"
                                    elif plan_period_id == "1":
                                        id = "месеци" 
                                    elif plan_period_id == "2" and plan_period_count == 1:
                                        id = "година"
                                    elif plan_period_id == "2":
                                        id = "години"

                                    print("Ти избра пакет " + customer_plan + " за период от " + str(plan_period_count) + id )

                                    is_app_runnin = False
                            else:
                                print("грешен период - пробвай пак")

                else:
                    print("грешна стойност - пробвай пак")
    
    else:
        print("грешна стойност - пробвай пак")