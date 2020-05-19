import tkinter as t
from tkinter import ttk

# Creating tkinter window 
window = t.Tk()
window.title('frames')
window.geometry('500x250')


def frameTest():
    # this clearly doesn't work like I though it would
    # it still does stuff though
    """ https://effbot.org/tkinterbook/pack.htm
    side=
    Specifies which side to pack the widget against.
    To pack widgets vertically, use TOP (default).
    To pack widgets horizontally, use LEFT.
    You can also pack widgets along the BOTTOM and RIGHT edges.
    You can mix sides in a single geometry manager,
    but the results may not always be what you expect.
    While you can create pretty complicated layouts by nesting Frame widgets,
    you may prefer using the grid geometry manager for non-trivial layouts.
    """
    top = t.Frame(window).pack()
    bottom = t.Frame(window).pack(side="bottom")
    but1 = t.Button(bottom, text="but1")
    but1.pack(side= "left")
    but2=t.Button(bottom, text="but2", bg="pink")
    but2.pack(side="right", fill="y")
    but3=t.Button(top, text="but3")
    but3.pack()
    but4 = t.Button(bottom, text="but4")
    but4.pack(side=bottom)


def main():
    frameTest()
    window.mainloop()


if __name__ == '__main__':
    main()
