import random
import string
import tkinter as tk
from tkinter import font, ttk

def copy_password():
    password_value = password_show.get()
    # Clear the clipboard and append the new value
    root.clipboard_clear()
    root.clipboard_append(password_value)
    root.update()

# Generate random character
def show_random_characters():
    scale_value = scale.get()
    random_characters = ''.join(random.choices(string.ascii_letters, k=scale_value))
    password_show.delete(0, tk.END)
    password_show.insert(0, random_characters)

def checkbox_state(*args): # *args allows the function to accept any number of positional arguments, which is useful because the Scale widget provides an argument to its command callback.
    scale_value = scale.get()
    selected_characters =[]

    if check_vars[0].get():# extend(): Adds characters to the selected_characters list based on which checkboxes are checked.
        selected_characters.extend(string.ascii_uppercase)
    if check_vars[1].get():
        selected_characters.extend(string.ascii_lowercase)
    if check_vars[2].get():
        selected_characters.extend(string.digits)
    if check_vars[3].get():
        selected_characters.extend(string.punctuation)

    if selected_characters:
        random_characters = ''.join(random.choices(selected_characters, k=scale_value))
        password_show.delete(0, tk.END) # Clear the current entry
        password_show.insert(0, random_characters)
# Create the main window
root = tk.Tk()
root.title("Password generator")
root.geometry("400x450")

# Main Label
custom_font = font.Font(size=12, weight="bold")
label = tk.Label(root, text="Password Generator", font=custom_font)
label.pack(pady=20)

# Frame of button and entry
frame = ttk.Frame(root)
frame.pack(pady=10, padx=10)
# Showing password entry
password_show = ttk.Entry(frame)
password_show.pack(side=tk.LEFT, padx=(20,20))

# Copy button
button_copy = ttk.Button(frame, text="Copy", command=copy_password)
button_copy.pack(side=tk.LEFT)


# Slider
slider_frame = ttk.Frame(root)
slider_frame.pack(pady=10, padx=10)

slider_label = ttk.Label(slider_frame, text="Password length: ")
slider_label.pack(side=tk.LEFT, padx=(20,20))

scale = tk.Scale(slider_frame, from_=5, to=40, orient="horizontal", command=checkbox_state)
scale.pack(side=tk.LEFT)

# Combobox
combo_frame = ttk.Frame(root)
combo_frame.pack(pady=10, padx=10)
combo_label = ttk.Label(combo_frame, text="Characters used: ")
combo_label.pack(side=tk.LEFT, padx=(20,20))

check_vars =[]

checkbox_labels = ["ABC", "abc", "123", "#$&"]
for labels in checkbox_labels:
    check_var = tk.IntVar(value=1)  # integer variable that Tkinter can use to track the state of the checkbox.
    check_vars.append(check_var)
    check_box = ttk.Checkbutton(combo_frame, text=labels, variable=check_var, command=checkbox_state)
    check_box.pack(side=tk.LEFT)

show_random_characters()
root.mainloop()