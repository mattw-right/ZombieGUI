

from tkinter import *
import time
from model import World
import tkinter as tk


def all_children (window) :
    _list = window.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list

def update(count, w, myworld):
    w.delete("all")
    myworld.update_world(count)

    infected, healthy, doctors = myworld.create_coord_list()

    for i in range(len(infected)):
        paint(infected[i, 0], infected[i, 1], '#FF0000', w)

    for i in range(len(healthy)):
        paint(healthy[i, 0], healthy[i, 1], '#0000FF', w)

    for i in range(len(doctors)):
        paint(doctors[i][0], doctors[i][1], '#00FF00', w)

    master.update()



def paint(x, y, colour, w):
    python_green = colour
    x1, y1 = (x - 3 + 100), (y - 3 + 100)
    x2, y2 = (x + 3 + 100), (y + 3 + 100)
    w.create_oval(x1, y1, x2, y2, fill=python_green)



def do():
    population = int(e1.get())
    initial_infection_rate = float(e2.get())
    closeness = int(e3.get())
    dimensions = int(e4.get())
    speed = int(e5.get())
    frequency = int(e6.get())
    turns = int(e7.get())
    no_doctors = int(e8.get())
    train_new_doctor_frequency = int(e9.get())
    length_of_immunity = int(e10.get())


    widget_list = all_children(master)
    for item in widget_list:
        item.pack_forget()

    myworld = World(population, initial_infection_rate, closeness, dimensions, speed, frequency, turns, no_doctors, length_of_immunity)
    myworld.populate_world(population, initial_infection_rate, closeness)

    w = Canvas(master,
               width=canvas_width,
               height=canvas_height)
    w.pack(expand=YES, fill=BOTH)

    for i in range(turns):
        update(i, w, myworld)
        if i % train_new_doctor_frequency == 0:
            myworld.train_doctor()
        time.sleep(0.05)

    mainloop()



#######################################

canvas_width = 750
canvas_height = 750


master = Tk()
master.title("Points")







################################

tk.Label(master, text="Population").pack(expand=YES, fill=BOTH)
e1 = tk.Entry(master)
e1.pack(expand=YES, fill=BOTH)
e1.insert(10, "200")

tk.Label(master, text="Initial Infection Rate").pack(expand=YES, fill=BOTH)
e2 = tk.Entry(master)
e2.pack(expand=YES, fill=BOTH)
e2.insert(10, "0.5")

tk.Label(master, text="Closeness").pack(expand=YES, fill=BOTH)
e3 = tk.Entry(master)
e3.pack(expand=YES, fill=BOTH)
e3.insert(10, "20")

tk.Label(master, text="Dimensions").pack(expand=YES, fill=BOTH)
e4 = tk.Entry(master)
e4.pack(expand=YES, fill=BOTH)
e4.insert(10, "500")

tk.Label(master, text="Speed").pack(expand=YES, fill=BOTH)
e5 = tk.Entry(master)
e5.pack(expand=YES, fill=BOTH)
e5.insert(10, "10")

tk.Label(master, text="Frequency").pack(expand=YES, fill=BOTH)
e6 = tk.Entry(master)
e6.pack(expand=YES, fill=BOTH)
e6.insert(10, "15")

tk.Label(master, text="Turns").pack(expand=YES, fill=BOTH)
e7 = tk.Entry(master)
e7.pack(expand=YES, fill=BOTH)
e7.insert(10, "1000")

tk.Label(master, text="Initial No. of Doctors").pack(expand=YES, fill=BOTH)
e8 = tk.Entry(master)
e8.pack(expand=YES, fill=BOTH)
e8.insert(10, "1")

tk.Label(master, text="Train New Doctor Frequency").pack(expand=YES, fill=BOTH)
e9 = tk.Entry(master)
e9.pack(expand=YES, fill=BOTH)
e9.insert(10, "100")

tk.Label(master, text="Length of Immunity").pack(expand=YES, fill=BOTH)
e10 = tk.Entry(master)
e10.pack(expand=YES, fill=BOTH)
e10.insert(10, "10")

tk.Button(master, text='Go', command=do).pack(expand=YES, fill=BOTH)



mainloop()


#####################################


