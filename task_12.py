from task_11 import Dessert

class JellyBean(Dessert):
    def __init__(self, name, calories=None, flavor=None):
        super().__init__(name, calories)
        self._flavor = flavor

    @property
    def flavor(self):
        return self._flavor

    @flavor.setter
    def flavor(self, value):
        self._flavor = value

    def is_delicious(self):
        return self._flavor != "black licorice"


jelly_bean = JellyBean("Jelly Bean", 20, "strawberry")
print(jelly_bean.is_delicious())  # Вывод: True

jelly_bean.flavor = "black licorice"
print(jelly_bean.is_delicious())  # Вывод: False
