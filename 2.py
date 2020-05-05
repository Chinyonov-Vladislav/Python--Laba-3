import random
from abc import ABCMeta, abstractmethod, abstractproperty
import sys
class Taggable():
    __metaclass__ = ABCMeta
    @abstractmethod
    def tag(self):
        pass
######################################################
class Book(Taggable):
    code_of_book = 1
    def __init__(self, author,name):
        try:
            #if str(name).isspace() or len(str(name))==0 or str(author).isspace() or len(str(author))==0:
            if len(str(name)) == 0 or len(str(author)) == 0:
               raise ValueError
            else:
                self.__name = name
                self.__author = author
                self.__code = Book.code_of_book
                Book.code_of_book+=1
        except ValueError:
            print("Ошибка создания объекта книги №{0}! В конструктор передана пустая строка!".format(str(Book.code)))
            print("Завершение работы скрипта!")
            sys.exit()
    def __str__(self):
            return "[{0}] {1} '{2}'".format(self.code,self.author,self.author)
    def tag(self):
            return [word for word in str(self.__name).split() if str(word)[0].isupper()]
    @property
    def name(self):
        return  self.__name
    @property
    def author(self):
        return self.__author
    @property
    def code(self):
        return self.__code
###########################################
class Library(Book):
    def __init__(self, number, adress):
        self.__number = number
        self.__adress = adress
        self.__books = list()
    def __iadd__(self, book):
            self.__books.append(book)
            return self
    def __iter__(self):
        return iter(self.__books)
    
lib = Library(1, "51 Some str., NY’")
lib += Book("Leo Tolstoi", "War and Peace")
lib += Book("Charles Dickens", "David Copperfield")
for book in lib:
#вывод в виде: [1] L.Tolstoi ‘War and Peace’
    print(book)
# вывод в виде: [‘War’, ‘Peace’]
    print(book.tag())