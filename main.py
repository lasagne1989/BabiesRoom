import asyncio
from connection import connection
from temp_check import temp_check
from time import time
import on_off

upper_limit = 18.5
lower_limit = 17.5

async def main():
    await asyncio.sleep(60)
    plugs, sensors = await connection()
    heater = "start"
    start_time = time()
    while True:
        temp = await temp_check(sensors)
        if temp < lower_limit and heater != "on":
            await on_off.turn_on(plugs)
            heater = "on"
            print("Heater on")
            start_time = time()
        if temp > upper_limit and heater != "off":
            await on_off.turn_off(plugs)
            heater = "off"
            end_time = time() - start_time
            print(f"Heater off after {end_time/60} mins")
        await asyncio.sleep(300)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main())
    loop.run_forever()