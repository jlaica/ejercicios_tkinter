import tkinter as tk

root = tk.Tk()
text = tk.Text(root)
text.pack()

def tab(arg):
    print("tab pressed")
    text.insert(tk.INSERT, " " * 4)
    return 'break'

text.bind("<Tab>", tab)
root.mainloop()
