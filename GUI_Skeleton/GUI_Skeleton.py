from Tkinter import *

class Game(Frame):
    # Constructor for Frame from Tkinter library
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        # Binds the key enter to the quit() method
        self.master.bind("<Escape>", self.quit)
        self.master.bind("<Return>", self.process)
        self.master.minsize(width=800, height=480)
        self.text = Label(self.master, text="Congratulations on being selected for the job! \n \
Our Boebot has broken down and you must repair it! \n \
Your task is to complete the following logic circuits by turning the available inputs on or off.")
        self.text.pack(side=TOP)
        self.begin = Button(self.master, text="Begin", command=lambda: self.setupGUI(8,1,1,800,480))
        self.begin.pack(side=BOTTOM)
        self.puzzle = "Puzzle1.gif"
    # Command to prepare screen for each puzzle
    def setupGUI(self, BUTTONS, COLUMNS, ROWS, WIDTH, HEIGHT):
    # set up buttons
        self.text.pack_forget()
        self.begin.pack_forget()
        # Generate a PhotoObject; default is off
        bphoto = PhotoImage(file="OffButton.gif")
        # Create key for each Button; setter value tracks off/on status;
        global setter
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
        photo = {c+r : PhotoImage(file=self.puzzle)
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
    def process(self, event):
        if (self.puzzle == "Puzzle1.gif" and setter[0] == 1 and setter[1] == 0 and setter[2] == 1 and setter[3] == 0 and setter[4] == 1 and setter[5] == 0 and setter[6] == 1 and setter[7] == 1):
            self.puzzle = "Puzzle2.gif"
            frame.setupGUI(8,1,1,800,480)
        elif (self.puzzle == "Puzzle2.gif" and setter[0] == 1 and setter[1] == 0 and setter[2] == 1 and setter[3] == 1 and setter[4] == 0 and setter[5] == 1 and setter[6] == 1 and setter[7] == 0):
            self.puzzle = "Puzzle3.gif"
            frame.setupGUI(8,1,1,800,480)
        elif (self.puzzle == "Puzzle3.gif" and setter[0] == 0 and setter[1] == 1 and setter[2] == 1 and setter[3] == 1 and setter[4] == 0 and setter[5] == 1 and setter[6] == 1 and setter[7] == 1):
            self.puzzle = "Puzzle4.gif"
            frame.setupGUI(8,1,1,800,480)
        elif (self.puzzle == "Puzzle4.gif" and setter[0] == 1 and setter[1] == 0 and setter[2] == 1 and setter[3] == 1 and setter[4] == 0 and setter[5] == 1 and setter[6] == 0 and setter[7] == 0):
            self.puzzle = "Win.gif"
            frame.setupGUI(8,1,1,800,480)
    # Quits the program, currently configured to Escape in the constructor
    def quit(self, event):
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


###########################################################################


# Run Tkinter
window = Tk()
# Figure out screen dimensions
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
# Make window full screen
window.overrideredirect(1)
frame = Game(window)
''' input for each puzzle formatted as setupGUI(BUTTONS, COLUMNS, ROWS, WIDTH, HEIGHT)'''
#frame.setupGUI(8,1,1,800,480)
window.mainloop()
