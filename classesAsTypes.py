class Person:
    def __init__(self, name:str):
        self.name = name

def get_name(one_person: Person):
    return one_person.name.title()

me = Person("riwa")
print(get_name(me))
