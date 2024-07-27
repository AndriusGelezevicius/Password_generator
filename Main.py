import random
import string
import tkinter as tk
from tkinter import font

def copy_password():
    password_value = password_show.get()
    print(f"password is: {password_value}")

# Generate random character
def show_random_characters():
    scale_value = scale.get()
    random_characters = ''.join(random.choices(string.ascii_letters, k=scale_value))
    password_show.delete(0, tk.END)
    password_show.insert(0, random_characters)

# Create the main window
root = tk.Tk()
root.title("Password generator")
root.geometry("400x450")
#root.resizable(False, False)

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
button_copy = tk.Button(frame, text="Copy", command=show_random_characters)
button_copy.pack(side=tk.LEFT)


# Slider
slider_frame = tk.Frame(root)
slider_frame.pack(pady=10, padx=10)

slider_label = tk.Label(slider_frame, text="Password length: ")
slider_label.pack(side=tk.LEFT, padx=(20,20))

scale = tk.Scale(slider_frame, from_=5, to=40, orient="horizontal")
scale.pack(side=tk.LEFT)

# Combobox
combo_frame = tk.Frame(root)
combo_frame.pack(pady=10, padx=10)
combo_label = tk.Label(combo_frame, text="Characters used: ")
combo_label.pack(side=tk.LEFT, padx=(20,20))

check_vars =[]

checkbox_labels = ["ABC", "abc", "123", "#$&"]
for labels in checkbox_labels:
    check_var = tk.IntVar()  # Cinteger variable that Tkinter can use to track the state of the checkbox.
    check_vars.append(check_var)
    check_box = tk.Checkbutton(combo_frame, text=labels, variable=check_var)
    check_box.pack(side=tk.LEFT)



show_random_characters()
root.mainloop()