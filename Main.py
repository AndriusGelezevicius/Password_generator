import tkinter as tk
from tkinter import font


# Create the main window
root = tk.Tk()
root.title("Password generator")
root.geometry("400x450")
root.resizable(False, False)

# Main Label
custom_font = font.Font(size=12, weight="bold")
label = tk.Label(root, text="Password Generator", font=custom_font)
label.pack(pady=20)

# Frame of button and entry
frame = tk.Frame(root)
frame.pack(pady=10, padx=10)
# Showing password entry
password_show = tk.Entry(frame)
password_show.pack(side=tk.LEFT, padx=(20,20))

# Copy button
button_copy = tk.Button(frame, text="Copy", command="copy_password")
button_copy.pack(side=tk.LEFT)





root.mainloop()