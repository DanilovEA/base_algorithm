"""
Created on Sat May 4 02:11:39 2020

@author: Danilov Evgeniy
"""
class Factorial(object):
    def __init__(self, number: int):
        self._number = number

    # Метод для нахождения факториала
    def factorial_finder(self, _number: int):
        if _number == 1:
            return 1
        return _number * self.factorial_finder(_number - 1)

    # Переопределяем метод для печати print()
    def __repr__(self):
        res = str("Hello, your factorial is {}".format(self.factorial_finder(self._number)))
        return res

if __name__ == "__main__":
    # Ждём от пользователя число, факториал которого будем считать
    number = int(input("Please, enter the number: "))
    
    # Создаем объект класса факториал
    a = Factorial(number)
    print(a)