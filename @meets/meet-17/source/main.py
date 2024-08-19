# translation_str = "Hello world"
# print(translation_str[0])

serial_number = "19924754789654"

def serial_number_print(serial_number):

    # добавяме два списъка
    # първия съдържа само четни числа
    even_number_collection = []
    
    # втория съдържа само нечетни числа
    odd_number_collection = []

    for element in serial_number:
        element_number  = int(element);
        result          = element_number + 1

        # Троен оператор
        # print_result    = 0 if result == 10 else result

        # Стандартен IF
        if result == 10:
           result = 0
    
        if result % 2 == 0:
            even_number_collection.append(result)
        else:
            odd_number_collection.append(result)

        # Принтираме четните 
    print(odd_number_collection)

        # Принтираме нечетните
    print(even_number_collection)

    # Сравнете ДЪЛЖИНИТЕ на двата списъка
    # В по късия налейте толкова -1, колкото са необходими за да се 
    # изравни дължината двата списъка

    # if len(odd_number_collection) > len(even_number_collection):
    while len(odd_number_collection) > len(even_number_collection):
        even_number_collection.append(-1)

    # if len(even_number_collection) > len(odd_number_collection):
    while len(even_number_collection) > len(odd_number_collection):
        odd_number_collection.append(-1)
        

    # Принтираме четните 
    print(odd_number_collection)

        # Принтираме нечетните
    print(even_number_collection)

    #  Да се направи трети списък които да се НАПЪЛНИ със сумата от елементите 
    # на всеки един от двата масива odd и even
    # odd   -> [1,3,5,7]
    # even  -> [2,4,6,8]
    # total -> [3, 7, 11, 15]


serial_number_print(serial_number)


# 1. Обхождаме серииния номер
# 2. Всяко число го събираме с единица
# 3. Ако резултата от сбора е 10 - принтираме 0
# 4. Всеки резултат трябва да бъде принтиран

# Ползваме - FOR цикъл
# помислете за операции по трансформация на данни