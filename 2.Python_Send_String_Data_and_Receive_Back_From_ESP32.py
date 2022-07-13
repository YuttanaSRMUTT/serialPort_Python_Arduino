'''
$ ls /dev/ttyUSB0
'''


'''
import serial

ser = serial.Serial("/dev/ttyUSB0", 115200)

while 1:
    print(ser.readline())
'''


# Importing Libraries
import string
import serial
import time

arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=1)


def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data
    
while True:
    name = input("Enter your name : ")
    value = write_read(name)
    print(value)




