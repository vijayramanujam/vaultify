import tkinter as tk
from tkinter import messagebox
from fuzzywuzzy import fuzz
import pickle
import os
import secrets
import string
import pyperclip

# File to store the passwords
PASSWORD_FILE = "passwords.pkl"

# Load passwords from the pickle file
def load_passwords():
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "rb") as f:
            return pickle.load(f)
    return {}

# Save passwords to the pickle file
def save_passwords(passwords):
    with open(PASSWORD_FILE, "wb") as f:
        pickle.dump(passwords, f)

# Add a new password
def add_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if website == "" or username == "" or password == "":
        messagebox.showwarning("Input Error", "All fields are required")
        return

    passwords = load_passwords()
    passwords[website] = {"username": username, "password": password}
    save_passwords(passwords)

    website_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

    messagebox.showinfo("Success", f"Password for {website} saved successfully!")

# Show all saved passwords
def show_passwords():
    passwords = load_passwords()
    if not passwords:
        messagebox.showinfo("No Passwords", "No passwords stored yet.")
        return

    passwords_text.delete(1.0, tk.END)  # Clear existing text
    for website, credentials in passwords.items():
        passwords_text.insert(tk.END, f"Website: {website}\nUsername: {credentials['username']}\nPassword: {credentials['password']}\n\n")

# Perform fuzzy search on the saved websites
def search_passwords():
    query = search_entry.get()
    if not query:
        messagebox.showwarning("Input Error", "Please enter a website to search for.")
        return
    
    passwords = load_passwords()
    if not passwords:
        messagebox.showinfo("No Passwords", "No passwords stored yet.")
        return

    # Perform fuzzy search
    search_results = []
    for website in passwords.keys():
        ratio = fuzz.partial_ratio(query.lower(), website.lower())  # Case-insensitive search
        if ratio > 50:  # You can adjust the threshold value (50) based on your preference
            search_results.append(website)

    # Show search results
    if search_results:
        passwords_text.delete(1.0, tk.END)  # Clear existing text
        for website in search_results:
            credentials = passwords[website]
            passwords_text.insert(tk.END, f"Website: {website}\nUsername: {credentials['username']}\nPassword: {credentials['password']}\n\n")
    else:
        messagebox.showinfo("No Results", "No matching websites found.")

# Clear all input fields when Ctrl+C is pressed
def clear_fields(event=None):
    website_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    search_entry.delete(0, tk.END)  # Also clears the search field if needed

# Close the application
def close_application():
    root.quit()

# Function to generate a strong password
def generate_password():
    password_length = 16  # You can adjust the length of the password
    alphabet = string.ascii_letters + string.digits + string.punctuation  # Allowed characters
    password = ''.join(secrets.choice(alphabet) for i in range(password_length))
    password_entry.delete(0, tk.END)  # Clear current content in the password field
    password_entry.insert(0, password)  # Insert the generated password

# Function to set website entry from clipboard if available
def set_website_from_clipboard():
    clipboard_content = pyperclip.paste()  # Get content from clipboard
    if clipboard_content:
        website_entry.delete(0, tk.END)  # Clear any existing content
        website_entry.insert(0, clipboard_content)  # Insert clipboard content into website field

# Create the main window
root = tk.Tk()
root.title("Simple Password Manager")

# Set up a consistent padding for all widgets
root.option_add("*Font", "Arial 10")
padx = 10
pady = 5

# Set the window size and make it resizable
root.geometry("500x500")
root.resizable(False, False)

# Frame for inputs
frame_inputs = tk.Frame(root)
frame_inputs.grid(row=0, column=0, padx=padx, pady=pady, sticky="nsew")

# Website field (increase width)
website_label = tk.Label(frame_inputs, text="Website")
website_label.grid(row=0, column=0, padx=padx, pady=pady, sticky="w")
website_entry = tk.Entry(frame_inputs)
website_entry.grid(row=0, column=1, padx=padx, pady=pady, columnspan=2, sticky="ew")

# Username field (increase width)
username_label = tk.Label(frame_inputs, text="Username")
username_label.grid(row=1, column=0, padx=padx, pady=pady, sticky="w")
username_entry = tk.Entry(frame_inputs)
username_entry.grid(row=1, column=1, padx=padx, pady=pady, columnspan=2, sticky="ew")

# Password field and generate button
password_label = tk.Label(frame_inputs, text="Password")
password_label.grid(row=2, column=0, padx=padx, pady=pady, sticky="w")
password_entry = tk.Entry(frame_inputs, show="*")
password_entry.grid(row=2, column=1, padx=padx, pady=pady)

generate_button = tk.Button(frame_inputs, text="Generate", command=generate_password)
generate_button.grid(row=2, column=2, padx=padx, pady=pady)

# Search field for fuzzy search (limit width)
search_label = tk.Label(frame_inputs, text="Search Website")
search_label.grid(row=3, column=0, padx=padx, pady=pady, sticky="w")
search_entry = tk.Entry(frame_inputs)
search_entry.grid(row=3, column=1, padx=padx, pady=pady, sticky="ew")

# Search button for fuzzy search
search_button = tk.Button(frame_inputs, text="Search", command=search_passwords)
search_button.grid(row=3, column=2, padx=padx, pady=pady)

# Textbox to display passwords
passwords_text = tk.Text(root, height=10, width=55)
passwords_text.grid(row=1, column=0, padx=padx, pady=pady, sticky="nsew")

# Frame for buttons at the bottom
frame_buttons = tk.Frame(root)
frame_buttons.grid(row=2, column=0, padx=padx, pady=pady, sticky="ew")

# Add password button
add_button = tk.Button(frame_buttons, text="Add Password", command=add_password)
add_button.grid(row=0, column=0, padx=padx, pady=pady, sticky="ew")

# Show passwords button
show_button = tk.Button(frame_buttons, text="Show All Passwords", command=show_passwords)
show_button.grid(row=0, column=1, padx=padx, pady=pady, sticky="ew")

# Close button
close_button = tk.Button(frame_buttons, text="Close", command=close_application)
close_button.grid(row=0, column=2, padx=padx, pady=pady, sticky="ew")

# Bind Ctrl+C to the clear_fields function
root.bind("<Control-c>", clear_fields)

# Set website field from clipboard when the application starts
set_website_from_clipboard()

# Configure grid row and column weights
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=3)
root.grid_rowconfigure(2, weight=1)

root.grid_columnconfigure(0, weight=1)

# Start the Tkinter main loop
root.mainloop()

