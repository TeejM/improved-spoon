from Tkinter import *

class GUITest2(Frame):
        def __init(self, master):
                Frame.__init__(self, master)
                self.master = master

        def setupGUI(self):
                # Make list of COLUMNS length
                columns = [str(c) for c in range(COLUMNS)]
                # Make list of ROWS length
                rows = [str(r) for r in range(ROWS)]
                
                # Generate key for each segment of grid
                # Connect each key to PhotoImage object
                photo = {i+str(j):PhotoImage(file="ia1.gif")\
                         for i in columns for j in rows}
                
                # Connect each key to Label object
                # Insert PhotoImage object to each Label
                grid = {k:Label(self.master, image=photo[k],\
                                width=WIDTH/COLUMNS,\
                                height=HEIGHT/ROWS)\
                                for i in columns for j in rows \
                                for k in sorted(photo)}

                # Name for PhotoObject key is the same as Label key
                for n,k in enumerate(sorted(grid)):
                        # Say Label key's image = name of PhotoObject key ?
                        grid[k].image = photo[k]
                        # Assign the row and column to each Label
                        grid[k].grid(row=n%len(rows), column=n/len(rows)%len(columns))
                        # Don't let image define Label size
                        grid[k].grid_propagate(False)

# Set values       
COLUMNS = 4
ROWS = 4
WIDTH = 800
HEIGHT = 480

# Run Tkinter
window = Tk()
t = GUITest2(window)
t.setupGUI()
window.mainloop()
