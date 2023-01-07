import customtkinter
import tkinter
import tkinter as Tk
from tkinter import *

# GAIN PLUGIN

root = Tk()
root.resizable(height=False,width=False)
root.geometry("300x500")
root.title("Giga Maximizer")
root['bg']='black'

def segmented_button_callback(value):
    print("segmented button clicked:", value)

segemented_button = customtkinter.CTkSegmentedButton(
                    master=root,values=["Gain AU", "Gain EX", "Gain FX"],
                    command=segmented_button_callback)
segemented_button.pack(padx=20, pady=67)
img = PhotoImage(file='/Users/mini/Desktop/Miscellaneous/pics.png')
btn = Button(root, fg="black",image=img,padx=5,pady=5)
btn.pack()
btn.place(x=125,y=10)

def button_event():
    print("button pressed")

button = customtkinter.CTkButton(
            master=root,width=120,height=32,
            border_width=0,corner_radius=8,
            text="Mute",command=button_event
            )

button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)
txt = Label(root,text="Gain +")
txt.config(font=("Helvetica regular",16))
txt.pack()
txt.place(x=119,y=110)

txt = Label(root,text="0db")
txt.config(font=("Helvetica regular",16))
txt.pack()
txt.place(x=132,y=360)

def slider_event(value):
    print(value)

slider = customtkinter.CTkSlider(master=root,orientation=VERTICAL, 
                                from_=0, to=100, command=slider_event)
slider.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

root.mainloop()