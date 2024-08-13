def generate():

    # category_index = get_category_index()
    # frequancy_index = get_frequancy_index()

    # return category_index + frequancy_index

    return get_category_index() + get_frequancy_index()



def get_category_index():

    while True:
        print("Какво обичаш да пазаруваш:")
        print("1.плодове и зеленчуци; ")
        print("2.месо и местни; ")
        print("3.цигари и алкохол; ")
        print("4.млечни продукти; ")
        print("5.захарни изделия; ")

        category_index = int(input("Каква категория продукти пазарувате"))
        if category_index >= 1 and category_index <= 5:
            return category_index

        print("Невалидни стойности - избери валидна категория")


def get_frequancy_index():

    while True:
        print("Колко често консумираш")
        print("1. рядко")
        print("2. понякога")
        print("3. често")

        frequancy_index = int(input("Колко често консумираш"))
        if frequancy_index >= 1 and frequancy_index <= 3:
            return frequancy_index

        print("Невалидни стойности - избери валидна честота")