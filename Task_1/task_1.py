from itertools import cycle
import time

class TrafficLight:

    __color = ['red', 'yellow', 'green', 'yellow']

    def running(self):
        tempValue = 0
        for color in cycle(self.__color):
            if color == 'red':
                tempValue = 7
            elif color == 'yellow':
                tempValue = 2
            else:
                tempValue = 10
            print(f'The {color} light is on now')
            time.sleep(tempValue)

traffic_light = TrafficLight()
traffic_light.running()