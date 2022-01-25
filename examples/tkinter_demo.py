#tkinter stuff:
import tkinter as tk #shorter name to use for all the methods

window = tk.Tk() #main window object - this will generate the window for our gui.
#the window is just a container for widgets.

#frame = ttk.Frame(window, padding = 10) #set a frame inside so we can lay stuff out better
#frame.grid() #set a grid 
# 1st parameter: the window object we want the frame on; padding: 10 pixels on each side.

#-----------------------------------------------------------------------------------------------------------
#WIDGETS:
text = tk.Label(text = 'hello world', foreground = "white", background = 'black') #make a Label type widget (interactable element)
#1st parameter(compulsory): text to show; other parameters(optional): colours, fonts, size(IN CHARACTERS, NOT PIXELS), etc.
#for colours, hex RGB values work too, ex. "#34A2FE". fg and bg - shortened versions.
#widgets have config dictionaries - print the keys to see all available parameters: print(text.configure().keys()

label = tk.Label(text = 'input name:') #context for the below
entry = tk.Entry(width = 50) # text input from the user. Saved, but not used yet.

name = entry.get() #stores the entry text inside a variable to be used.
entry.delete(0, tk.END) #wipe the entire entry box. The indexing here works the same as in slicing operations.
#these two won't work as intended unless it's run from inside a widget (like a button)

def function(): #define a function that does something useful. read lines below.
    name = entry.get() #get data
    entry.delete(0, tk.END) #wipe the entry form (optional)
    print(name) #print data

button = tk.Button(text = 'click me!', width =25, height = 5, command = function)
#the command parameter names a callback function to be run when the button is pressed. What are callbacks again?


#alternatively, bind keyboard buttons:
window.bind('<Return>',lambda event:function())

#-----------------------------------------------------------------------------------------------------------
#GEOMETRY MANAGERS:
#pack - will try to pack everything in a column, the way they are ordered in code, and wrap the window as tightly as possible
#text.pack() #place the widgets on the window (fit the widget in and resize the window to it)
#button.pack()
#label.pack()
#entry.pack()

#frame - a frame is a container, contained inside the window. Each window and frame can use different geometry managers.
frame = tk.Frame(master = window) #make the frame in the window (window is the variable name used above)
frame_label = tk.Label(master=frame, text='Frame!') #place a label associated to the frame

#grid - instead of packing everything on top of each other, grid allows arrangement.
frame.columnconfigure(0, weight = 1) #set column 1
frame.columnconfigure(1, weight = 1) #set column 2. Play around with the weight variable!
#same can be used for rows: frame.rowconfigure(...)
#lists are encouraged: frame.columnconfigure([0,1,2], minsize = 50, weight = 1)

#each widget can only be placed once, so we'll have to comment out the above .pack() placements in order to use these .grid ones:
#text.grid(column = 0, row = 0, padx = 5, pady = 5)
#button.grid(column = 0, row = 1, padx = 5, pady = 5)
#label.grid(column = 1, row = 0, padx = 5, pady = 5)
#entry.grid(column = 1, row = 1, padx = 5, pady = 5)

#the sticky parameter: allows you to 'stick' an object to a particular location of the window(or grid cell) based on cardinal directions.
#n, e, s, w, ne, se, nw, sw. to fill an entire cell from a grid, use 'nsew'.
text.grid(column = 0, row = 0, padx = 5, pady = 5, sticky = 'n')
button.grid(column = 0, row = 1, padx = 5, pady = 5, sticky = 'nsew')
label.grid(column = 1, row = 0, padx = 5, pady = 5, sticky = 'se')
entry.grid(column = 1, row = 1, padx = 5, pady = 5, sticky = 'sw')

window.mainloop() #start the tkinter event loop.
# nothing can run after the mainloop, unless it's called from a widget!
