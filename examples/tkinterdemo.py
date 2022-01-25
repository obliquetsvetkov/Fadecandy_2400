import tkinter as tk

window = tk.Tk() #object that is root window
window.title('TKInter hello world')

text = tk.Label(text = 'Hello world')
text2 = tk.Label(text = 'two')
text3 = tk.Label(text = 'three')

text.pack()
text2.pack()
text3.pack()

window.mainloop() # start event loop, method on top of 'window'
