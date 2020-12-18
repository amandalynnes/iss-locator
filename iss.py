#!/usr/bin/env python

__author__ = 'Amanda Simmons, Peter M'
# https://stackoverflow.com/questions/3682748/converting-unix-timestamp-string-to-readable-date
# https://stackoverflow.com/questions/1841565/valueerror-invalid-literal-for-int-with-base-10

import requests
from datetime import datetime
import turtle

def turtle_test(coords):
    screen = turtle.Screen()
    screen.title("Follow the Space station!")
    screen.bgpic("map.gif")
    screen.register_shape("iss.gif")
    screen.setup(width=720, height=360, startx=None, starty=None)
    turtle_obj = turtle.Turtle()
    # turtle_obj.setup(width=.90, height=0.9, startx=None, starty=None)
    turtle_obj.penup()
    turtle_obj.setheading(90)
    turtle_obj.shape("iss.gif")
    lat = int(float(coords['latitude']))
    lon = int(float(coords['longitude']))
    turtle_obj.goto(lat, lon)

def main():
    response_obj = requests.get('http://api.open-notify.org/astros.json')
    data = response_obj.json()
    astronauts = data['people']
    astronaut_total = data['number']
    # print(astronauts)
    for astronaut in astronauts:
        print(f'astronaut: {astronaut["name"]}, craft: {astronaut["craft"]}, total astronauts in space: {astronaut_total}')

    response_obj = requests.get('http://api.open-notify.org/iss-now.json')
    data = response_obj.json()
    # print(data)
    timestamp = int(data['timestamp'])
    human_read_ts = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    coords = data['iss_position']
    print(f'current geographic coordinates of space station: {coords}, timestamp: {human_read_ts}')
    turtle_test(coords)
    turtle.done()
if __name__ == '__main__':
    main()
