CUSTOMER_BIRTH_YEAR = -1

def set_customer_birth_date(year):
    global CUSTOMER_BIRTH_YEAR
    CUSTOMER_BIRTH_YEAR = year

def get_customer_age():
    return 2024 - CUSTOMER_BIRTH_YEAR

def is_adoult():
    return get_customer_age() >= 18
    