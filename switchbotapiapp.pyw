from tkinter import colorchooser
from tkinter import *
from tkinter import ttk
import os

with open('devices.txt') as devices:
    devices = [line.rstrip() for line in devices]


print("---- Debug data ----")
print("")
print("Token : " , devices[0])
print("LED Light Line : " , devices[1])
print("Color Bulb Line : " , devices[2])
print("")
print("Dont know how to fix 23 Failed writing body error")
print("")

#==================================================================================================================================
def choose_color():
    color_code = colorchooser.askcolor(title ="Choose color")
    color_code = color_code[0]
    color_result_rgb = ' '.join(format(x, "1.0f") for x in color_code)
    color_code = color_result_rgb.replace(" ", ":")
    print(color_code)
    f = open("json/bulb_color.json", "w")
    f.write("""
    {
        "command": "setColor",
        "parameter": "%s",
        "commandType": "command"
    }
    """ % color_code)
    f.close()
def choose_brightness():
    f = open("json/bulb_brightness.json", "w")
    f.write("""
    {
        "command": "setBrightness",
        "parameter": "%s",
        "commandType": "command"
    }
    """ % brightness.get())
    f.close()
    os.popen('curl -X POST -H "Content-Type: application/json" -d @json/bulb_brightness.json "https://api.switch-bot.com/v1.0/devices/{}/commands"  -H "Authorization: {}"'.format(devices[2],devices[0]))
#==================================================================================================================================
def turn_on():
    os.popen('curl -X POST -H "Content-Type: application/json" -d @json/on.json "https://api.switch-bot.com/v1.0/devices/{}/commands"  -H "Authorization: {}"'.format(devices[1],devices[0]))

def turn_off():
    os.popen('curl -X POST -H "Content-Type: application/json" -d @json/off.json "https://api.switch-bot.com/v1.0/devices/{}/commands"  -H "Authorization: {}"'.format(devices[1],devices[0]))

def brightness_up():
    os.popen('curl -X POST -H "Content-Type: application/json" -d @json/brightness_up.json "https://api.switch-bot.com/v1.0/devices/{}/commands"  -H "Authorization: {}"'.format(devices[1],devices[0]))

def brightness_down():
    os.popen('curl -X POST -H "Content-Type: application/json" -d @json/brightness_down.json "https://api.switch-bot.com/v1.0/devices/{}/commands"  -H "Authorization: {}"'.format(devices[1],devices[0]))

def red():
    os.popen('curl -X POST -H "Content-Type: application/json" -d @json/red.json "https://api.switch-bot.com/v1.0/devices/{}/commands"  -H "Authorization: {}"'.format(devices[1],devices[0]))

def blue():
    os.popen('curl -X POST -H "Content-Type: application/json" -d @json/blue.json "https://api.switch-bot.com/v1.0/devices/{}/commands"  -H "Authorization: {}"'.format(devices[1],devices[0]))

def green():
    os.popen('curl -X POST -H "Content-Type: application/json" -d @json/green.json "https://api.switch-bot.com/v1.0/devices/{}/commands"  -H "Authorization: {}"'.format(devices[1],devices[0]))

def purple():
    os.popen('curl -X POST -H "Content-Type: application/json" -d @json/purple.json "https://api.switch-bot.com/v1.0/devices/{}/commands"  -H "Authorization: {}"'.format(devices[1],devices[0]))
#==================================================================================================================================
def turn_on2():
    os.popen('curl -X POST -H "Content-Type: application/json" -d @json/on.json "https://api.switch-bot.com/v1.0/devices/{}/commands"  -H "Authorization: {}"'.format(devices[2],devices[0]))

def turn_off2():
    os.popen('curl -X POST -H "Content-Type: application/json" -d @json/off.json "https://api.switch-bot.com/v1.0/devices/{}/commands"  -H "Authorization: {}"'.format(devices[2],devices[0]))

def send_data():
    os.popen('curl -X POST -H "Content-Type: application/json" -d @json/bulb_color.json "https://api.switch-bot.com/v1.0/devices/{}/commands"  -H "Authorization: {}"'.format(devices[2],devices[0]))
#==================================================================================================================================

window = Tk()

#==================================================================================================================================
img1 = PhotoImage(file="images/box1.png")
box1 = Canvas(window, width = 293, height = 287, highlightthickness=0, bd=0)
box1.pack()  
box1.place(x=1, y=0)
box1.create_image(0, 0, anchor=NW, image=img1) 

window.geometry('700x500')
window.title("Switchbot API App")
icon = PhotoImage(file = "images/icon.png")
window.iconphoto(False, icon)
window.configure(bg='gray')

on_img=PhotoImage(file='images/on.png')
on_button = Button(window, highlightthickness=0, bd=0, text='', image=on_img, command=lambda: turn_on())
on_button.pack(ipadx=5, ipady=5, expand=True)
on_button.place(x=15, y=50)

off_img=PhotoImage(file='images/off.png')
off_button = Button(window, highlightthickness=0, bd=0, text='', image=off_img, command=lambda: turn_off())
off_button.pack(ipadx=5, ipady=5, expand=True)
off_button.place(x=15, y=90)

brightness_up_img=PhotoImage(file='images/brightness_up.png')
brightness_up_button = Button(window, highlightthickness=0, bd=0, text='', image=brightness_up_img, command=lambda: brightness_up())
brightness_up_button.pack(ipadx=5, ipady=5, expand=True)
brightness_up_button.place(x=135, y=48)

brightness_down_img=PhotoImage(file='images/brightness_down.png')
brightness_down_button = Button(window, highlightthickness=0, bd=0, text='', image=brightness_down_img, command=lambda: brightness_down())
brightness_down_button.pack(ipadx=5, ipady=5, expand=True)
brightness_down_button.place(x=135, y=90)

red_img=PhotoImage(file='images/red.png')
red_button = Button(window, highlightthickness=0, bd=0, text='', image=red_img, command=lambda: red())
red_button.pack(ipadx=5, ipady=5, expand=True)
red_button.place(x=15, y=180)

blue_img=PhotoImage(file='images/blue.png')
blue_button = Button(window, highlightthickness=0, bd=0, text='', image=blue_img, command=lambda: blue())
blue_button.pack(ipadx=5, ipady=5, expand=True)
blue_button.place(x=15, y=225)

purple_img=PhotoImage(file='images/purple.png')
purple_button = Button(window, highlightthickness=0, bd=0, text='', image=purple_img, command=lambda: purple())
purple_button.pack(ipadx=5, ipady=5, expand=True)
purple_button.place(x=175, y=180)

green_img=PhotoImage(file='images/green.png')
green_button = Button(window, highlightthickness=0, bd=0, text='', image=green_img, command=lambda: green())
green_button.pack(ipadx=5, ipady=5, expand=True)
green_button.place(x=175, y=225)
#==================================================================================================================================

img2 = PhotoImage(file="images/box2.png")
box2 = Canvas(window, width = 293, height = 287, highlightthickness=0, bd=0)
box2.pack()
box2.place(x=300, y=0)
box2.create_image(0,0 , anchor=NW, image=img2)

choose_color_img=PhotoImage(file='images/choose_color.png')
choose_color = Button(window, highlightthickness=0, bd=0, text='', image=choose_color_img, command = choose_color)
choose_color.pack(ipadx=5, ipady=5, expand=True)
choose_color.place(x=310, y=90)

on2_img=PhotoImage(file='images/on.png')
on2_button = Button(window, highlightthickness=0, bd=0, text='', image=on_img, command=lambda: turn_on2())
on2_button.pack(ipadx=5, ipady=5, expand=True)
on2_button.place(x=470, y=90)

off2_img=PhotoImage(file='images/off.png')
off2_button = Button(window, highlightthickness=0, bd=0, text='', image=off_img, command=lambda: turn_off2())
off2_button.pack(ipadx=5, ipady=5, expand=True)
off2_button.place(x=470, y=50)

send_data_img=PhotoImage(file='images/send_data.png')
send_data_button = Button(window, highlightthickness=0, bd=0, text='', image=send_data_img, command=lambda: send_data())
send_data_button.pack(ipadx=5, ipady=5, expand=True)
send_data_button.place(x=310, y=50)

brightness = Scale(window, from_=0, to=100, length=260, orient=HORIZONTAL, highlightthickness=0, bd=0)
brightness.pack()
brightness.place(x=315, y=170)
print(brightness.get())

send_data1_img=PhotoImage(file='images/send_data.png')
send_data1_button = Button(window, highlightthickness=0, bd=0, text='', image=send_data1_img, command=lambda: choose_brightness())
send_data1_button.pack(ipadx=5, ipady=5, expand=True)
send_data1_button.place(x=385, y=210)

#==================================================================================================================================
window.mainloop()

