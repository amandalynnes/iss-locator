#!/usr/bin/env python

__author__ = 'Amanda Simmons'

import requests


def main():
    response_obj = requests.get('http://api.open-notify.org/astros.json')
    data = response_obj.json()
    astronauts = data['people']
    astronaut_total = data['number']
    # print(astronauts)
    for astronaut in astronauts:
        print(f'astronaut: {astronaut["name"]}, craft: {astronaut["craft"]}, total astronauts in space: {astronaut_total}')


if __name__ == '__main__':
    main()
