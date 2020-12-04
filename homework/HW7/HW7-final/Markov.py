import numpy as np


class Markov:
    def __init__(self, day_zero_weather=None):
        self.data = np.array([])
        self.weathers = ['sunny', 'cloudy', 'rainy', 'snowy', 'windy', 'hailing']
        if day_zero_weather in self.weathers:
            self.day_zero_weather = day_zero_weather
        else:
            raise Exception('Day zero weather is not valid! ')

    def load_data(self, file_path='./weather.csv'):
        self.data = np.genfromtxt(file_path, delimiter=',')

    def get_prob(self, current_day_weather, next_day_weather):
        if current_day_weather not in self.weathers:
            raise Exception('Current day weather is not valid! ')
        if next_day_weather not in self.weathers:
            raise Exception('Next day weather is not valid! ')

        idx_current = self.weathers.index(current_day_weather)
        idx_next = self.weathers.index(next_day_weather)
        return self.data[idx_current, idx_next]

    def _simulate_weather_for_day(self, day):
        markov_iter = iter(self)
        for i in range(day):
            next(markov_iter)
        return next(markov_iter)

    def get_weather_for_day(self, day, trials=100):
        result = []
        for i in range(trials):
            result.append(self._simulate_weather_for_day(day))
        return result

    def __iter__(self):
        return MarkovIterator(self.day_zero_weather, self.data, self.weathers)


class MarkovIterator:
    def __init__(self, day_zero_weather, data, weathers):
        self._current_day_weather = day_zero_weather
        self.data = data
        self.weathers = weathers

    def __next__(self):
        weather_current_day = self._current_day_weather

        # Simulate next day
        idx_current_day = self.weathers.index(self._current_day_weather)
        prob = self.data[idx_current_day, :].tolist()
        idx_next_day = np.random.choice(len(self.weathers), 1, p=prob)[0]
        self._current_day_weather = self.weathers[idx_next_day]

        return weather_current_day

    def __iter__(self):
        return self

