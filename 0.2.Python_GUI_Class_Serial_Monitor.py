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



class SerialPortReader:
    def __init__(self, master):
        self.master = master
        self.master.title("connecting port")
        self.master.geometry('510x265')
        self.master.option_add('*font','corbert 20')

        # font
        self.frame_font  = font.Font(family='Helvetica', size=12, weight='bold')
        self.header_font = font.Font(family='Helvetica',size=30, weight='bold')
        self.input_font = font.Font(family='Helvetica',size=16, weight='bold')
        self.display_font = font.Font(family='Helvetica',size=20, weight='bold')


        # HEADER GUI LAYOUT  < *******************************************************
        self.frame_header = Frame(self.master)
        self.frame_header.grid(row=0, column=0, columnspan=3)
        self.lbl_header = Label(self.frame_header, text='CONNECT PORT', borderwidth=0, relief=GROOVE , width=22, height=3)
        self.lbl_header.grid(row=0, column=0, pady=3, padx=5)
        self.lbl_header['font'] = self.header_font
        self.lbl_header['fg'] = 'snow'
        self.lbl_header['bg'] = 'gray26'


        # Connect Layout  < ********************************************************
        self.frame_connect_system = LabelFrame(self.master, text = '  Connect System', fg='gray26')
        self.frame_connect_system['font'] = self.frame_font 
        self.frame_connect_system.grid(row=1, column=0, ipady=5, ipadx=2)


        self.read_serial_btn = Button(self.frame_connect_system, text="Read Port")
        self.read_serial_btn['font'] = self.input_font
        self.read_serial_btn.bind("<Button-1>",self.read_data_all_serial_port_connected_func) # Click เม้าท์ซ้าย OK
        self.read_serial_btn['fg'] = 'snow'
        self.read_serial_btn['bg'] = 'blue'
        self.read_serial_btn.grid(row=0, column=0, pady=3, padx=2, sticky=E)

        self.connect_btn = Button(self.frame_connect_system, text="Connect Port")
        self.connect_btn['font'] = self.input_font
        self.connect_btn.bind("<Button-1>",self.connecting_serial_port_func) # Click เม้าท์ซ้าย OK
        self.connect_btn['fg'] = 'snow'
        self.connect_btn['bg'] = 'green4'
        self.connect_btn.grid(row=0, column=1, pady=3, padx=2, sticky=E)


      



    def serial_port_func(self, event):
        return [list(p) for p in list(serial.tools.list_ports.comports())]
    # ? ----------------------> End of serial_port_func 


    def read_data_all_serial_port_connected_func(self, event):
        myports = self.serial_port_func(event)
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
    # ? ----------------------> End of read_data_all_serial_port_connected_func 



    def connecting_serial_port_func(self, event):
        myports = self.serial_port_func(event)
        esp32Port = serial.Serial(myports[0][0], baudrate=115200, timeout=.1)
        print(esp32Port)
        return esp32Port
    # ? ----------------------> End of connecting_serial_port_func 




if __name__ == '__main__':
    root = Tk()
    my_gui = SerialPortReader(root)
    root.mainloop()