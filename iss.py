#!/usr/bin/env python

__author__ = 'Amanda Simmons, Peter M, Daniel L'
# https://stackoverflow.com/questions/3682748/converting-unix-timestamp-string-to-readable-date
# https://stackoverflow.com/questions/1841565/valueerror-invalid-literal-for-int-with-base-10

import requests
from datetime import datetime
import turtle


def turtle_main(coords):
    screen = turtle.Screen()
    screen.title("Follow the Space station!")
    screen.bgpic("map.gif")
    screen.register_shape("iss.gif")
    screen.setup(width=720, height=360, startx=None, starty=None)
    screen.setworldcoordinates(-180, -90, 180, 90)
    turtle_obj = turtle.Turtle()
    indy_location = turtle.Turtle()
    indy_location.penup()
    indy_location.setheading(90)
    indy_location.hideturtle()
    indy_location.goto(-86.148003, 39.791000)
    indy_location.dot(5, "yellow")

    turtle_obj.penup()
    turtle_obj.setheading(90)
    turtle_obj.shape("iss.gif")
    lat = int(float(coords['latitude']))
    lon = int(float(coords['longitude']))
    turtle_obj.goto(lon, lat)

def main():
    response_obj = requests.get('http://api.open-notify.org/astros.json')
    data = response_obj.json()
    astronauts = data['people']
    astronaut_total = data['number']
    for astronaut in astronauts:
        print(f'astronaut: {astronaut["name"]}, craft: {astronaut["craft"]}, total astronauts in space: {astronaut_total}')

    response_obj = requests.get('http://api.open-notify.org/iss-now.json')
    data = response_obj.json()
    timestamp = int(data['timestamp'])
    human_read_ts = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    coords = data['iss_position']
    print(f'current geographic coordinates of space station: {coords}, timestamp: {human_read_ts}')
    turtle_main(coords)
    turtle.done()
if __name__ == '__main__':
    main()
