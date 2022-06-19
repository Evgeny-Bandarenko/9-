# Создать класс Dog.
# Класс имеет четыре
# атрибута: height, weight, name, age. Класс
# имеет три метода: jump, run, bark. Каждый
# метод выводит сообщение на экран.
# Создать объект класса Dog, вызвать все
# методы
# объекта и вывести на экран все его
# атрибуты.



# class Dog:
#
#     def __init__(self, name, age, height, weight):
#         self.name = name
#         self.age = age
#         self.height = height
#         self.weight = weight
#
#
#     def jump(self, m):
#         return f"прыгнул {self.name}, {m} метра "
#
#
#     def run(self, km):
#         return f"пробежал {self.name}, {km} километров"
#
#
#     def bark(self, wof_wof):
#         return f"{self.name}, подает голос {wof_wof}"
#
# Zheki = Dog("Zheki", 3, 1, 60 )
# print(Zheki.__dict__)
# print(Zheki.jump(2))
# print(Zheki.run(5))
# print(Zheki.bark("wof_wof"))


# Добавить в класс Dog метод change_name.
# Метод
# принимает на вход новое имя и меняет
# атрибут имени у
# объекта. Создать один объект класса.
# Вывести имя.
# Вызвать метод change_name. Вывести имя


class Dog:


    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight


    def jump(self, m):
        return f"прыгнул {self.name}, {m} метра "


    def run(self, km):
        return f"пробежал {self.name}, {km} километров"


    def bark(self, wof_wof):
        return f"{self.name}, подает голос {wof_wof}"


    def change_name(self, name):
        return f"{self.name},изменил кличку на {name.age = "Zan"}"

Zheki = Dog("Zheki", 3, 1, 60 )
print(Zheki.__dict__)
print(Zheki.jump(2))
print(Zheki.run(5))
print(Zheki.bark("wof_wof"))
print(Zheki.change_name)
print(Zheki.__dict__)