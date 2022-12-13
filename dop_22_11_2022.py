# Напишите программу в которой есть главный класс с текстовым полем.

# В главное классе должен быть метод для присваивания значения полю: без аргументов и с одним текстовым аргументом. (описать принцип инкапсуляции)
# obj.setValue(12) // Пример с аргументом
# obj.x = '' //Пример без аргумента

# Объект главного класса создаётся передачей одного текстового аргумента конструктору. На основе главного класса создается класса потомок. (описать принцип наследования)


# В классе-потомке нужно добавить числовое поле. У конструктора класса-потомка два аргумента.

class Parent:

    def __init__(self, n):
        self.__text_field = n
        
    @property
    def text_field(self):
        return self.__text_field
    
    @text_field.setter
    def text_field(self, value):
        self.__text_field = value
        
    @text_field.deleter
    def text_field(self):
        del self.__text_field

    # def get__read(self):
    #     return self.__text_field
    
    # def set__write(self, texter):
    #     self.__text_field = texter


# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.number_field = 0
    
    
# var = Child()
# print(var.text_field)
# print(var.number_field)

n = 'Empty'
peremOne = Parent(n)

print(peremOne.text_field)
peremOne.text_field = 'Field'
print(peremOne.text_field)

del peremOne.text_field

try:
    print(peremOne.text_field)
except:
    print('Удалено')
finally:
    print('Try block was ended')

# print(peremOne.get__read())

# peremOne.set__write('Full')
# print(peremOne.get__read())


class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
    
p1 = Point(1, 2)
p2 = Point(2, 3)

print(f'Point 1: {p1}')
print(f'Point 1: {p2}')
print(f'Sum of points: {p1 + p2}')