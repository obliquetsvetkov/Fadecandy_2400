import tkinter as tk

window = tk.Tk() #object that is root window
window.title('TKInter hello world')

text = tk.Label(text = "What's your name?", foreground = 'white',
                background = 'blue', width = 30, height = 3)
text.pack()

entry = tk.Entry(width = 30)
entry.pack()

def save_and_print():
    name = entry.get() #denis, type 'string'
    entry.delete(0, tk.END)
    print(name)

button = tk.Button(text = 'Submit', width = 30, height = 5,
                   command = save_and_print)
button.pack(padx = 5, pady = 5)

#window.bind('<Return>', command = save_and_print)
window.bind('<Return>', lambda event:save_and_print()) #if func need parameters

window.mainloop() # start event loop, method on top of 'window'
