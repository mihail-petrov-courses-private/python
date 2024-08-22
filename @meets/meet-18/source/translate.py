CHARACTER_MAP = {
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

def translate(char_sequance):
    
    translation = ""
    for char_position, char_id in char_sequance:

        if is_char_upper(char_position, char_id):
            translation += translate_upper(char_position, char_id)

        elif is_char_special(char_position, char_id):
            translation += translate_special(char_position, char_id)

        else:
            translation += translate_letter(char_position, char_id)

    return translation

def is_char_special(char_position, char_id):
    return  (char_id == " " or
            char_id == "?"  or
            char_id == ".")

def is_char_upper(char_position, char_id):
    return char_id.isupper()

def translate_special(char_position, char_id):
    if char_id == " " and is_position_even(char_position):
        return "***"
    
    if char_id == " " and is_position_odd(char_position):
        return "___"
    
    if char_id == ".":
        return "|...|"
    
    if char_id == "?":
        return "$$$"

def translate_letter(char_position, char_id):
    return CHARACTER_MAP.get(char_id)

def translate_upper(char_position, char_id):

    if is_position_odd(char_position):
        return "[" + translate_letter(char_id.lower()) + "]"
    
    if is_position_even(char_position):
        return "{" + translate_letter(char_id.lower()) + "}"


def is_position_odd(char_position):
    return ((char_position + 1) % 2 != 0)

def is_position_even(char_position):
    return not is_position_odd(char_position)
