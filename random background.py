from tkinter import *
import random
root=Tk()
root.geometry("600x600")
root.title("Background Changer")

dictionary={"color":["maroon1","lawn green","magenta2","purple1","springgreen2","chocolate1", "deep pink","cyan"]}

def change():
    no=random.randint(0,7)
    root.configure(background=dictionary["color"][no])

btn=Button(root, text="Change", command=change)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()