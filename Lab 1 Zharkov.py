from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Абстрактный класс, представляющий животное.

    Атрибуты:
    - name (str): Имя животного.
    - age (int): Возраст животного в годах.
    """

    def __init__(self, name: str, age: int):
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным.")
        self.name = name
        self.age = age

    @abstractmethod
    def make_sound(self) -> str:
        """
        Метод, который возвращает звук, издаваемый животным.

        :return: Звук животного.
        :rtype: str
        :doctest:
        >>> dog = Dog("Buddy", 3)
        >>> dog.make_sound()
        'Woof!'
        """
        ...

class Dog(Animal):
    def make_sound(self) -> str:
        return "Woof!"

class Vehicle(ABC):
    """
    Абстрактный класс, представляющий транспортное средство.

    Атрибуты:
    - model (str): Модель транспортного средства.
    - year (int): Год выпуска.
    """

    def __init__(self, model: str, year: int):
        if year < 1886:  # Первый автомобиль был создан в 1886 году
            raise ValueError("Год выпуска не может быть раньше 1886.")
        self.model = model
        self.year = year

    @abstractmethod
    def start_engine(self) -> str:
        """
        Метод, который запускает двигатель транспортного средства.

        :return: Сообщение о запуске двигателя.
        :rtype: str
        :doctest:
        >>> car = Car("Toyota", 2020)
        >>> car.start_engine()
        'Engine started!'
        """
        ...

class Car(Vehicle):
    def start_engine(self) -> str:
        return "Engine started!"

class Building(ABC):
    """
    Абстрактный класс, представляющий здание.

    Атрибуты:
    - address (str): Адрес здания.
    - floors (int): Количество этажей.
    """

    def __init__(self, address: str, floors: int):
        if floors <= 0:
            raise ValueError("Количество этажей должно быть положительным.")
        self.address = address
        self.floors = floors

    @abstractmethod
    def get_info(self) -> str:
        """
        Метод, который возвращает информацию о здании.

        :return: Информация о здании.
        :rtype: str
        :doctest:
        >>> building = Skyscraper("123 Main St", 50)
        >>> building.get_info()
        'Building at 123 Main St with 50 floors.'
        """
        ...

class Skyscraper(Building):
    def get_info(self) -> str:
        return f"Building at {self.address} with {self.floors} floors."
