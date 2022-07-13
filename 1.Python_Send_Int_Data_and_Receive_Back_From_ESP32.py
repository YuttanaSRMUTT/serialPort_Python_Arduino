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
    num = input("Enter a number: ")
    value = write_read(num)
    print(value)




'''
count_str = '0'
print(type(count_str))

while True:
    arduino.write(bytes(count_str, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    print(data)
    time.sleep(1)
    count_str = str(int(count_str)+1)
'''



