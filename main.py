from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.title("Artist Works")
root.geometry("500x500")

color_input = Entry(root)
color_input.place(relx = 0.6, rely = 0.9, anchor=CENTER)
color_input.insert(0, "Enter color here")

canvas = Canvas(root, width = 500, height = 500, bg = "white", highlightbackground = "lightgrey")
canvas.pack()

img = ImageTk.PhotoImage(Image.open(r"P:\Python projects\Artist\start_point1.png"))
my_image = canvas.create_image(50,50, image=img)

direction = ""
oldx = 50
oldy = 50
newx = 50
newy = 50

def draw(direction, oldx, oldy, newx, newy):
    fill_color = color_input.get

root.bind("<Right>", right_dir)
root.bind("<Left>", left_dir)
root.bind("<Up>", up_dir)
root.bind("<Down>", down_dir)


root.mainloop()