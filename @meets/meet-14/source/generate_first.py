import util

def generate_digit_first(): 
    customer_year = int(input("Кога си роден ?"))

    if customer_year == 1965:
        return 0
    
    # изчислява възрастта на клиента в години, спрямо годината която е въвел;
    customer_age = 2024 - customer_year

    # след това ПОТРЕБИТЕЛЯ ВЪВЕЖДА число в интервала от 1 до 7;
    random_number = int(input("Въведи число в интервала 1 - 7"))

    # разделя възрастта на клиента с това число и полученият резултат се използва като първа цифра.
    result_digit = int(customer_age / random_number)

    if result_digit > 10:
        result_digit = int(result_digit / 10)


    # След като съм сметнал числото
    if (customer_year < 1965) and util.is_odd(result_digit):
        return result_digit
            
    if (customer_year > 1965) and util.is_even(result_digit):
        return result_digit
    
    return result_digit + 1