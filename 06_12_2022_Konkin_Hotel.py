# 6. Создать класс Отель. Класс хранит цены на разные комнаты.
#    Класс хранит количество забронированных комнат разного типа.
#    Выдавать количество свободных комнат. Создать метод "забронировать"
class Hotel:

    def __init__(self):
        self.__rooms = {
                        'econom':   [], 
                        'standart': [], 
                        'VIP':      []}
        self.__amount = None
    
    @property
    def create_hotel(self):
        return self.__rooms
    @create_hotel.setter
    def create_hotel(self, some_tat):
        self.__amount = some_tat
        for i in range(some_tat):
            room = input('Price, Status = ').split(', ') 
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
                    number_room = room[0]
                    if room[0] == number and room[2] == True:
                        room[2] = False
                        print(f'The room № {number_room} was FREE AND Now Booking')
                    elif room[0] != number and room[2] == True:
                        print(f'The room № {number_room} FREE ')
                    else:
                        print(f'The room № {number_room} Booked ')
                       
        else:
            print('Incorrect number room')
                
room = Hotel()
room.create_hotel = 6
print(room.create_hotel)
room.rent(1)
room.rent(3)
print(room.rent)

