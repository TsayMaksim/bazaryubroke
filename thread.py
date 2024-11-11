from threading import Thread
from time import sleep


def traffic_light(colors):
    for i in colors:
        sleep(2)
        print(i)


order = ['red', 'yellow', 'green']


def traffic_light2(colors):
    for i in colors:
        sleep(2)
        print(i)


order2 = ['RED', 'YELLOW', 'GREEN']

t1 = Thread(target=traffic_light(order))
t2 = Thread(target=traffic_light2(order2,))
t1.start()
t2.start()