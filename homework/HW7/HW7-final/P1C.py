from Markov import Markov


# Dict for city and corresponding initial weather
city_weather = {
    'New York': 'rainy',
    'Chicago': 'snowy',
    'Seattle': 'rainy',
    'Boston': 'hailing',
    'Miami': 'windy',
    'Los Angeles': 'cloudy',
    'San Francisco': 'windy'
}

# Dict to store simulation results
city_simulate = {}

# Do simulations
for city in city_weather.keys():
    weather = city_weather[city]
    markov = Markov(weather)
    markov.load_data()

    city_simulate[city] = markov.get_weather_for_day(day=7, trials=100)

# Count the number of occurrences of each weather
weather_list = ['sunny', 'cloudy', 'rainy', 'snowy', 'windy', 'hailing']
for city in city_simulate.keys():
    count_dict = {}
    for weather in weather_list:
        count_dict[weather] = city_simulate[city].count(weather)
    print(f'{city}: {count_dict}')

# print the most commonly predicted weather for each city
print('\nMost likely weather in seven days')
print('----------------------------------')
for city in city_simulate.keys():
    simulation = city_simulate[city]
    print(f'{city}: {max(set(simulation), key=simulation.count)}')
