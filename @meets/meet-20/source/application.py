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

    def get_info(self):

        user_status = "REGULAR"
        if self.is_vip:
            user_status = "VIP"

        return f"{self.name} {self.age} {user_status}"


visitor = Visitor(
    visitor_name="Mihail",
    visitor_age=10,
    is_visitor_vip=False)

# това не е готино
# visitor.name = "Dragan"

class Event:
    title: str
    visitor_collection: [Visitor] = []

    # Разширете конструктора, така че да приема допълнително поле
    # дали партито е за пълнолетни потребители. 
    # НЕ ПЪЛНОЛЕТНИТЕ НЕ МОГАТ да се регистрират.

    def __init__(self, event_title):
        self.title = event_title

    # Да направим функция, с название register_visitor
    # тази функция ще получава ОБЕКТ, от тип Visitor
    # ще добавя този обект в СПИСЪК - поле в класа Event

    def register_visitor(self, visitor_object: Visitor):
        self.visitor_collection.append(visitor_object)

    # Да направим функция list_all_register_visitors,
    # която да преминава през всички регистрирани
    # посетители и да извежда информация за тях
    # ИМЕ - ВЪЗРАСТ и дали са VIP
    def list_all_register_visitors(self):
        for element in self.visitor_collection:
            print(element.get_info())


new_event = Event("Black Party")
new_event.register_visitor(visitor)
new_event.register_visitor(visitor)
new_event.register_visitor(visitor)
new_event.register_visitor(visitor)
new_event.list_all_register_visitors()

# Системата трябва да може да създава СЪБИТИЯ, за всяко
# СЪБИТИЕ имаме посетител. Дадено съитие може да се
# разграничава по това дали е само за VIP посетители
# или само за пълнолетни посетители

# Ако се опитаме да регистрираме посетител, който не отговаря
# на критериите, трябва да получим съобщение за отказ

# Всяко събитие трябва да може да изведе списък с посетителите
# Които са регистрирани за него