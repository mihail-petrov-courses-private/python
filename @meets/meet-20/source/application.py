# Да се напише програма, за регистрация на посетители
# на събития в даден нощен клуб

# Всеки посетител има следната информация за себе си:
# - години
# - име
# - дали е VIP посетител
class Visitor:

    age: int
    name: str
    is_vip: bool

    def __init__(self, visitor_age: int, visitor_name: str, is_visitor_vip: bool):
        self.age = visitor_age
        self.name = visitor_name
        self.is_vip = is_visitor_vip

visitor = Visitor(
    visitor_name="Mihail",
    visitor_age=10,
    is_visitor_vip=False)

# това не е готино
# visitor.name = "Dragan"


class Event:
    title: str

    def __init__(self, event_title):
        self.title = event_title

    # Да направим функция, с название register_visitor
    # тази функция ще получава ОБЕКТ, от тип Visitor
    # ще добавя този обект в СПИСЪК - поле в класа Event


# Системата трябва да може да създава СЪБИТИЯ, за всяко
# СЪБИТИЕ имаме посетител. Дадено съитие може да се
# разграничава по това дали е само за VIP посетители
# или само за пълнолетни посетители

# Ако се опитаме да регистрираме посетител, който не отговаря
# на критериите, трябва да получим съобщение за отказ

# Всяко събитие трябва да може да изведе списък с посетителите
# Които са регистрирани за него