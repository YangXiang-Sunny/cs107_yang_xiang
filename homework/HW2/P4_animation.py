import numpy as np
import matplotlib.pyplot as plt
import datetime


# Define closure
def clock_r(r):
    def clock_theta(theta):
        radian = float(theta) / 180 * np.pi
        x = r * np.cos(radian)
        y = r * np.sin(radian)
        return x, y
    return clock_theta


fig = plt.figure(figsize=(6, 6))

while datetime.datetime.now().second != 0:
    CurrentDT = datetime.datetime.now()
    hour = CurrentDT.hour
    minute = CurrentDT.minute
    second = CurrentDT.second

    # Calculate theta in degrees for each hand
    theta_hour = 90 - 30*hour - float(minute)/2
    theta_minute = 90 - 6*minute
    theta_second = 90 - 6*second

    # Specify the length of hour, minute and second hands
    length_hour = 0.5
    length_minute = 1
    length_second = 2

    # hour_hand = name_of_closure(length_of_hour_hand)
    hour_hand = clock_r(length_hour)
    minute_hand = clock_r(length_minute)
    second_hand = clock_r(length_second)

    # x_hour, y_hour = hour_hand(theta_hour)
    x_hour, y_hour = hour_hand(theta_hour)
    x_minute, y_minute = minute_hand(theta_minute)
    x_second, y_second = second_hand(theta_second)

    # Plot the clock
    plt.cla()
    plt.plot([0, x_hour], [0, y_hour], linewidth=4)
    plt.plot([0, x_minute], [0, y_minute], linewidth=2)
    plt.plot([0, x_second], [0, y_second], linewidth=1)
    plt.axis([-length_second, length_second, -length_second, length_second])
    plt.axis('off')
    fig.canvas.draw()
    plt.pause(0.1)
