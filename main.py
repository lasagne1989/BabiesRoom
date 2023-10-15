# from sys import path
# path.insert(0, '/home/raspberry')
import asyncio
from connection import connection
import adafruit_dht
from board import D4
import on_off

dht_device = adafruit_dht.DHT22(D4, use_pulseio=True)

upper_limit = 18.0
lower_limit = 17.0


async def main(heater_on=False):
    plugs = await connection()
    while True:
        try:
            temp = await dht_device.temperature
            print(temp)
            if heater_on:
                print("Heater On!")
            if not heater_on:
                print("Heater Off!)")
            if temp < lower_limit and heater_on is False:
                await on_off.turn_on(plugs)
                print("on")
                print(temp)
                heater_on = not heater_on
                print(heater_on)

            if temp > upper_limit and heater_on is True:
                await on_off.turn_off(plugs)
                print("off")
                print(temp)
                heater_on = not heater_on
                print(heater_on)
        except RuntimeError as error:
            print(error.args[0])
        await asyncio.sleep(5)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main())
    loop.run_forever()
