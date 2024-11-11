from time import sleep


def traffic_light(colors):
    for i in colors:
        yield i

order = ['red', 'yellow', 'green']
all_colors = traffic_light(order)


def traffic_light2(colors):
    for i in colors:
        sleep(2)
        print(i)

order2 = ['RED', 'YELLOW', 'GREEN']


print(next(all_colors, sleep(2)))
print(next(all_colors, sleep(2)))
print(next(all_colors, sleep(2)))
traffic_light2(order2)