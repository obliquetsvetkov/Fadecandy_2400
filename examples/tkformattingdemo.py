import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(width = 100, height = 100, bg = 'green')
frame2 = tk.Frame(width = 20, height = 20, bg = 'red')
frame3 = tk.Frame(width = 50, height = 50, bg = 'blue')

frame1.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
frame2.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
frame3.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)

window.mainloop()
