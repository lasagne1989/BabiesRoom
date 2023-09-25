from meross_iot.http_api import MerossHttpClient
from meross_iot.manager import MerossManager
from sys import path
path.insert(0, 'home/raspberry')
from data import logon


async def connection():
    EMAIL, PASSWORD = logon()

    # Setup the HTTP client API from user-password
    http_api_client = await MerossHttpClient.async_from_user_password(email=EMAIL, password=PASSWORD)

    # Setup and start the device manager
    manager = MerossManager(http_client=http_api_client)
    await manager.async_init()

    # Retrieve the devices I want
    await manager.async_device_discovery()
    plugs = manager.find_devices(device_name="heater")
    print(f"Number of plugs: {len(plugs)}")
    if len(plugs) < 1:
        print(f"Number of plugs: {len(plugs)}")
        # Close the manager and logout from http_api
        manager.close()
        await http_api_client.async_logout()
    return plugs


if __name__ == '__main__':
    connection()
