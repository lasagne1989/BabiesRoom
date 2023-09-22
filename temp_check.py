async def temp_check(sensors):
    print(sensors)
    dev = sensors[0]
    await dev.async_update()
    # Access read cached data
    temp = dev.last_sampled_temperature
    print(temp)
    return temp


if __name__ == '__main__':
    temp_check()