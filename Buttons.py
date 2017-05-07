from Tkinter import *

window = Tk()

LeftFrame = Frame(window)
LeftFrame.pack(side=LEFT)
RightFrame = Frame(window)
RightFrame.pack(side=RIGHT)


def toggle(i):
    if Buttons[i].config("text")[-1] == "High":
        Buttons[i].config(text="Low")
    else:
        Buttons[i].config(text="High")


Buttons = {i: Button(LeftFrame, bg="white", text="High", height=3, width=5, command=lambda i=i: toggle(i)) for i in range (1, 9)}
for i in range(1, len(Buttons)+1):
    Buttons[i].grid(column=0, row=i+1)

# print Buttons[1]
img = PhotoImage(file="map.gif")
Image = Label(RightFrame, image=img)
Image.pack(anchor=E)

window.mainloop()
