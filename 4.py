class StringFormatter(object):
    def __init__(self, text):
        self.__text = str(text)
        self.__list  = list()
        self.__result = None
    def func1(self, number): #– удаление всех слов из строки, длина которых меньше n букв
        print("1) удаление всех слов из строки, длина которых меньше {0} букв".format(number))
        self.__list = list(self.__text.split())
        self.__list = list(filter(lambda x: len(x) >= number, self.__list))
        self.__result =' '.join(self.__list)
        return self.__result
    def func2(self): #– замена всех цифр в строке на знак «*»;
        print("2) замена всех цифр в строке на знак «*»")
        self.__list = list(self.__text)
        for i in range(len(self.__list)):
            if self.__list[i].isdigit():
                self.__list[i] = "*"
            else:
               continue
        self.__result = ''.join(self.__list)
        return self.__result
    def func3(self): #– вставка по одному пробелу между всеми символами в строке;
        print("3) вставка по одному пробелу между всеми символами в строке")
        self.__list = list(self.__text)
        self.__result=" ".join(self.__list)
        return self.__result
    def func4(self): #– сортировка слов по размеру;
        print("4) сортировка слов по размеру")
        self.__list = sorted(list(self.__text.split()), key=len)
        self.__result = ' '.join(self.__list)
        return self.__result
    def func5(self): # – сортировка слов в лексикографическом порядке.
        print("5) сортировка слов в лексикографическом порядке")
        self.__list = sorted(list(self.__text.split()))
        self.__result = ' '.join(self.__list)
        return self.__result

example = StringFormatter(input("Введите текст: "))
print(example.func1(3))
print(example.func2())
print(example.func3())
print(example.func4())
print(example.func5())
