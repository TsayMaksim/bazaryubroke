import asyncio
from time import sleep


async def traffic_light(colors):
    for i in colors:
        sleep(2)
        print(i)

order = ['red', 'yellow', 'green']


async def traffic_light2(colors):
    for i in colors:
        sleep(2)
        print(i)

order2 = ['RED', 'YELLOW', 'GREEN']


async def main():
    t1 = asyncio.create_task(traffic_light(order))
    t2 = asyncio.create_task(traffic_light2(order2))
    await asyncio.gather(t1, t2)

asyncio.run(main())