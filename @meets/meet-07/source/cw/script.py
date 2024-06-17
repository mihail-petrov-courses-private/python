is_app_running = True

while is_app_running:
    print("Абонаментни планове:")
    print("1.ENTRY")
    print("2.PREMIUM")
    print("3.VIP")
    print("0. не искам да избирам")
    customer_plan           = int(input("Избери план: "))
    is_plan_choose_valid    = (customer_plan >= 1 and customer_plan <= 3)

    if is_plan_choose_valid:
        pass
    elif customer_plan == 0:
        is_app_running = False
        print("Лек ден")
    else:        
        print("няма такъв план, моля изберете отново")