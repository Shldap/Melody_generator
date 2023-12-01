import tkinter as tk
from tkinter import messagebox
from melody_generator import generate_melody

# Create the GUI
window = tk.Tk()
window.title("Melody Generator")

# Melody length label and entry field
melody_length_label = tk.Label(window, text="Melody Length:")
melody_length_label.pack()
melody_length = tk.IntVar(value=8)
melody_length_entry = tk.Entry(window, textvariable=melody_length)
melody_length_entry.pack()

# Mood selection dropdown
mood_label = tk.Label(window, text="Select Mood:")
mood_label.pack()
moods = ["happy", "sad", "calm", "rnb", "drill", "hip-hop","metro_boomin"]
mood_selection = tk.StringVar(value="happy")
mood_dropdown = tk.OptionMenu(window, mood_selection, *moods)
mood_dropdown.pack()

# Generate button
generate_button = tk.Button(window, text="Generate Melody", command=generate_melody)
generate_button.pack()

# Run the GUI
window.mainloop()
