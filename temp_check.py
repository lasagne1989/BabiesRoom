import adafruit_dht
from board import D4
from time import sleep

dht_device = adafruit_dht.DHT22(D4, use_pulseio=True)

def temp_check():
    try:
        temperature = dht_device.temperature



if __name__ == '__main__':
    temp_check()