from meross_iot.http_api import MerossHttpClient
from meross_iot.manager import MerossManager

EMAIL = "xxxxxx@xxxx.com"
PASSWORD = "xxxx"


async def connection():
    # Setup the HTTP client API from user-password
    http_api_client = await MerossHttpClient.async_from_user_password(email=EMAIL, password=PASSWORD)

    # Setup and start the device manager
    manager = MerossManager(http_client=http_api_client)
    await manager.async_init()

    # Retrieve the devices I want
    await manager.async_device_discovery()
    plugs = manager.find_devices(device_name="heater")
    sensors = manager.find_devices(device_type='ms100')
    print(f"Number of plugs: {len(plugs)}. Number of sensors: {len(sensors)}")
    if len(plugs) < 1 or len(sensors) < 1:
        print(f"Number of plugs: {len(plugs)}. Number of sensors: {len(sensors)}")
        # Close the manager and logout from http_api
        manager.close()
        await http_api_client.async_logout()
    return plugs, sensors


if __name__ == '__main__':
    connection()
