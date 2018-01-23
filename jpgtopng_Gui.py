# tkinter trolling
from tkinter import *
from PIL import Image
import os

def click():
    entered_text=textentry.get()
    entered_name=textentry2.get()
    output.delete(0.0,END)
    try:
        imagedir = entered_text
        im = Image.open(imagedir)
        imagename = entered_name
        im.save(imagename+".png", "PNG")
    except:
        entered_text="No such image"


    output.insert(END,"File located at: " + os.path.abspath(imagename)+".png")
        

window = Tk()

window.title("PNG Image Converter")
window.configure(background="black")

Label(window, text="IMG Directory:", bg="black", fg="red", font="Tahoma 12 italic").grid(row=1,column=0,sticky=W)
textentry = Entry(window,width=20,bg="white")
textentry.grid(row=2,column=0,sticky=W)


Label(window, text="IMG Name You Want:", bg="black", fg="red", font="Tahoma 12 italic").grid(row=3,column=0,sticky=W)
textentry2 = Entry(window,width=40,bg="white")
textentry2.grid(row=4,column=0,sticky=W)

Button(window,text="Convert",width=6,command=click).grid(row=5,column=0,sticky=W)

Label(window,text="\n\nOutput:",bg="black",fg="red",font="Tahoma 12 italic").grid(row=7,column=0,sticky=W)

output = Text(window,width=50,height=6,wrap=WORD,background="blue")
output.grid(row=7,column=0,columnspan=2,sticky=W)

window.mainloop()
