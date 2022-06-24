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


# class Dog:
#
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
#
#
#     def change_name(self, new_name):
#          self.name = new_name
#
# Zheki = Dog("Zheki", 3, 1, 60 )
# print(Zheki.__dict__)
# print(Zheki.jump(2))
# print(Zheki.run(5))
# print(Zheki.bark("wof_wof"))
# Zheki.name = "Zan"
# print(Zheki.__dict__)


# Создать три класса: Dog, Cat, Parrot.
# Атрибуты каждого класса: name, age,
# master.
# Каждый класс содержит
# конструктор и методы: run, jump,
# birthday(увеличивает age на 1), sleep.
# Класс Parrot имеет дополнительный
# метод fly, Cat - meow, Dog - bark.


# class Dog:
# 
# 
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
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
#     def birthday(self, age):
#         return f"У {self.name} день рождения, ему {age + 1} года"
# 
# 
#     def slip(self, hour):
#         return f"{self.name} проспал {hour} часа"
# 
#     def bark(self, wof_wof):
#         return f"{self.name}, подает голос {wof_wof}"
# 
# 
# 
# 
# Zheki = Dog("Zheki", 3, "Vasya" )
# print(Zheki.__dict__)
# print(Zheki.jump(2))
# print(Zheki.run(5))
# print(Zheki.slip(8))
# print(Zheki.bark("wof_wof"))
# print(Zheki.birthday(3))




# class Cat:
#
#
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#
#
#     def jump(self, m):
#         return f"прыгнула {self.name}, {m} метра "
#
#
#     def run(self, km):
#         return f"пробежала {self.name}, {km} километров"
#
#
#     def birthday(self, age):
#         return f"У {self.name} день рождения, ей {age + 1} года"
#
#
#     def slip(self, hour):
#         return f"{self.name} проспал {hour} часов"
#
#     def bark(self, meow_meow):
#         return f"{self.name}, мяучит {meow_meow}"
#
#
#
#
# Aliwi = Cat("Aliwi", 1, "lysi" )
# print(Aliwi.__dict__)
# print(Aliwi.jump(1))
# print(Aliwi.run(1))
# print(Aliwi.slip(12))
# print(Aliwi.bark("meow_meow"))
# print(Aliwi.birthday(1))
#
#
# class Parrot:
#
#
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#
#
#     def jump(self, sm):
#         return f"прыгнул {self.name}, {sm} сантиметров "
#
#
#     def run(self, m):
#         return f"пробежала {self.name}, {m} метров"
#
#
#     def birthday(self, age):
#         return f"У {self.name} день рождения, ему {age + 1} года"
#
#
#     def slip(self, hour):
#         return f"{self.name} проспал {hour} часов"
#
#     def bark(self, fly):
#         return f"{self.name}, пролетел {fly} метров"
#
#
#
#
# Kecha = Parrot("Kecha", 1, "lysili" )
# print(Kecha.__dict__)
# print(Kecha.jump(20))
# print(Kecha.run(5))
# print(Kecha.slip(3))
# print(Kecha.bark(20))
# print(Kecha.birthday(1))



# class Pet:
# 
#     def init(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
# 
#     def jump(self, m):
#         return f" прыжок {self.name} {m} метров."
# 
#     def run(self, km):
#         return f" {self.name} пробежал {km} км."
# 
#     def birthday(self, age):
#         return f"{self.name} birthday {age + 1}"
# 
#     def slip(self, hour):
#         return f"{self.name} проспал {hour} часов."
# 
# 
# class Dog(Pet):
# 
# 
#     def __init__(self, name, age, master):
#         super().init(name, age, master)
# 
# 
#     def bark(self, wof_wof):
#         return f" {self.name} подаёт голос {wof_wof}"
# 
# 
# class Cat(Pet):
# 
# 
#     def __init__(self, name, age, master):
#         super().init(name, age, master)
# 
# 
#     def bark(self, meow_meow):
#         return f" {self.name} подаёт голос {meow_meow}"
# 
# 
# class Parrot(Pet):
# 
# 
#     def __init__(self, name, age, master):
#         super().init(name, age, master)
# 
# 
#     def bark(self, km, m):
#         return f" {self.name} пролетел {km} км на высоте {m} метров."
# 
# Zheki = Dog("Zheki", 3, "Vasya" )
# print(Zheki.__dict__)
# print(Zheki.jump(2))
# print(Zheki.run(5))
# print(Zheki.slip(8))
# print(Zheki.bark("wof_wof"))
# print(Zheki.birthday(3))
# Aliwi = Cat("Aliwi", 1, "lysi" )
# print(Aliwi.__dict__)
# print(Aliwi.jump(1))
# print(Aliwi.run(1))
# print(Aliwi.slip(12))
# print(Aliwi.bark("meow_meow"))
# print(Aliwi.birthday(1))
# Kecha = Parrot("Kecha", 1, "lysili" )
# print(Kecha.__dict__)
# print(Kecha.jump(20))
# print(Kecha.run(5))
# print(Kecha.slip(3))
# print(Kecha.bark(20,3))
# print(Kecha.birthday(1))