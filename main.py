import asyncio
from connection import connection
import adafruit_dht
from board import D4
import on_off

dht_device = adafruit_dht.DHT22(D4, use_pulseio=True)

upper_limit = 18.0
lower_limit = 17.9


async def main(heater_on=False, cycle=0):
    plugs = await connection()
    while True:
        try:
            temp = dht_device.temperature
            print(f"Temperature: {temp} Heater On: {heater_on}")
            if heater_on:
                cycle += 1

            if temp < lower_limit and heater_on is False:
                await on_off.turn_on(plugs)
                print(f"Temperature dropped below {lower_limit}, heater turned on.")
                heater_on = not heater_on

            if temp > upper_limit and heater_on is True:
                await on_off.turn_off(plugs)
                time_on = round((cycle * 5) / 60)
                print(f"Temperature rose above {upper_limit}, heater turned off. Heater was on for {time_on} mins")
                heater_on = not heater_on
                cycle = 0
        except RuntimeError:
            print("NEEEEEEEEEEEEEEEWO")
        await asyncio.sleep(5)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main())
    loop.run_forever()
