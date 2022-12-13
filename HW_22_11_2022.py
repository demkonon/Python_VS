import tkinter as tk
from datetime import datetime


class Doings():

    def __init__(self):
        self.win = tk.Tk()
        self.txt_name_b = None
        self.txt_theday = None
        self.ch_ch1_value = None
        self.number_bis = 0
        self.text_mass = []
        self.lbl_changeable_arr = []
        self.lb1_arr = []

    def datafor(self):
        d = datetime.today()
        day = d.day
        month = d.month
        year = d.year
        tk.Label(self.win,
                 text="DAY: %s" % (str(day)),
                 font=("Arial Bold", 27),
                 bg='lightgrey') \
            .grid(column=0, row=1)

        tk.Label(self.win,
                 text="MONTH: %s" % (str(month)),
                 font=("Arial Bold", 12),
                 bg='lightgrey') \
            .grid(column=1, row=1)
        tk.Label(self.win,
                 text="Year: %s" % (str(year)),
                 font=("Arial Bold", 8),
                 bg='lightgrey') \
            .grid(column=0, row=0, stick='w')


    def next_b(self):
        currentData = datetime.now().date()
        if self.ch_ch1_value.get() == 1:
            text = 'DOne'
        else:
            text = 'note doNE'
        if self.txt_name_b.get():
            t0 = self.txt_name_b.get()
            self.number_bis += 1
        lbl_changeable = \
            tk.Label(self.win,
                     text="%i. %s status: %s Date <<<<<%s>>>>>" % (self.number_bis, t0, text, str(currentData)),
                     font=("Arial Bold", 10),
                     width=80,
                     pady=6, padx=8,
                     anchor='w',
                     bg='lightgrey')
        text_f = " %s |status: %s| Date <<<<<%s>>>>>" % (t0, text, str(currentData))
        self.text_mass.append(text_f)
        row_ch = 3 + self.number_bis
        lbl_changeable.grid(column=2, row=row_ch)
        self.lbl_changeable_arr.append(lbl_changeable)

        self.txt_name_b.delete(0, tk.END)

    def text_delete(self):
        self.ch_ch1_value.set(False)
        self.number_bis = 0
        self.txt_name_b.delete(0, tk.END)
        for i in self.lbl_changeable_arr:
            i.destroy()
        for i in self.lb1_arr:
            i.destroy()

    def cases_save(self):
        cur = datetime.today()
        d = str(cur.day)
        m = str(cur.month)
        y = str(cur.year)
        d1 = open(f'{d}_{m}_{y}.txt', 'w')
        for i in self.text_mass:
            d1.write(str(i) + '\n')
        d1.close()
        self.txt_name_b.delete(0, tk.END)
        self.text_delete()

    def open_day(self):
        td = self.txt_theday.get()
        row_i = 0
        if td.find('txt') == -1 and ('/' in td):
            t = td.split('/')
            do = open(f'{t[0]}_{t[1]}_{t[2]}.txt', 'r')
            for line in do:
                lb1 = tk.Label(self.win, text=line, bg='lightgrey').grid(column=2, row=row_i + 4)
                row_i += 1
                self.lb1_arr.append(lb1)


    def interface(self):
        self.win.title('ready-made CASES')
        wi = 850
        he = 450
        self.win.geometry(f'{wi}x{he}+850+300')
        self.win.minsize(800, 450)
        self.win.config(bg='lightgrey')

        tk.Label(self.win,
                 text="check",
                 font=("Arial Bold", 13),
                 bg='lightgrey') \
            .grid(column=1, row=2)

        self.ch_ch1_value = tk.BooleanVar()
        self.ch_ch1_value.set(0)
        tk.Checkbutton(
            bg='lightgrey',
            variable=self.ch_ch1_value,
            onvalue=1,
            offvalue=0, ) \
            .grid(column=1, row=3)

        tk.Label(self.win,
                 text="cases on",
                 font=("Arial Bold", 13),
                 bg='lightgrey') \
            .grid(column=2, row=2)

        self.txt_name_b = tk.Entry(self.win, width=50, bg='lightgrey')
        self.txt_name_b.grid(column=2, row=3)
        self.txt_theday = tk.Entry(self.win, width=10, bg='lightgrey')
        self.txt_theday.grid(column=0, row=4)

        tk.Label(self.win, bg='lightgrey').grid(column=3, row=3)
        tk.Button(self.win,
                  text='Enter',
                  width=15,
                  font=("Arial Bold", 12),
                  command=self.next_b,
                  bg='lightgrey') \
            .grid(column=4, row=1)
        tk.Button(self.win,
                  text='CLEAR',
                  width=15,
                  font=("Arial Bold", 12),
                  command=self.text_delete,
                  bg='lightgrey') \
            .grid(column=4, row=2)
        tk.Button(self.win,
                  text='save cases to file',
                  width=15,
                  font=("Arial Bold", 12),
                  command=self.cases_save,
                  bg='lightgrey') \
            .grid(column=4, row=3)
        tk.Button(self.win,
                  text='Open The day for read',
                  width=20,
                  font=("Arial Bold", 12),
                  command=self.open_day,
                  bg='lightgrey') \
            .grid(column=0, row=3)
        self.win.grid_columnconfigure(4, minsize=40)
        self.datafor()
        self.win.mainloop()

#   1. Создать класс машина и от него унаследовать класс самолет
#    класс машина должен содержать метод "ехать", которому передается скорость
#    класс самолет должен выдавать надпись "подъем" при скорости больше 300 км/ч
#    скорость хранить в специальном поле
#    это поле создается в ините и не принимает параметров, начальная скорость 0
class Machine():

    def __init__(self):
        self.speed = 0
    def drive(self, speed):
        self.speed = speed

class Airplan(Machine):

    def drive(self, speed):
        super(Airplan, self).drive(speed)
        if self.speed > 300:
            print('fly')
        else:
            print('drive')

# 2. Создать класс книга и класс учебник.
#    Класс книга должен содержать список страниц.
#    Класс учебник должен содержать вдобавок словарь вопросов.
#    Класс книга должна по номеру страницы выводить страницу
#    Класс учебник должен иметь метод задавания вопроса, ответ на который содержится
#    на странице.

class Book():
    def __init__(self):
        self.pages = ['context...', 'foreword...', 'table of contents...', 'pictures...']
    def see_page(self, index):
        return self.pages[index]


class Classbook(Book):
    def __init__(self):
        self.structure = {
            # 0: 'context?',
            # 1: 'foreword?',
            # 2: 'table of contents?',
            # 3: 'pictures?',
            'context?': 1,
            'foreword?': 2,
            'table of contents?': 3,
            'pictures?': 4
        }
        super().__init__()
    def make_question(self, question):
        for dict_quest in self.structure.items():
            if question == dict_quest[0]:
                print(f'Answer: {super().see_page(dict_quest[1] - 1)}')
            
        




def works():
    print("""   
             Press <1>,  If you want open your Doings
             Press <2> , If you want open task about speed
             Press <3> , if you want open task about book""")
    choice = input("Your choice-----")
    if choice == '1':
        c = Doings()
        c.interface()
    elif choice == '2':
        d = Airplan()
        x = int(input('enter some speed-----'))
        d.drive(x)
    elif choice == '3':
        c = Classbook()
        q = input('Enter your question:')
        c.make_question(q)


if __name__ == '__main__':
    works()



