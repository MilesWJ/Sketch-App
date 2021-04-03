from tkinter import *

X = 0
Y = 0

COLOR = "black"


def find_xy(event):
    global X, Y
    X, Y = event.x, event.y


def create_line(event):
    global X, Y
    canvas.create_line((X, Y, event.x, event.y), fill=COLOR)
    X, Y = event.x, event.y


def new_canvas():
    canvas.delete("all")


def color_red(event):
    global COLOR
    COLOR = "red"


def color_orange(event):
    global COLOR
    COLOR = "orange"


def color_yellow(event):
    global COLOR
    COLOR = "yellow"


def color_green(event):
    global COLOR
    COLOR = "green"


def color_blue(event):
    global COLOR
    COLOR = "blue"


def color_purple(event):
    global COLOR
    COLOR = "purple"


def color_black(event):
    global COLOR
    COLOR = "black"


sketech_app = Tk()

sketech_app.title("Sketch App")
sketech_app.state("zoomed")

sketech_app.rowconfigure(0, weight=1)
sketech_app.columnconfigure(0, weight=1)

menubar = Menu(sketech_app)
sketech_app.config(menu=menubar)
submenu = Menu(menubar)
menubar.add_cascade(label="File", menu=submenu)
submenu.add_command(label="New Canvas", command=new_canvas)

canvas = Canvas(sketech_app)
canvas.grid(row=0, column=0, sticky="nsew")

canvas.bind("<Button-1>", find_xy)
canvas.bind("<B1-Motion>", create_line)

canvas.bind_all("<Key-1>", color_red)
canvas.bind_all("<Key-2>", color_orange)
canvas.bind_all("<Key-3>", color_yellow)
canvas.bind_all("<Key-4>", color_green)
canvas.bind_all("<Key-5>", color_blue)
canvas.bind_all("<Key-6>", color_purple)
canvas.bind_all("<Key-7>", color_black)

sketech_app.mainloop()
