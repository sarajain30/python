from tkinter import *
import random
import time

W = 800
H = 600

tk = Tk()
can = Canvas(tk, width=W, height=H)
tk.title("BOING")
can.pack()

ball1 = can.create_oval(10, 10, 60, 60, fill="lime green")
ball2 = can.create_oval(300, 50, 350, 100, fill="red")

xs1 = 9
ys1 = 5

xs2 = 10
ys2 = 6

while True:
    can.move(ball1, xs1, ys1)
    pos1 = can.coords(ball1)
    if pos1[3] >= H or pos1[1] <= 0:
        ys1 = -ys1
    if pos1[2] >= W or pos1[0] <= 0:
        xs1 = -xs1
        

    can.move(ball2, xs2, ys2)
    pos2 = can.coords(ball2)
    if pos2[3] >= H or pos2[1] <= 0:
        ys2 = -ys2
    if pos2[2] >= W or pos2[0] <= 0:
        xs2 = -xs2

    if abs(pos1[3] -pos2[3]) <50 and abs (pos2[2] -pos1[2]) <50:
         ys1 = -ys1
         xs1 = -xs1
         ys2 = -ys2
         xs2 = -xs2
    tk.update()
    time.sleep(0.01)

tk.mainloop()








