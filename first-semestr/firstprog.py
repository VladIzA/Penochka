import math                                                     # Модуль, позволяющий работать с числами, с помощью различных математических функций
import numpy                                                    # Библиотека, позволяющая работать с массивами и матрицами
import matplotlib.pyplot as mpp                                 # Библиотека.модуль, позволяющий работать в интерфейсе MATLAB

                # Эта программа рисует график функции, заданной выражением ниже

if __name__=='__main__':                                        # Если быть честным, то я не совсем понимаю, что это, но возможно работает как точка входа в приложение
    arguments = numpy.r_[0:200:0.1]                             # Создание массива от 0 до 200 (не включительно) с шагом 0.1
    mpp.plot(                                                   # Функция plot строит график элементов массива arguments
        arguments,
        [math.sin(a) * math.sin(a/20.0) for a in arguments]     # Сама функция, отображенная на графике
    )
    mpp.show()                                                  # Вызывает сам интерфейс