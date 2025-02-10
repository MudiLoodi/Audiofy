"""
GUI implementation for the Audiofy application.
Provides a user-friendly interface for PDF to audio conversion.
"""

import os
from tkinter import filedialog
import customtkinter as ctk
from utils.converter import AudioConverter
from config.settings import *

class AudioBookApp(ctk.CTk):
    """
    Main application window for the PDF to Audiobook converter.
    Handles user interaction and coordinates conversion process.
    """

    def __init__(self):
        """Initialize the application window and setup UI components."""
        super().__init__()
        self.setup_window()
        self.create_widgets()
        self.file_path = None

    def setup_window(self):
        """Configure the main window properties and layout."""
        self.title("PDF to Audiobook Converter")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def create_widgets(self):
        """Create and initialize all UI widgets."""
        self._create_main_frame()
        self._create_title()
        self._create_file_selection()
        self._create_output_entry()
        self._create_convert_button()
        self._create_status_label()

    def _create_main_frame(self):
        """Create the main container frame for all widgets."""
        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.grid(row=0, column=0, padx=PADDING, pady=PADDING, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)

    def _create_title(self):
        """Create the application title label."""
        self.label_title = ctk.CTkLabel(
            self.main_frame, 
            text="PDF to Audiobook Converter", 
            font=("Arial", 24, "bold"),
            text_color=PRIMARY_COLOR
        )
        self.label_title.grid(row=0, column=0, pady=PADDING, sticky="n")

    def _create_file_selection(self):
        """Create file selection button and selected file label."""
        self.button_select_file = ctk.CTkButton(
            self.main_frame, 
            text="Select PDF File", 
            command=self.select_file, 
            corner_radius=8
        )
        self.button_select_file.grid(row=1, column=0, pady=10, sticky="ew", padx=50)

        self.label_file = ctk.CTkLabel(
            self.main_frame, 
            text="No file selected", 
            wraplength=WINDOW_WIDTH, 
            font=("Arial", 12)
        )
        self.label_file.grid(row=2, column=0, pady=5, sticky="n")

    def _create_output_entry(self):
        """Create entry field for output filename."""
        self.entry_output_name = ctk.CTkEntry(
            self.main_frame, 
            placeholder_text="Output file name", 
            width=ENTRY_WIDTH, 
            height=ENTRY_HEIGHT,
            corner_radius=8
        )
        self.entry_output_name.grid(row=3, column=0, pady=PADDING, sticky="n")

    def _create_convert_button(self):
        """Create the main conversion action button."""
        self.button_convert = ctk.CTkButton(
            self.main_frame, 
            text="Convert to Audiobook", 
            command=self.convert_to_audio, 
            height=BUTTON_HEIGHT, 
            corner_radius=8,
            fg_color=PRIMARY_COLOR, 
            hover_color=HOVER_COLOR
        )
        self.button_convert.grid(row=6, column=0, pady=30, sticky="ew", padx=50)

    def _create_status_label(self):
        """Create label for displaying conversion status and errors."""
        self.label_status = ctk.CTkLabel(
            self.main_frame, 
            text="", 
            wraplength=WINDOW_WIDTH, 
            font=("Arial", 12),
            text_color=PRIMARY_COLOR
        )
        self.label_status.grid(row=7, column=0, pady=0, sticky="n")

    def select_file(self):
        """
        Handle file selection via dialog.
        Updates UI to show selected filename.
        """
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            self.file_path = file_path
            self.label_file.configure(text=f"Selected file: {os.path.basename(file_path)}")
        else:
            self.label_file.configure(text="No file selected")

    def convert_to_audio(self):
        """
        Handle the PDF to audio conversion process.
        Validates input, shows progress, and handles errors.
        """
        if not self.file_path:
            self.label_status.configure(text="Error: No file selected!", text_color=ERROR_COLOR)
            return

        output_name = self.entry_output_name.get()
        if not output_name:
            self.label_status.configure(text="Error: Select a name for the output file!", text_color=ERROR_COLOR)
            return

        try:
            self.label_status.configure(text="Processing...", text_color=PROCESSING_COLOR)
            self.update()

            converter = AudioConverter(
                file=self.file_path,
                output_name=output_name,
                model=DEFAULT_MODEL,
                device=DEFAULT_DEVICE
            )
            converter.convert()

            self.label_status.configure(text="Conversion complete! File saved.", text_color=SUCCESS_COLOR)
        except Exception as e:
            self.label_status.configure(text=f"Error: {str(e)}", text_color=ERROR_COLOR)
