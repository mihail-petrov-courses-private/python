from classroom import Classroom


class School:
    _name: str
    _classroom_collection: list[Classroom]

    def __init__(self, name: str):
        self._name = name

    def add_classroom(self, classroom_object: Classroom):
        self._classroom_collection.append(classroom_object)

    def liss_classroom(self):
        for classroom in self._classroom_collection:
            print(classroom.get_name())
