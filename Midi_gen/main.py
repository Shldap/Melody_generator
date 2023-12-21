import tkinter as tk
from tkinter import filedialog
import pretty_midi
import logic

class MidiGeneratorGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MIDI Generator")
        self.geometry("300x150")

        self.source_midi = None

        self.btn_select_source_midi = tk.Button(
            self,
            text="Select Source MIDI",
            command=self.select_source_midi
        )
        self.btn_select_source_midi.pack(pady=10)

        self.btn_generate_midi = tk.Button(
            self,
            text="Generate MIDI",
            state=tk.DISABLED,
            command=self.generate_midi
        )
        self.btn_generate_midi.pack(pady=10)

    def select_source_midi(self):
        self.source_midi = filedialog.askopenfilename(
            initialdir="/",
            title="Select Source MIDI",
            filetypes=(("MIDI files", "*.mid"), ("all files", "*.*"))
        )

        if self.source_midi:
            self.btn_generate_midi.config(state=tk.NORMAL)

    def generate_midi(self):
        # Generate the MIDI data
        midi_data = logic.generate_midi(self.source_midi)

        # Save the generated MIDI file
        save_path = filedialog.asksaveasfilename(
            initialdir="/",
            title="Save Generated MIDI",
            filetypes=(("MIDI files", "*.mid"), ("all files", "*.*"))
        )
        if save_path:
            midi_data.write(save_path)

if __name__ == "__main__":
    app = MidiGeneratorGUI()
    app.mainloop()
