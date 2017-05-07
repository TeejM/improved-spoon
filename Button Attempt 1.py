from Tkinter import *

window = Tk()

LeftFrame = Frame(window)
LeftFrame.pack(side=LEFT)
RightFrame = Frame(window)
RightFrame.pack(side=RIGHT)


def toggle():
    if B1.config("text")[-1] == "High":
        B1.config(text="Low")
    else:
        B1.config(text="High")

for i in range (1, 9):
    B = Button(LeftFrame, bg="white", text="High", height=3, width=5, command=lambda i=i: toggle())
    B.pack(anchor=W)



img = PhotoImage(file="map.gif")
Image = Label(RightFrame, image=img)
Image.pack(anchor=E)

window.mainloop()

