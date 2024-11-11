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


###


def red():
    print('red')


def yellow():
    print('yellow')


def green():
    print('green')


t1 = Thread(target=red())
t2 = Thread(target=yellow())
t3 = Thread(target=green())

t1.start()
t2.start()
t3.start()