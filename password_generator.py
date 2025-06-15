import tkinter as tk
from tkinter import ttk
import random
import string

# Function to generate password
def generate_password():
    length = password_length_slider.get()  # Get value from the slider
    include_symbols = var_symbols.get()
    include_numbers = var_numbers.get()

    # Define characters to include
    characters = string.ascii_letters  # Letters (both uppercase and lowercase)

    if include_symbols:
        characters += string.punctuation  # Add symbols
    if include_numbers:
        characters += string.digits  # Add numbers

    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))

    # Update the password entry field with the generated password
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)

# Setting up the main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x450")  # Adjusted size for better layout
window.config(bg="navy blue")  # Background color

# Add a title label with some styling
title_label = tk.Label(window, text="Password Generator", font=("Helvetica", 18, "bold"), bg="yellow")
title_label.pack(pady=20)

# Label and range slider for password length
label_length = tk.Label(window, text="Password Length:", font=("Helvetica", 12), bg="gray")
label_length.pack(pady=5)

# Range slider for password length (from 8 to 20)
password_length_slider = tk.Scale(window, from_=8, to=20, orient="horizontal", length=300, font=("Helvetica", 12), sliderlength=20, showvalue=1, bg="gray", troughcolor="gray", highlightthickness=0)
password_length_slider.set(12)  # Set default value
password_length_slider.pack(pady=10)

# Define Boolean variables for checkbox states
var_symbols = tk.BooleanVar()
var_numbers = tk.BooleanVar()

# Stylish Checkbuttons using ttk for modern look
check_symbols = ttk.Checkbutton(window, text="Include Symbols", variable=var_symbols, style="TCheckbutton")
check_symbols.pack(pady=5)

check_numbers = ttk.Checkbutton(window, text="Include Numbers", variable=var_numbers, style="TCheckbutton")
check_numbers.pack(pady=5)

# Function to create rounded button using tk.Button
def create_rounded_button(parent, text, command):
    # Use tk.Button for full control over appearance
    button = tk.Button(parent, text=text, command=command, font=("Helvetica", 12, "bold"), bg="gray", fg="white", relief="flat", height=2, width=20, bd=0)
    
    # Apply custom styling to create rounded corners
    button.config(borderwidth=0, highlightthickness=0)
    button.pack(pady=20)

    return button

# Use the function to create the rounded button
create_rounded_button(window, "Generate Password", generate_password)

# Entry field to display the generated password
label_password = tk.Label(window, text="Generated Password:", font=("Helvetica", 12), bg="yellow")
label_password.pack(pady=5)

entry_password = tk.Entry(window, font=("Helvetica", 12), width=30, bd=2, relief="solid", fg="#333333")
entry_password.pack(pady=10)

# Style the Checkbuttons using ttk theme
style = ttk.Style()
style.configure("TCheckbutton", font=("Helvetica", 12), background="yellow", foreground="#333333", padding=10)

# Run the Tkinter event loop
window.mainloop()