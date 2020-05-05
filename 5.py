from tkinter import *


class StringFormatter(object):
    def __init__(self, text):
        self.__text = str(text)
        self.__list = list()

    def func1(self, number):  # – удаление всех слов из строки, длина которых меньше n букв
        self.__list = list(self.__text.split())
        self.__list = list(filter(lambda x: len(x) >= number, self.__list))
        self.__text = ' '.join(self.__list)
        # return self.__text

    def func2(self):  # – замена всех цифр в строке на знак «*»;
        self.__list = list(self.__text)
        for i in range(len(self.__list)):
            if self.__list[i].isdigit():
                self.__list[i] = "*"
            else:
                continue
        self.__text = ''.join(self.__list)
        # return self.__text

    def func3(self):  # – вставка по одному пробелу между всеми символами в строке;
        self.__list = list(self.__text)
        self.__text = " ".join(self.__list)
        # return self.__text

    def func4(self):  # – сортировка слов по размеру;
        self.__list = sorted(list(self.__text.split()), key=len)
        self.__text = ' '.join(self.__list)
        # return self.__text

    def func5(self):  # – сортировка слов в лексикографическом порядке.
        self.__list = sorted(list(self.__text.split()))
        self.__text = ' '.join(self.__list)

    # return self.__text
    @property
    def text(self):
        return self.__text


class MyWindow():
    def click_button(self):
        if len(str(self.message_entry1.get())) is not 0 or str(self.message_entry1.get()).isspace() is FALSE:
            object1 = StringFormatter(self.message_entry1.get())
            if self.lang1.get() == 1:
                object1.func1(int(self.spin.get()))
            if self.lang2.get() == 1:
                object1.func2()
            if self.lang3.get() == 1:
                object1.func3()
            if self.lang4.get() == 1 and self.lang5.get() == 1:
                object1.func4()
            if self.lang4.get() == 1 and self.lang5.get() == 2:
                object1.func5()
            self.string.set(str(object1.text))
            self.message_entry2.config(textvariable=self.string)
            del object1
        else:
            self.string.set("Ошибка ввода текста! Повторите попытку")
            self.message_entry2.config(textvariable=self.string)

    def activate_and_disactivare_radiobuttons(self):
        if self.lang4.get() == 0:
            self.lang5.set(0)
            self.radiobutton1.config(state=DISABLED, variable=self.lang5)
            self.radiobutton2.config(state=DISABLED, variable=self.lang5)
        if self.lang4.get() == 1:
            self.radiobutton1.config(state=ACTIVE)
            self.radiobutton2.config(state=ACTIVE)

    def set_start_value_of_spin(self):
        if self.lang1.get() == 0:
            self.var.set(5)
            self.spin.config(textvariable=self.var, state=DISABLED)
        else:
            self.spin.config(state=NORMAL)

    def __init__(self):
        self.__window = Tk()
        self.__window["bg"] = "White"
        self.__window.title("Обработка строк")
        self.__window.geometry('520x520')
        self.init_ui()

    def init_ui(self):
        # надпись "Строка"
        self.label1 = Label(text="Строка:", fg="black", bg="white")
        self.label1.place(x=10, y=25)
        # поле для ввода обрабатываемой строки
        self.message_entry1 = Entry(bg="red")
        self.message_entry1.place(x=75, y=25, width=400)

        # первый checkbox
        self.lang1 = IntVar()
        self.checkbutton1 = Checkbutton(text="Удалить слова размером меньше", variable=self.lang1,
                                        onvalue=1, offvalue=0, command=self.set_start_value_of_spin)
        self.checkbutton1.place(x=50, y=100)
        # spinbox
        self.var = IntVar()
        self.var.set(5)
        self.spin = Spinbox(self.__window, from_=0, to=100000, width=10, textvariable=self.var, state=DISABLED)
        self.spin.place(x=280, y=102)
        # надпись букв
        self.label3 = Label(text="букв", fg="black", bg="white")
        self.label3.place(x=360, y=100)
        # второй checkbox
        self.lang2 = IntVar()
        self.checkbutton2 = Checkbutton(text="Заменить все цифры на *", variable=self.lang2,
                                        onvalue=1, offvalue=0)
        self.checkbutton2.place(x=50, y=150)
        # третий checkbox
        self.lang3 = IntVar()
        self.checkbutton3 = Checkbutton(text="Вставить по пробелу между символами", variable=self.lang3,
                                        onvalue=1, offvalue=0)
        self.checkbutton3.place(x=50, y=200)
        # четвертый checkbox
        self.lang4 = IntVar()
        self.checkbutton4 = Checkbutton(text="Сортировка слов в строке", variable=self.lang4,
                                        onvalue=1, offvalue=0, command=self.activate_and_disactivare_radiobuttons)
        self.checkbutton4.place(x=50, y=250)
        # radiobutton 1
        self.lang5 = IntVar()
        self.radiobutton1 = Radiobutton(text="По размеру", value=1, variable=self.lang5, state=DISABLED)
        self.radiobutton1.place(x=75, y=300)
        # radiobutton 2
        self.radiobutton2 = Radiobutton(text="Лексикографически", value=2, variable=self.lang5, state=DISABLED)
        self.radiobutton2.place(x=75, y=350)
        # кнопка
        self.btn = Button(self.__window,
                          text="Форматирование текста",  # надпись на кнопке
                          width=30, height=2,  # ширина и высота
                          bg="Grey", fg="black",  # цвет фона и надписи
                          command=self.click_button)
        self.btn.place(x=150, y=400)
        # надпись "Результат"
        self.label2 = Label(text="Результат:", fg="black", bg="white")
        self.label2.place(x=10, y=475)
        #  поле для вывода обработанной строки
        self.string = StringVar()
        self.message_entry2 = Entry(textvariable=self.string, bg="green")
        self.message_entry2.place(x=75, y=475, width=400)

    def show(self):
        self.__window.mainloop()


if __name__ == "__main__":
    window = MyWindow()
    window.show()
