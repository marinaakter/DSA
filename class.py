class Person:
    def __init__(self,person_name,date_of_birth,ht):
        self.__name = person_name
        self.__date_of_birth = date_of_birth
        self.__height = ht
    
    def get_name(self):
        return self.__name
    
    def __has__any__number(self, string):
        return "0" in string

    def set_name(self, new_name):
        if (self.__has__any__number(new_name)):
            print("Sorry, person name can't contain any number")
            return


    def get_summary(self):
        return f"Name:{self.__name},DOB:{self.__date_of_birth},Height:{self.__height}"



a_person = Person("Marina","2003","5'4")
print(a_person.get_summary())
b_person = Person("John","2000","5'10")
print(b_person.get_summary())
a_person.set_name("Marina Akter")
print(a_person.get_summary())

print(a_person.date_of_birth)
a_person.set_name("0Marina Akter")