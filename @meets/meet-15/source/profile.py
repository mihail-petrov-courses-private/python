CUSTOMER_BIRTH_YEAR = -1

FIRST_DIGIT = -1
SECOND_DIGIT = -1
THIRD_DIGIT = -1
FORTH_DIGIT = -1
FIFTH_DIGIT = -1
SIXTH_DIGIT = -1

def set_customer_birth_date(year):
    global CUSTOMER_BIRTH_YEAR
    CUSTOMER_BIRTH_YEAR = year

def get_customer_age():
    return 2024 - CUSTOMER_BIRTH_YEAR

def is_adoult():
    return get_customer_age() >= 18
    
def set_first(value):
    global FIRST_DIGIT
    FIRST_DIGIT = value

def get_first():
    return FIRST_DIGIT

def set_second(value):
    global SECOND_DIGIT
    SECOND_DIGIT = value

def get_second():
    return SECOND_DIGIT

def set_third(value):
    global THIRD_DIGIT
    THIRD_DIGIT = value

def get_third():
    return THIRD_DIGIT

def set_forth(value):
    global FORTH_DIGIT
    FORTH_DIGIT = value

def get_forth():
    return FORTH_DIGIT

def set_fifth(value):
    global FIFTH_DIGIT
    FIFTH_DIGIT = value

def get_fifth():
    return FIFTH_DIGIT


def set_sixth(value):
    global SIXTH_DIGIT
    SIXTH_DIGIT = value

def get_sixth():
    return SIXTH_DIGIT