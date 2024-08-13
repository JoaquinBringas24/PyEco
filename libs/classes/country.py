

class Country():

    def __init__(self, growth_rate: float, population: int) -> None:
        
        self._growth_rate = growth_rate + 1

        self._population = population

    @property
    def growth_rate(self):
        self._growth_rate

    @property
    def population(self):
        self._population

    def grow(self):
        self._population *= self._growth_rate
