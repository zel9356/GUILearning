import tkinter as t
from PIL import ImageTk, Image

window = t.Tk()
window.title("GUI with Images")
window.geometry("500x500")
img = ImageTk.PhotoImage(file="C3C17.tiff")  # this ImageTK allows us to use tiffs
label = t.Label(window, image=img, height=378, width=504)
label.pack()
window.mainloop()
