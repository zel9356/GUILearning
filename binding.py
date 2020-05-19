import tkinter as t

"""
Binding functions are the ones called when an event occurs
"""
window = t.Tk()
window.title("GUI")


def eventHandling():
    # this allows something to happen over and over when a button is clicked
    # instead of just the first click causing something
    def clicked(event):
        t.Label(window, text="clicked").pack()

    but1 = t.Button(window, text="PRESS ME")
    but1.bind("<Button-1>", clicked)
    but1.pack()


def clicking():
    def rightClick(event):
        t.Label(window, text="Right Click!!").pack()

    def leftClick(event):
        t.Label(window, text="Left Click!!").pack()

    def midClick(event):
        t.Label(window, text="mid Click!!").pack()

    # buttons corresponds to dif possible mose clicks
    window.bind("<Button-1>", leftClick)
    window.bind("<Button-2>", midClick)
    window.bind("<Button-3>", rightClick)


def main():
    # eventHandling()
    clicking()
    window.mainloop()


if __name__ == '__main__':
    main()
