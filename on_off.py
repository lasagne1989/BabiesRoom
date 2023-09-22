async def turn_on(plugs):
    # Turn it on channel 0
    dev = plugs[0]
    await dev.async_update()
    await dev.async_turn_on(channel=0)


async def turn_off(plugs):
    # Turn it on channel 0
    dev = plugs[0]
    await dev.async_update()
    await dev.async_turn_off(channel=0)


if __name__ == '__main__':
    turn_on(plugs)
    turn_off(plugs)
