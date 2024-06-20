# Потребителя въвежда в системата абонаментен пакет, който иска да закупи. Пакетите са именовани както следва:

# ENTRY
# PREMIUM
# VIP

# Ключ за управление на нашата програма.
while True:

    print("Изберете абонаментен пакет")
    print("ENTRY")
    print("PREMIUM")
    print("VIP")
    customer_plan = input("Избирам пакет: ")
    is_customer_plan_valid = (  
                                customer_plan == 'ENTRY'   or 
                                customer_plan == 'PREMIUM' or
                                customer_plan == 'VIP'
                            )
    
    if is_customer_plan_valid:

        while True:

            print("За какъв период искаш да се абонираш")
            print("1. месеци")
            print("2. години")
            customer_plan_period_id = input("Избирам период: ")
            is_customer_plan_period_id_valid = (customer_plan_period_id == "1" or
                                                customer_plan_period_id == "2")
            

            if is_customer_plan_period_id_valid:
                
                while True:

                    is_plan_period_count_valid = False

                    # Месеци
                    if customer_plan_period_id == "1":

                        print("Изберете броя на месеците, за които искате да се абонирате 1 - 24")
                        plan_period_count           = int(input("Въведете броя на месеците: "))
                        is_plan_period_count_valid  = (
                                                        plan_period_count >= 1 and 
                                                        plan_period_count <= 24
                                                    )

                    if customer_plan_period_id == "2":

                        print("Изберете броя на годините, за които искате да се абонирате 1 - 2")
                        plan_period_count = int(input("Въведете броя на годините: "))
                        is_plan_period_count_valid = (
                                                        plan_period_count == 1 or 
                                                        plan_period_count == 2
                                                    )

                    if is_plan_period_count_valid:
                        pass
                    else:
                        print("Грешна стойност - моля опитайте отново")


            else:
                print("Грешен избор - моля опитайте отново")

    else:
        print("Грешен избор - моля опитайте отново")