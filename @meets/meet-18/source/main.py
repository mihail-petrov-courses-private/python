# Да свържем 
# СИМВОЛ - с друг - СИМВОЛ
# РЕЧНИЦИ - dictunary / map
character_map = {
    "a" :	"@(",
    "b" :	"!@",
    "c" :	"(",
    "d" :	"@!",
    "e" :	"(-",
    "f" :	"!-",
    "g" :	"&",
    "h" :	"!%",
    "i" :	"!",
    "j" :	".!",
    "k" :	"!<",
    "l" :	"!!",
    "m" :	"^^",
    "n" :	"%",
    "o" :	"()",
    "p" :	"!^@",
    "q" :	"!.@",
    "r" :	"@<",
    "s" :	")(",
    "t" :	"/_",
    "u" :	"^>",
    "v" :	"<!>",
    "w" :	"><",
    "x" :	"<>",
    "y" :	".=.",
    "z" :	"#$",
}

# Взимаме думата
# intervenzia
# И за всеки нейн символ - който можем да вземем
# като обходим думата символ по символ в ЦИКИЛ
# За всеки символ - правим проверка в РЕЧНИКА
# и добавяме резултата в един краен НИЗ

def translate_word(word):

    translated_word = ""
    for letter in word:
        translated_letter = character_map[letter]
        translated_word += translated_letter

    return translated_word
        

print(translate_word("intervenzia"))
print(translate_word("korekzia"))
print(translate_word("pregovori"))

# Да се напише функция която получава някакъв текст. 
# KJHGVSFJGVDJKFHGDJGFKJDGJFGDJKFGHDGFJHDGFKHDG
# Искаме да преброим колко пъти се среща всеки един от тези символи в думата

# Помислете как можем да го решим - като знаем че в един речник, можем да имаме
# само един УНИКАЛЕН ключ

def count_by_letter(word):
    
    letter_count_map = {}

    for letter in word:

        if letter_count_map.get(letter) == None:
            # Трябва да добавя ключ към речника
           letter_count_map[letter] = 1
        else:
           letter_count_map[letter] += 1   

    for key in letter_count_map:
        print(f"{key} -> {letter_count_map[key]}")

    
count_by_letter("KJHGVSFJGVDJKFHGDJGFKJDGJFGDJKFGHDGFJHDGFKHDG")


# print("A".isupper())
# print("a".isupper())

# Превод на главни букви
def translate_word_capital(word):

    translated_word = ""

    for index, letter in enumerate(word):

        if letter.isupper() and ((index + 1) % 2 == 0):
            translated_word += ("[" + character_map[letter.lower()] + "]")
        
        elif letter.isupper() and ((index + 1) % 2 != 0):
            translated_word += ("{" + character_map[letter.lower()] + "}")

        else:
            translated_word += character_map[letter]

    return translated_word


print(translate_word_capital("iNtervenzia"))
