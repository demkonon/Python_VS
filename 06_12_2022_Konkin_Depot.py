# 5. Создать класс, хранящий количества товаров на складе.
#    Если товара нет, класс должен возвращать 0 (не вываливаться)
class Depot:

    def __init__(self, some_total):
        self.__value = some_total
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, some_tat):
        if type(some_tat) in (int, float):
            self.__value = some_tat
    
    def __str__(self):
        if self.__value <= 0:
            return '0'
        else:
            return '1'

goods = Depot(0)
goods.value = 10
print(goods)

