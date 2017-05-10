from Tkinter import *

class Game(Frame):
    # Constructor for Frame from Tkinter library
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        # Binds the key enter to the quit() method
        self.master.bind("<Escape>", self.quit)
        
    # Command to prepare screen for each puzzle
    def setupGUI(self, BUTTONS, COLUMNS, ROWS, WIDTH, HEIGHT):
    # set up buttons
        # Generate a PhotoObject; default is off
        bphoto = PhotoImage(file="OffButton.gif")
        # Create key for each Button; setter value tracks off/on status;
        setter = {i : 0 for i in range(BUTTONS) }
        # Generate each Button; pass in PhotoObject; give toggle() command
        Buttons = {i : Button(self.master, image=bphoto
                                      # Consider Buttons as a column; give extra space between rows
                      , width=WIDTH/10, height=HEIGHT/(BUTTONS+1)
                      # Pass through required values for toggle() to work
                      , command=lambda i=i: toggle(i, bphoto, setter, Buttons)
                    )
            # Share each setter key with each Button object
               for i in sorted(setter)
               }
        # Format each Button via shared key
        for i in range(0, len(Buttons)):
            Buttons[i].image = bphoto
            # Buttons have same column but consecutive rows
            Buttons[i].grid(row=i, column=0)
            # Don't let image define Button size
            Buttons[i].grid_propagate(False)
            # Make Buttons rowspan larger if multiple Labels
            if (ROWS > BUTTONS): Buttons[i].grid(rowspan=ROWS/BUTTONS+1)

    # set up labels
        columns = [str(c) for c in range(COLUMNS)]
        rows = [str(r) for r in range(ROWS)]
        # Generate and create key for each PhotoObject
        ''' Notice PhotoObject naming convention of column + row +".gif" '''
        photo = {c+r : PhotoImage(file="Puzzle1.gif")
             # Number is based off COLUMNS and ROWS
             for c in columns for r in rows
             }
        # Create and insert PhotoImage object to each Label
        label = {k : Label(self.master, image=photo[k]
                                # Consider Buttons as a column
                , width=(WIDTH-WIDTH/10)/COLUMNS
                , height=HEIGHT/ROWS
                 )
                # Share each PhotoObject key with each Label object
                for k in sorted(photo)
             }
        # Format each Label via shared key; enumerate to return index of key
        for n,k in enumerate(sorted(label)):
            label[k].image = photo[k]
            # Assign row going down then column going right with enumerate
            label[k].grid(row=n%len(rows)
                      , column=n/len(rows)%len(columns)+1)
            # Don't let image define Label size
            label[k].grid_propagate(False)
            # Make Labels rowspan larger if multiple Buttons
            if (BUTTONS > ROWS): label[k].grid(rowspan=BUTTONS/ROWS)
    # Quits the program, currently configured to Escape in the constructor
    def quit(self,event):
        self.master.destroy()

# Toggle accepts the shared key, bphoto, setter, and Buttons 
def toggle(i, bphoto, setter, Buttons):
    # Create a PhotoObject for buttons with on status
    On = PhotoImage(file="OnButton.gif")
    # Use existing PhotoObject for off status
    Off = bphoto
    # If on status when called, change photo and status to off
    if  (setter[i] == 1):
        Buttons[i].config(image=Off)
        Buttons[i].image = Off
        setter[i] = 0
    # If off status when called, change photo and status to on
    else:
        Buttons[i].config(image=On)
        Buttons[i].image = On
        setter[i] = 1

# Run Tkinter
window = Tk()
# Figure out screen dimensions
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
# Make window full screen
window.overrideredirect(1)
frame = Game(window)
''' input for each puzzle formatted as setupGUI(BUTTONS, COLUMNS, ROWS, WIDTH, HEIGHT)'''
frame.setupGUI(8,1,1,800,480)
window.mainloop()
