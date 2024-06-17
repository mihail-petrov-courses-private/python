# функционалност 1
kitchen_pan_count                   = int(input(" Колко тигана има в кухнята?"))
kitchen_pot_count                   = int(input(" Колко тенджери има в кухнята?"))
kitchen_width_dimention             = float(input(" Колко сантиметра е широка кухнята?"))
kitchen_lenght_dimention            = float(input(" Колко сантиметра е дълга кухнята?"))
kitchen_heigh_dimention             = float(input(" Колко сантиметра е висока кухнята?"))
kitchen_master_chef_name            = input(" Как се казва главният готвач?")
kitchen_stuff_count                 = int(input(" Колко готвачи работят в кухнята?"))
kitchen_service_stuff_count         = int(input(" Колко сервитьори работят в ресторанта?"))
kitchen_master_sauce_name           = input(" Как се казва отговорника на сосовете ?")
kitchen_min_temperature             = float(input(" Каква е минималната температура в кухнята?"))
kitchen_max_temperature             = float(input(" Каква е максималната температура в кухнята?"))
kitchen_account_ammount             = float(input(" Колко парички имате в банковата си сметка?"))
kitchen_dayly_turnover_amount       = float(input(" Колко парички е дневният оборот на ресторанта ви?"))
kitchen_oppening_time               = int(input(" В колко часа отваряте?"))
kitchen_closing_time                = int(input(" В колко часа затваряте?"))

# трябва да питаме потребителя дали иска да отговаря допълнително
# is_optional_questions_applicable    = (input("Искаш ли да отговориш на въпросите Y/N") == 'Y')
optional_questions_answer             = input("Искаш ли да отговориш на въпросите Y/N")
is_optional_questions_applicable      = optional_questions_answer == 'Y'

has_refrigerator    = False
has_stove           = False
has_convectomat     = False
has_grill           = False
has_aspiratore      = False

if is_optional_questions_applicable:

    has_refrigerator    = (input("Разполагате ли с хладилник?") == 'Y'          )
    has_stove           = (input("Разполагате ли с газов котлон?") == 'Y'       )
    has_convectomat     = (input("Разполагате ли с конвектомат?") == 'Y'        )
    has_grill           = (input("Разполагате ли с електрическа скара?") == 'Y' )
    has_aspiratore      = (input("Разполагате ли с аспиратор? ") == 'Y'         )


print("Моля изберете вашето ястие:")
print("1. Месно ястие;")
print("2. Вегетарианско ястие")
print("3. Десерт")
customer_meal_choise = int(input("Избирам: "))

if customer_meal_choise == 1:

    portion_size = input("Размер на порцията")  

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
                        ( portion_size == 'MEDIUM'          ) or
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
    

    if can_offer_meal: 

        print("Избери си начин на приготвяне")
        if can_cook_rare:
            print("RARE")

        if can_cook_medium:
            print("MEDIUM")

        if can_cook_welldone:
            print("WELL DONE")
    else: 
        print("Нямаме условия за приготвяне на месото")



    pass # Pass е инструкция без логика, стойност - активност
elif customer_meal_choise == 2:
    pass
elif customer_meal_choise == 3:
    pass
else:
    print("Грешен избор")