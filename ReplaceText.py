#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk

def apply_replacements():
    # Get the replacement rules and text from the entry fields
    rules_str = rules_entry.get()
    text = text_entry.get("1.0", tk.END)
    
    # Process the replacement rules
    rules = rules_str.split('][')
    for rule in rules:
        rule = rule.replace('[', '').replace(']', '')
        if '>' in rule:
            old, new = rule.split('>')
            text = text.replace(old, new)
    
    # Clear the text field and insert the modified text
    text_entry.delete("1.0", tk.END)
    text_entry.insert("1.0", text)

def populate_rules():
    # Define the rules based on the dropdown selection
    rules_options = {
        "Czech ASCII Alternatives": "[č>c][Č>C][š>s][Š>S][ž>z][Ž>Z][ř>r][Ř>R][ť>t][Ť>T][ď>d][Ď>D][ň>n][Ň>N][ů>u][Ú>U][á>a][Á>A][é>e][É>E][í>i][Í>I][ó>o][Ó>O][ú>u][Ú>U][ý>y][Ý>Y][ě>e][Ě>E]",
        "Replace with ?": "[č>?][Č>?][š>?][Š>?][ž>?][Ž>?][ř>?][Ř>?][ť>?][Ť>?][ď>?][Ď>?][ň>?][Ň>?][ů>?][Ú>?][á>?][Á>?][é>?][É>?][í>?][Í>?][ó>?][Ó>?][ú>?][Ú>?][ý>?][Ý>?][ě>?][Ě>?]"
    }
    selected_option = rules_var.get()
    rules_entry.delete(0, tk.END)  # Clear the field first
    rules_entry.insert(0, rules_options[selected_option])  # Populate with the selected rules

# Create the main window
root = tk.Tk()
root.title("Text Replacement Tool")

# Create a large text field
text_entry = tk.Text(root, height=15, width=50)
text_entry.pack(pady=10)

# Create a small field for replacement rules
rules_entry = tk.Entry(root)
rules_entry.pack(pady=5)

# Create a button to apply replacements
apply_button = tk.Button(root, text="Apply Replacements", command=apply_replacements)
apply_button.pack(pady=5)

# Separator (Horizontal Line)
separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x', padx=5, pady=5)

# Dropdown menu for rule selection
rules_var = tk.StringVar(root)
rules_var.set("ASCII Alternatives")  # default value
rules_dropdown = tk.OptionMenu(root, rules_var, "ASCII Alternatives", "Replace with ?")
rules_dropdown.pack(pady=5)

# Create a button to populate the rules field based on the selection
populate_button = tk.Button(root, text="Populate Rules", command=populate_rules)
populate_button.pack(pady=5)



# Run the application
root.mainloop()
