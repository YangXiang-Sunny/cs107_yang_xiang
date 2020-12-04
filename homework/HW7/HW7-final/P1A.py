from Markov import Markov


weather_today = Markov()
weather_today.load_data(file_path='./weather.csv')
print(weather_today.get_prob('cloudy', 'windy'))    # This line should print 0.08


