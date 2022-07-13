import time

from tkinter import Tk, Label, Button
from tkinter import *
import tkinter.font as font

import serial
import serial.tools.list_ports
# ? คืออะไรยังไม่เรียนรู้ >> น่าจะเกี่ยวกับมาตรฐานการสื่อสารอนุกรม RS485
import serial.rs485 
# ? -------------
# ? คืออะไรยังไม่เรียนรู้ >> น่าจะเกี่ยวกับ Comport Network
import serial.rfc2217 
# ? -------------



def serial_port_connected_func():
    return [list(p) for p in list(serial.tools.list_ports.comports())]



def read_data_all_serial_port_connected_function(myports):
    # https://www.scaler.com/topics/python/string-formatting-in-python/  >> Webpage เรียนรู้ Format String >> "{:.>15}".format()
    print("{:.>15} = {}\n{:.>15} = {}\n{:.>15} = {}".format("Data Length", len(myports),"Data Type",type(myports),"Data", myports))
    print("-"*100)
    for i in range(len(myports)):
        print("{:.>15} [{}] = {}\n{:.>15} [{}] = {}\n{:.>15} [{}] = {}".\
                format("Data Length", i, len(myports[i]), \
                        "Data Type", i, type(myports[i]), \
                        "Data", i, myports[i])\
            )
        for j in range(len(myports[i])):
            print("{:.>15} [{}],[{}] = {}\n{:.>15} [{}],[{}] = {}\n{:.>15} [{}],[{}] = {}".\
                    format("Data Length", i, j, len(myports[i][j]), \
                            "Data Type", i, j, type(myports[i][j]), \
                            "Data", i, j, myports[i][j])\
                )
        print("="*100)

def initial_port_function(mySerialPort):
    # print(mySerialPort)
    return serial.Serial(mySerialPort[0][0], baudrate=115200, timeout=1)







# ? Run Program Area
if __name__ == '__main__':
    mySerialPort= serial_port_connected_func()
    # print(mySerialPort)
    # ? -------------------

    # read_data_all_serial_port_connected_function(mySerialPort)
    # ? -------------------

    esp32SerialPort = initial_port_function(mySerialPort)
    print(esp32SerialPort)
    # ? -------------------










