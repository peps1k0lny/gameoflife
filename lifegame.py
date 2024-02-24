import tkinter as tk
from tkinter import messagebox as mb
import random


class Life(tk.Toplevel):
    def __init__(self, parent, xyc):
        super().__init__(parent)
        self.wdth = xyc[0]  # Присваиваем переменной длину
        self.hght = xyc[1]  # Присваиваем переменной ширину
        self.rnd = xyc[2]  # Присваиваем переменной количество живых клеток

        self.field = []  # Создаем массив с полем
        for i in range(self.hght + 2):  # Проходимся по ординате
            f = []  # Создаем подмассив
            for j in range(self.wdth + 2):  # Проходимся по абсциссе
                f.append(0)  # Добавляем 0 в подмассив
            self.field.append(f)  # Добавляем подмассив в массив

        for i in range(self.rnd):  # Проходимся по кол-ву случайных точек
            xrnd = random.randint(1, self.wdth)  # Создаем случайную абсциссу
            yrnd = random.randint(1, self.hght)  # Создаем случайную ординату
            self.field[yrnd][xrnd] = 1  # Обозначаем данную точку как живую

        self.geometry(f"{self.wdth*10+10}x{self.hght*10+40}")  # Обозначаем размеры окна
        self.title("Жизнь")  # Создаем заголовок окна

        self.frame = tk.Frame(self)  # Создаем окно с кнопками
        self.frame.pack(fill=tk.BOTH)  # Закрепляем его посередине и делаем отступ

        self.btn1 = tk.Button(self.frame, text='Начать', command=self.running)  # Создаем кнопку "Начать"
        self.btn1.pack(side='left')  # Привязываем ее к середине
        self.btn2 = tk.Button(self.frame, text='Стереть', command=self.clear)  # Создаем кнопку "Стереть"
        self.btn2.pack(side='left')  # Привязываем ее к середине

        self.canvas = tk.Canvas(self, bg="white", width=self.wdth * 10, height=self.hght * 10)  # Создаем холст для поля
        self.canvas.pack(anchor=tk.CENTER, expand=1)  # Закрепляем его в центре

        self.output()  # Выводим на него массив поля

        self.ps = True  # Обозначаем паузу игры


        self.canvas.bind('<Button-1>', self.draw)  # Вызываем функцию для рисования

    def animation(self):
        """
        Эта функция анимирует жизнь
        """
        if self.ps is False:  # Если игра продолжается,
            self.canvas.delete("all")  # то стираем поле игры
            self.output()  # Рисуем клетки
            self.checking()  # Проверяем кол-во соседей клетки
            self.after(100, self.animation)  # Зацикливаем анимацию

    def running(self):
        """
        Эта функция позволяет нам смотреть за жизнью
        """
        self.ps = False  # Обозначаем продолжение игры
        self.animation()  # Вызываем функцию для анимирования
        self.btn1.destroy()  # Уничтожаем кнопку "Продолжить" или "Начать"
        self.btn1 = tk.Button(self.frame, text='Пауза', command=self.pause)  # Создаем кнопку "Пауза"
        self.btn1.pack(side='left')  # Привязываем ее к середине
        self.btn2.destroy()  # Уничтожаем кнопку "Стереть"
        self.btn2 = tk.Button(self.frame, text='Стереть', state="disabled")  # Создаем пустую кнопку "Стереть"
        self.btn2.pack(side='left')  # Привязываем ее к середине

    def pause(self):
        """
        Эта функция позволяет нам самостоятельно заполнять поле или стереть его
        """
        self.ps = True  # Обозначаем паузу
        self.output()  # Выводим поле
        self.btn1.destroy()  # Уничтожаем кнопку "Пауза"
        self.btn1 = tk.Button(self.frame, text='Продолжить', command=self.running)  # Создаем кнопку "Продолжить"
        self.btn1.pack(side='left')  # Привязываем ее к середине
        self.btn2.destroy()  # Уничтожаем пустую кнопку "Стереть"
        self.btn2 = tk.Button(self.frame, text='Стереть', command=self.clear)  # Создаем кнопку "Стереть"
        self.btn2.pack(side='left')  # Привязываем ее к середине

    def clear(self):
        """
        Эта функция стирает двумерный массив клеток и заполняет пустыми клетками
        """
        self.field.clear()  # Стираем массив
        for i in range(self.hght + 2):  # Проходимся по ординате
            f = []  # Создаем подмассив
            for j in range(self.wdth + 2):  # Проходимся по абсциссе поля
                f.append(0)  # Добавляем 0 в подмассив
            self.field.append(f)  # Добавляем подмассив в массив
        self.output()  # Выводим поле

    def checking(self):
        """
        Эта функция проверяет каждую клетку на кол-во соседних живых клеток
        """
        checker = []  # Создаем массив кол-ва соседних живых клеток для каждой клетки
        for i in range(self.hght + 2):  # Проходимся по ординате
            f = []  # Создаем подмассив
            for j in range(self.wdth + 2):  # Проходимся по абсциссе
                f.append(0)  # Добавляем 0 в подмассив
            checker.append(f)  # Добавляем подмассив в массив

        for i in range(1, self.hght + 1):  # Проходимся по ординате поля
            for j in range(1, self.wdth + 1):  # Проходимся по абсциссе поля
                summ = 0  # Создаем параметр для подсчета
                if self.field[i - 1][j - 1] == 1:  # Если клетка сверху слева живая,
                    summ += 1  # то плюс 1
                if self.field[i - 1][j] == 1:  # Если клетка сверху живая,
                    summ += 1  # то плюс 1
                if self.field[i - 1][j + 1] == 1:  # Если клетка сверху справа живая,
                    summ += 1  # то плюс 1
                if self.field[i][j - 1] == 1:  # Если клетка слева живая,
                    summ += 1  # то плюс 1
                if self.field[i][j + 1] == 1:  # Если клетка справа живая,
                    summ += 1  # то плюс 1
                if self.field[i + 1][j - 1] == 1:  # Если клетка снизу слева живая,
                    summ += 1  # то плюс 1
                if self.field[i + 1][j] == 1:  # Если клетка снизу живая,
                    summ += 1  # то плюс 1
                if self.field[i + 1][j + 1] == 1:  # Если клетка снизу справа живая,
                    summ += 1  # то плюс 1
                checker[i][j] = summ  # Назначаем в массив сумму

        for i in range(1, self.hght + 1):  # Проходимся по ординате поля
            for j in range(1, self.wdth + 1):  # Проходимся по абсциссе поля
                if self.field[i][j] == 0:  # Если это мертвая клетка
                    if checker[i][j] == 3:  # Если у нее три живых соседа,
                        self.field[i][j] = 1  # то оживляем ее
                elif self.field[i][j] == 1:  # Если это живая клетка
                    if checker[i][j] < 2 or checker[i][j] > 3:  # Если у нее меньше двух или больше трех живых соседей,
                        self.field[i][j] = 0  # то она умирает

    def output(self):
        """
        Эта функция рисует все поле
        """
        for i in range(1, self.hght + 1):  # Проходимся по ординате
            for j in range(1, self.wdth + 1):  # Проходимся по абсциссе
                if self.field[i][j] == 1:  # Если в массиве данная клетка закрашена,
                    self.canvas.create_rectangle((j - 1) * 10, (i - 1) * 10, (j - 1) * 10 + 10, (i - 1) * 10 + 10,
                                            fill="black", outline="black")
                    # то рисуем живую клетку
                elif self.field[i][j] == 0:  # Если в массиве данная клетка пустая,
                    # то рисуем мертвую клетку
                    self.canvas.create_rectangle((j - 1) * 10, (i - 1) * 10, (j - 1) * 10 + 10, (i - 1) * 10 + 10,
                                            fill="red", outline="black")

    def draw(self, e):
        """
        Эта функция рисует точку во время паузы мышкой пользователя
        """
        if self.ps is True:  # Если сейчас пауза
            ii = (e.y + 10) // 10  # Считываем нажатие по абсциссе
            jj = (e.x + 10) // 10  # Считываем нажатие по ординате
            if self.field[ii][jj] == 1:  # Если данная клеточка закрашена,
                self.field[ii][jj] = 0  # то стираем
            elif self.field[ii][jj] == 0:  # Если клеточка пуста,
                self.field[ii][jj] = 1  # то закрашиваем
            self.output()  # И выводим поле


class Entrance(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x300")
        self.title("Введите размеры поля")
        frm_form = tk.Frame()
        frm_form.pack(anchor=tk.S, expand=1)

        lbl_x = tk.Label(master=frm_form, text="Длина:")
        self.ent_x = tk.Entry(master=frm_form, width=10)
        lbl_x.grid(row=0, column=0, sticky="e")
        self.ent_x.grid(row=0, column=1)

        lbl_y = tk.Label(master=frm_form, text="Ширина:")
        self.ent_y = tk.Entry(master=frm_form, width=10)
        lbl_y.grid(row=1, column=0, sticky="e")
        self.ent_y.grid(row=1, column=1)

        lbl_c = tk.Label(master=frm_form, text="Клетки:")
        self.ent_c = tk.Entry(master=frm_form, width=10)
        lbl_c.grid(row=2, column=0, sticky="e")
        self.ent_c.grid(row=2, column=1)

        frm_buttons = tk.Frame()
        frm_buttons.pack(anchor=tk.N, expand=1)

        btn_submit = tk.Button(master=frm_buttons, text="Начать!", command=self.inputting)
        btn_submit.pack()

    def inputting(self):
        xyc = [self.ent_x.get(), self.ent_y.get(), self.ent_c.get()]
        x = xyc[0]
        y = xyc[1]
        c = xyc[2]
        if x.isdigit() is False:
            mb.showerror("Ошибка", "Должно быть введено число длины")
        if y.isdigit() is False:
            mb.showerror("Ошибка", "Должно быть введено число широты")
        if c.isdigit() is False:
            mb.showerror("Ошибка", "Должно быть введено число количества клеток")
        if x.isdigit() is True and y.isdigit() is True and c.isdigit() is True:
            xyc = [int(x), int(y), int(c)]
            Life(self, xyc)


if __name__ == "__main__":
    game = Entrance()
    game.mainloop()
