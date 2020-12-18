#!/usr/bin/env python

__author__ = 'Amanda Simmons, Peter M'
# https://stackoverflow.com/questions/3682748/converting-unix-timestamp-string-to-readable-date

import requests
from datetime import datetime
from turtle import *

def turtle_test():
    screen = Screen()
    screen.bgpic("map.gif")
    turtle_obj = Turtle()
    turtle_obj.shape('turtle')
    turtle_obj.color('red', 'yellow')
    turtle_obj.begin_fill()
    while True:
        turtle_obj.forward(200)
        turtle_obj.left(170)
        if abs(turtle_obj.pos()) < 1:
            break
    turtle_obj.end_fill()
    turtle_obj.done()

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
    turtle_test()
if __name__ == '__main__':
    main()
