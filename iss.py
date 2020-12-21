#!/usr/bin/env python

__author__ = 'Amanda Simmons, Peter M, Daniel L'
# https://stackoverflow.com/questions/3682748/converting-unix-timestamp-string-to-readable-date
# https://stackoverflow.com/questions/1841565/valueerror-invalid-literal-for-int-with-base-10

import requests
from datetime import datetime
import turtle
import time


def create_turtle_screen():
    screen = turtle.Screen()
    screen.title("Follow the Space station!")
    screen.bgpic("map.gif")
    screen.register_shape("iss.gif")
    screen.setup(width=720, height=360, startx=None, starty=None)
    screen.setworldcoordinates(-180, -90, 180, 90)
    return screen


def create_indy_turtle():
    indy_location = turtle.Turtle()
    indy_location.penup()
    indy_location.setheading(90)
    indy_location.hideturtle()
    indy_location.goto(-86.148003, 39.791000)
    indy_location.dot(5, "yellow")
    indy_location.color("orange")
    indy_location.write(get_iss_pass_time())


def create_iss_turtle(coords):
    iss_turtle_obj = turtle.Turtle()
    iss_turtle_obj.penup()
    iss_turtle_obj.setheading(90)
    iss_turtle_obj.shape("iss.gif")
    lat = int(float(coords['latitude']))
    lon = int(float(coords['longitude']))
    iss_turtle_obj.goto(lon, lat)


def turtle_main(coords):
    screen = create_turtle_screen()
    create_indy_turtle()
    create_iss_turtle(coords)


def get_and_print_astro():
    astro_response_obj = requests.get('http://api.open-notify.org/astros.json')
    data = astro_response_obj.json()
    astronauts = data['people']
    astronaut_total = data['number']
    for astronaut in astronauts:
        print(f'astronaut: {astronaut["name"]}, craft: {astronaut["craft"]}, total astronauts in space: {astronaut_total}')


def get_and_print_iss():
    iss_response_obj = requests.get('http://api.open-notify.org/iss-now.json')
    data = iss_response_obj.json()
    timestamp = int(data['timestamp'])
    human_read_ts = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    coords = data['iss_position']
    print(f'current geographic coordinates of space station: {coords}, timestamp: {human_read_ts}')
    return coords


def get_iss_pass_time():
    iss_response_obj = requests.get('http://api.open-notify.org/iss-pass.json?lat=39.791000&lon=-86.148003')
    data = iss_response_obj.json()
    risetime = data['response'][0]['risetime']
    # print(risetime)
    human_read_ts = time.ctime(risetime)
    return human_read_ts


def main():
    get_and_print_astro()
    coords = get_and_print_iss()
    get_iss_pass_time()
    turtle_main(coords)
    turtle.done()


if __name__ == '__main__':
    main()
