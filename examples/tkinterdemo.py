import tkinter as tk

window = tk.Tk() #object that is root window
window.title('TKInter hello world')

text = tk.Label(text = "What's your name?", foreground = 'white',
                background = 'blue', width = 30, height = 3)
#text.pack()

entry = tk.Entry(width = 30)
#entry.pack()

def save_and_print():
    name = entry.get() #denis, type 'string'
    entry.delete(0, tk.END)
    print(name)

button = tk.Button(text = 'Submit', width = 30, height = 5,
                   command = save_and_print)
#button.pack(padx = 5, pady = 5)

window.bind('<Return>', lambda event:save_and_print()) #if func need parameters

frame = tk.Frame(master = window)
label = tk.Label(master = window, text = 'Frame!', bg = 'black', fg = 'white')

frame.columnconfigure(0, weight = 1)
frame.columnconfigure(1, weight = 3)

text.grid(column = 0, row = 0, padx = 5, pady = 5, sticky = 'n')
entry.grid(column = 0, row = 1, padx = 5, pady = 5, sticky = 's')
button.grid(column = 1, row = 0, padx = 5, pady = 5, sticky = 'se')
label.grid(column = 1, row = 1, padx = 5, pady = 5, sticky = 'nsew')

window.mainloop() # start event loop, method on top of 'window'
