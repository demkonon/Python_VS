# 1. Написать класс, хранящий информацию о длине лап разных животных,
#    и его название. Класс ничего не должен делать (даже инит!!!)
   
#    class Animal
class Animal:
    # без инита
    cat = 9
    dog = 18
    supermouse = 27

# 2. Добавить в класс метод, позволяющий указывать название животного
#    и длину его лап.

    def __init__(self, an, len):
        self.__some_animal = an
        self.__some_length = len

    @property
    def some_animal(self):
        return self.__some_animal
    @some_animal.setter
    def some_animal(self, value):
        self.__some_animal = value
        
    @property
    def some_lenght(self):
        return  self.__some_length
    @some_lenght.setter
    def some_lenght(self, value1):
        self.__some_length = value1

# 3. Добавить способ сравнения классов на больше и меньше.
#    Продемонстрировать работу
    def __lt__(self, other):
        if self.some_lenght < other.some_lenght:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.some_lenght == other.some_lenght:
            return 'Equal'

    # 4. Добавить способ печати животного на экран
#    "Кошка, лапы 10 см"
    def __str__(self):
        return f"{self.__some_animal} leg lenght {self.__some_length}"

print(Animal.cat)
print(Animal.dog)
cat = Animal('Cat', 20)
dog = Animal('Dog', 45)
supermouse = Animal('Supermouse', 45)


print(cat)
print(dog)

print(cat < dog)
print(dog < cat)
print(dog == supermouse)