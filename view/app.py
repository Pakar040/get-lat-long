from model.xml_manager import PoleDataWriter
import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog
from CTkMessagebox import CTkMessagebox


class App:
    def __init__(self, root):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.root = root
        self.root.geometry(f"{400}x{200}")
        self.root.title("Pole Lat and longs")
        self.directory = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        label = ctk.CTkLabel(self.root, text="Directory:")
        label.pack(padx=10, pady=5)

        entry = ctk.CTkEntry(self.root, textvariable=self.directory)
        entry.pack(padx=10, pady=5)

        browse_button = ctk.CTkButton(self.root, text="Browse", command=self.browse)
        browse_button.pack(padx=10, pady=5)

        run_button = ctk.CTkButton(self.root, text="Run", command=self.run)
        run_button.pack(padx=10, pady=5)

    def browse(self):
        self.directory.set(filedialog.askdirectory())

    def run(self):
        if self.directory.get():
            writer = PoleDataWriter(self.directory.get())
            writer.write_to_excel()
        CTkMessagebox(
            title='',
            message="Spreadsheet with latitudes an longitudes in folder",
            icon="check",
            option_1="Ok",
        )

