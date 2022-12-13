
   


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



# 6. Создать класс Отель. Класс хранит цены на разные комнаты.
#    Класс хранит количество забронированных комнат разного типа.
#    Выдавать количество свободных комнат. Создать метод "забронировать"
class Hotel:

    def __init__(self):
        self.__rooms = {
                        'econom':   [], 
                        'standart': [], 
                        'VIP':      []}
    
    @property
    def rooms(self):
        return self.__rooms

    @rooms.setter
    def rooms(self, some_tat):
        self.__amount = some_tat
        for i in range(some_tat):
            room = input('Price, Status = ').split(', ') # 1200, занята
            room = [i + 1, int(room[0]), False if room[1] == 'Booked' else True]
            if room[1] > 0 and room[1] < 50:
                self.__rooms['econom'].append(room)
            elif room[1] >= 50 and room[1] < 100:
                self.__rooms['standart'].append(room)
            elif room[1] >= 100:
                self.__rooms['VIP'].append(room)
            else:
                print('Invalid price!')
            
    def rent(self, number):
        if number <= self.__amount:
            for kat in self.__rooms.values():
                for room in kat:
                    if room[0] == number and room[2] == True:
                        room[2] = False 
                        print("The room was FREE AND Now Booking")
                    else:
                        print("The room is occupied")
                
room = Hotel()
room.rooms = 3
print(room.rooms)
room.rent(1)
print(room.rent)
