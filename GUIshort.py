from Tkinter import *

class GUITest2(Frame):
        def __init(self, master):
                Frame.__init__(self, master)
                self.master = master

        def setupGUI(self):
                columns = [str(c) for c in range(COLUMNS)]
                rows = [str(r) for r in range(ROWS)]
                photo = {i+str(j):PhotoImage(file="ia1.gif") for i in columns for j in rows}
                grid = {k:Label(self.master, image=photo[k], width=WIDTH/COLUMNS, \
                                       height=HEIGHT/ROWS) for i in columns for j in rows \
                                       for k in sorted(photo)}
                for n,k in enumerate(sorted(grid)):
                        grid[k].image = photo[k]
                        grid[k].grid(row=n%len(rows), column=n/len(rows)%len(columns))
                        grid[k].grid_propagate(False)

                
COLUMNS = 4
ROWS = 4
WIDTH = 800
HEIGHT = 600
window = Tk()
t = GUITest2(window)
t.setupGUI()
window.mainloop()
