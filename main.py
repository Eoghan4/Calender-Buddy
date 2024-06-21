# Calender Buddy is not associated with Primark, Pennneys or any other company.
# Created by Eoghan McGough


import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

from get_time import get_time
from read_excel import get_row, get_times
from logic import main


# Function to be called when the button is clicked
def on_button_click():
    text1 = textbox1.get()  # Get text from the first Entry widget
    text2 = textbox2.get()  # Get text from the second Entry widget
    #print(f"Textbox 1: {text1}")  # Print the content of the first textbox
    #print(f"Textbox 2: {text2}")  # Print the content of the second textbox
    main(text2,text1)

def on_button2_click():
    text1 = textbox3.get()  # Get text from the first Entry widget  # Get text from the second Entry widget
    #print(f"Textbox 1: {text1}")  # Print the content of the first textbox
    #print(f"Textbox 2: {text2}")  # Print the content of the second textbox
    main(text1)

# Function to add placeholder text
def add_placeholder(entry, placeholder):
    entry.insert(0, placeholder)
    entry.bind("<FocusIn>", lambda event: clear_placeholder(entry, placeholder))
    entry.bind("<FocusOut>", lambda event: restore_placeholder(entry, placeholder))

# Function to clear placeholder text
def clear_placeholder(entry, placeholder):
    if entry.get() == placeholder:
        entry.delete(0, tk.END)
        entry.config(fg='black')

# Function to restore placeholder text
def restore_placeholder(entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.config(fg='grey')

# Create the main window
root = tk.Tk()
root.title("Calender Buddy")
root.geometry("500x400")  # Set the window size to 500x500 pixels

icon_path = "icon.png"
icon_image = Image.open(icon_path)
icon_photo = ImageTk.PhotoImage(icon_image)
root.iconphoto(False, icon_photo)

image_path = "Logo.png"
original_image = Image.open(image_path)
resized_image = original_image.resize((200, 30))  # Resize to 100x100 pixels
image = ImageTk.PhotoImage(resized_image)

image_label = tk.Label(root, image=image)
image_label.pack(pady=10)



# Create a label above the first textbox with larger font
label = tk.Label(root, text="Calender Buddy (Staff)", font=("Helvetica", 16))
label.pack(pady=1)

label2 = tk.Label(root, text="Add Colleague to Database", font=("Helvetica", 10))
label2.pack(pady=20)

# Create the first Entry (single-line textbox) with a placeholder
textbox1 = tk.Entry(root, width=40, fg='grey')
textbox1.pack(pady=5)
add_placeholder(textbox1, "Colleague name (As it appears on the roster)")

# Create the second Entry (single-line textbox) with a placeholder
textbox2 = tk.Entry(root, width=40, fg='grey')
textbox2.pack(pady=5)
add_placeholder(textbox2, "Colleague email")

# Create a button
button = tk.Button(root, text="Enter", command=on_button_click)
button.pack(pady=10)


label3 = tk.Label(root, text="Add Roster to Calenders", font=("Helvetica", 10))
label3.pack(pady=20)

# Create the first Entry (single-line textbox) with a placeholder
textbox3 = tk.Entry(root, width=40, fg='grey')
textbox3.pack(pady=5)
add_placeholder(textbox3, "Roster Directory")


# Create a button
button2 = tk.Button(root, text="Run", command=on_button2_click)
button2.pack(pady=10)

# Run the main event loop
root.mainloop()
