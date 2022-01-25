import tkinter as tk

window = tk.Tk()


for i in range(3):
    window.columnconfigure(i, weight = i+1, minsize = 75)
    window.rowconfigure(i, weight = i+1, minsize = 75)


for row in range(3):
    for col in range(3):
        frame = tk.Frame(master = window, relief = tk.RAISED, borderwidth = 1)
        frame.grid(row=row, column = col, padx = 5, pady = 5)
        label = tk.Label(master = frame, text = f"{row}, {col}")
        label.pack()
        

window.mainloop()
