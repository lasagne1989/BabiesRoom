#from sys import path
#path.insert(0, '/home/raspberry')
import asyncio
from connection import connection
from time import time
import adafruit_dht
from board import D4
import on_off

dht_device = adafruit_dht.DHT22(D4, use_pulseio=True)

upper_limit = 15.0
lower_limit = 14.0


async def main():
    plugs = await connection()
    try:
        temp = dht_device.temperature
        if temp < lower_limit:
            await on_off.turn_on(plugs)
            print("on")
            print(temp)
        if temp > upper_limit:
            await on_off.turn_off(plugs)
            print("off")
            print(temp)
    except RuntimeError as error:
        print(error.args[0])


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main())
    loop.run_forever()
