import tkinter as tk
from tkinter import font


# Create the main window
root = tk.Tk()
root.title("Password generator")
root.geometry("400x450")
root.resizable(False, False)

custum_font = font.Font(size = 12, weight="bold")
label = tk.Label(root, text="Password Generator", font=custum_font)
label.pack(pady = 20)








root.mainloop()