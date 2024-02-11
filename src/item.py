import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return f'{self.name}'

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.pay_rate * self.price
        return self.price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, title):
        if len(title) >= 10:
            self.__name = title[:10]
        else:
            self.__name = title

    @classmethod
    def instantiate_from_csv(cls, file_name):
        """
        Класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv
        """
        cls.all.clear()
        with open(file_name, 'r')as f:
            reader = csv.DictReader(f)
            items = list(reader)
            for item in items:
                print(cls(name=item.get('name'),
                          price=item.get('price'),
                          quantity=item.get('quantity')))

    @staticmethod
    def string_to_number(name):
        """
        Статический метод, возвращающий число из числа-строки
        """
        return int(float(name))



