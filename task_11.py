class Dessert:
    def __init__(self, name, calories=None):
        self._name = name
        self._calories = calories

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, value):
        self._calories = value

    def is_healthy(self):
        return self._calories is not None and self._calories < 200

    def is_delicious(self):
        return True


dessert1 = Dessert("Cake", 300)
print(dessert1.is_healthy())    # Вывод: False
print(dessert1.is_delicious())  # Вывод: True

dessert2 = Dessert("Fruit Salad", 150)
print(dessert2.is_healthy())    # Вывод: True
print(dessert2.is_delicious())  # Вывод: True

dessert1.calories = 180
print(dessert1.is_healthy())    # Вывод: True
