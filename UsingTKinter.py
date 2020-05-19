import tkinter as t
from tkinter import ttk, scrolledtext, messagebox


def intro():
    # making our widow where widgets will go, named window
    window = t.Tk()
    window.geometry('2080x1000')  # setting window size, this is roughly the size of my screen
    window.title("Gui")  # giving the window a title
    # making a label, in the window with text "hello"
    # pack, puts lable into window, centered
    label = t.Label(window, text="Hello").pack()
    label1 = t.Label(window, text="New Label")
    # places with border/increadsed size
    # label1.place(bordermode=t.OUTSIDE, height=100, width=100)
    # places at center
    label1.place(relx=.5, rely=.5, anchor=t.CENTER)
    # main loop will display the window
    window.mainloop()


def buttons():
    window = t.Tk()
    window.geometry('2080x1000')  # setting window size, this is roughly the size of my screen
    window.title("Gui")
    # we cannot mix pack and grid placment methods together
    # here we are placing the label at coordinates 0,0
    # do not combine these two lines, if so label will have none
    # type and we cant change the text of it later
    label = t.Label(window, text="Hello")
    label.grid(column=0, row=0)

    # here we are creating a method that will occur when our button is pressed
    def click():
        # changes the text of the label to "PUSHED"
        label.configure(text="PUSHED")

    # making a button in window with test "button!!"
    # bg is the background color of the button
    # fg is the text color, so here we are creating a purple button w/ white text
    # command is the function that will occur when pressed
    but = t.Button(window, text="Button!!", bg="purple", fg="white", command=click)
    # we are using .gris to place the button in the same row but one colm over
    # from the label. This has coordinates 1,0
    but.grid(column=1, row=0)
    window.mainloop()


def entry():
    window = t.Tk()
    window.geometry('2080x1000')  # setting window size, this is roughly the size of my screen
    window.title("Gui")
    label = t.Label(window, text="Hello")
    label.grid(column=0, row=0)
    # Entry is an input field
    # we create the entry box with width 10
    entryBox = t.Entry(window, width=10)
    # and we place it at 3,3
    entryBox.grid(column=3, row=3)

    # making an evnt that occur when button is pressed
    def click():
        # get text from entry box and change label to that
        tempText = "The word is " + entryBox.get()
        label.configure(text=tempText)

    but = t.Button(window, text="enter", bg="purple", fg="white", command=click)
    # we are using .gris to place the button in the same row but one colm over
    # from the label. This has coordinates 1,0
    but.grid(column=1, row=0)
    window.mainloop()


def comboBox():
    window = t.Tk()
    window.title('Combobox')
    window.geometry('500x250')
    # Combobox creation
    n = t.StringVar()
    newCBox = ttk.Combobox(window, width=10, textvariable=n)

    # Adding combobox drop down list
    newCBox['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "none")

    newCBox.grid(column=1, row=0)
    # this sets the current value the box is on to element 10 in the tuple/ "none"
    newCBox.current(10)
    window.mainloop()


def checkButton():
    # check box
    # can select mutiple
    window = t.Tk()
    window.title('Check Button')
    window.geometry('500x250')
    # this is a tkinter var type
    stateOfChk = t.BooleanVar()
    # we make that true
    stateOfChk.set(True)
    # when we put stateOfChk in as the var the box starts checked
    # if it were false it would start un checked
    # here we are making the check bos in our window with text "select me" and var state
    chk = ttk.Checkbutton(window, text="select me", var=stateOfChk)
    chk.grid(column=0, row=0)
    window.mainloop()


def radioButton():
    # this is a circular check box i guess
    window = t.Tk()
    window.title('Radio Button')
    window.geometry('500x250')
    aList = []
    # making Radio buttons in window with text and a UNIQUE value
    # if value is not unique error will occur
    # only when can be picked/checked at once
    aList.append(ttk.Radiobutton(window, text="A", value=1))
    aList.append(ttk.Radiobutton(window, text="B", value=2))
    aList.append(ttk.Radiobutton(window, text="C", value=3))
    aList.append(ttk.Radiobutton(window, text="D", value=4))
    # since we add the buttons to a list we can ad them with a for loop
    for i in range(0, 4):
        aList[i].grid(column=i, row=0)
    window.mainloop()


def scrolledText():
    # scrolling box of text
    window = t.Tk()
    window.title('Scrolled Text')
    window.geometry('500x250')
    # if hight and width not given it will be entire window
    scrolly = scrolledtext.ScrolledText(window, width=30, height=5)
    # pack, which will center it at the top
    scrolly.pack()
    # and wee need to give it text with the insert method, make sure the first var is INSERT from TKinter
    # the second is our text
    scrolly.insert(t.INSERT, "It was the best of times, it was the worst of times, "
                             "it was the age of wisdom, it was the age of foolishness, "
                             "it was the epoch of belief, it was the epoch of incredulity, "
                             "it was the season of Light, it was the season of Darkness, "
                             "it was the spring of hope, it was the winter of despair, "
                             "we had everything before us, ")
    window.mainloop()


def messageBox():
    # SHOWS A MESSAGE IN A BOX
    window = t.Tk()
    window.title('Message Box')
    window.geometry('500x250')

    # this will be our command if the check box is acted on
    def isTrue():
        # here we are making the message box, with the title and message within
        if stateOfChk.get() == True:  # is checked do: popup box
            messagebox.showinfo("Pop up", "Warning you clicked the box")

    # this is a tkinter var type
    stateOfChk = t.BooleanVar()
    # we make that true
    stateOfChk.set(False)
    # when we put stateOfChk in as the var the box starts checked
    # if it were false it would start un checked
    # here we are making the check bos in our window with text "select me" and var state
    chk = ttk.Checkbutton(window, text="select me", var=stateOfChk, command=isTrue)
    chk.grid(column=0, row=0)
    window.mainloop()


def spinBox():
    window = t.Tk()
    window.title('Spin Box')
    window.geometry('500x250')
    spin = ttk.Spinbox(window, from_=0, to_=100, width=20)
    spin.pack()
    window.mainloop()


def main():
    intro()
    # buttons()
    # entry()
    # comboBox()
    # checkButton()
    # radioButton()
    # scrolledText()
    # messageBox()
    # spinBox()


if __name__ == '__main__':
    main()
