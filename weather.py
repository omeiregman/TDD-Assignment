'''Q1. Weather data

Assume the attached file port-harcourt-weather.txt contains weather data for Port Harcourt in 2016.
Download this file and write a program that returns the day number (column one) with the smallest temperature spread
(the maximum temperature is the second column, the minimum the third column).'''

import csv


with open("port-harcourt-weather.txt", 'r') as f:
    new = [row for row in csv.reader(f.read().splitlines())]
    print new

with open("test.txt", "w") as new_file:
    new_file.write(str(new))
