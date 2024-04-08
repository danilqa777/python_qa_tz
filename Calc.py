class Calc:
    # Конструктор класса
    def __init__(self):
        self.result = 0

    def clear(self):
        self.result = 0
        return self

    # Метод для сложения двух чисел
    def add(self, x, y):
        self.result = x + y
        return self

    # Метод для вычитания двух чисел
    def subtract(self, x, y):
        self.result = x - y
        return self

    # Метод для умножения двух чисел
    def multiply(self, x, y):
        self.result = x * y
        return self

    # Метод для деления двух чисел
    def divide(self, x, y):
        if y == 0:
            raise ZeroDivisionError("y = 0, division by zero")
        self.result = x / y
        return self

    # Метод для прибавления к числу в памяти
    def add_mem(self, x):
        self.result += x
        return self

    # Метод для вычитания из числа в памяти
    def subtract_mem(self, x):
        self.result -= x
        return self

    # Метод для умножения на число в памяти
    def multiply_mem(self, x):
        self.result *= x
        return self

    # Метод для деления числа из памяти
    def divide_mem(self, x):
        if x == 0:
            raise ZeroDivisionError("x = 0, division by zero")
        self.result /= x
        return self

    # Метод для получения результата вычислений
    def get_result(self):
        return self.result
