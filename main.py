from sys import path
path.insert(0, 'home/raspberry')
import asyncio
from connection import connection
from time import time
import adafruit_dht
from board import D4
import on_off

dht_device = adafruit_dht.DHT22(D4, use_pulseio=True)

upper_limit = 18.5
lower_limit = 17.5


async def main():
    plugs, sensors = await connection()
    heater_on = True
    try:
        temp = dht_device.temperature
        if temp < lower_limit and heater_on == False:
            await on_off.turn_on(plugs)
            heater_on = True
            print("On")
        if temp > upper_limit and heater_on:
            await on_off.turn_off(plugs)
            heater_on = False
            print("off")
    except RuntimeError as error:
        print(error.args[0])


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main())
    loop.run_forever()
