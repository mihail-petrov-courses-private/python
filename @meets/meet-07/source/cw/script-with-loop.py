# функционалност 1
kitchen_pan_count                   = 5
kitchen_pot_count                   = 5
kitchen_width_dimention             = 450
kitchen_lenght_dimention            = 450
kitchen_heigh_dimention             = 450
kitchen_master_chef_name            = "Ivan"
kitchen_stuff_count                 = 5
kitchen_service_stuff_count         = 5
kitchen_master_sauce_name           = "Dragan"
kitchen_min_temperature             = 45
kitchen_max_temperature             = 48
kitchen_account_ammount             = 5000
kitchen_dayly_turnover_amount       = 10000
kitchen_oppening_time               = 8
kitchen_closing_time                = 22

# трябва да питаме потребителя дали иска да отговаря допълнително
# is_optional_questions_applicable    = (input("Искаш ли да отговориш на въпросите Y/N") == 'Y')
optional_questions_answer             = "Y"
is_optional_questions_applicable      = True

has_refrigerator    = False
has_stove           = False
has_convectomat     = False
has_grill           = False
has_aspiratore      = False

if is_optional_questions_applicable:

    has_refrigerator    = True
    has_stove           = True
    has_convectomat     = True
    has_grill           = True
    has_aspiratore      = True

is_application_running = True

while is_application_running:

    print("Моля изберете вашето ястие:")
    print("1. Месно ястие;")
    print("2. Вегетарианско ястие")
    print("3. Десерт")
    print("4. Изход")
    customer_meal_choise = int(input("Избирам: "))

    if customer_meal_choise == 1:

        is_meal_preparation_active = True

        while is_meal_preparation_active:

            print("Изберете размер на порцията")
            print("SMALL")
            print("MIDIUM")
            print("LARGE")
            portion_size = input("Избирам")  
            is_size_correct = (portion_size == 'SMALL' or portion_size == 'MIDIUM' or portion_size == 'LARGE')

            if is_size_correct:

                can_cook_rare = (
                                    ( has_stove == False            ) and
                                    ( has_grill == True             ) and
                                    (   kitchen_min_temperature >= 36 and 
                                        kitchen_min_temperature <= 48 
                                    )                                 and
                                    ( has_aspiratore    == True     ) and 
                                    ( portion_size      == 'SMALL'  )
                                )

                can_cook_medium = (
                                    ( has_convectomat == True           ) or
                                    ( kitchen_stuff_count == 5          ) or 
                                    ( portion_size == 'MIDIUM'          ) or
                                    ( kitchen_master_chef_name == 'Ivan')
                                )
                
                can_cook_welldone = (
                                    (    
                                        (
                                            kitchen_closing_time == 22
                                        ) 
                                        or
                                        (
                                            kitchen_master_sauce_name == 'Petar' or 
                                            kitchen_master_sauce_name == 'Rado'
                                        )
                                    )
                                    and
                                    (
                                        (
                                            ((kitchen_width_dimention * kitchen_lenght_dimention) / 10000) == 45
                                        )
                                        or 
                                        (
                                            (kitchen_pan_count == 3)
                                            or
                                            (kitchen_pot_count == 2)
                                        )     
                                    )
                                )
                

                can_offer_meal = (  can_cook_rare or  
                                    can_cook_medium or 
                                    can_cook_welldone
                                )
                

                is_meal_preparation_active = False

            
                if can_offer_meal: 
                    
                    is_cook_method_posible = True

                    while is_cook_method_posible:

                        print("Избери си начин на приготвяне")
                        if can_cook_rare:
                            print("RARE")

                        if can_cook_medium:
                            print("MEDIUM")

                        if can_cook_welldone:
                            print("WELL DONE")

                        cook_method_type = input("Избери начин на приготвяне:")
                        is_cook_method_type_valid = (
                                                        cook_method_type == 'RARE' or 
                                                        cook_method_type == 'MEDIUM' or
                                                        cook_method_type == 'WELL DONE' 
                                                    )

                        if is_cook_method_type_valid:
                            is_cook_method_posible = False
                        else:
                            print("Избрахте грешен метод, пробвайте пак")
                else: 
                    print("Нямаме условия за приготвяне на месото")
                
            else:
                print("Не предлагаме такава порция - избери отново")

    elif customer_meal_choise == 2:
        pass
    elif customer_meal_choise == 3:
        pass
    elif customer_meal_choise == 4:
        is_application_running = False
        print("Приятен ден")
    else:
        print("Грешен избор - опитайте отново")