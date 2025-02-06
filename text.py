import os
from tkinter import filedialog
import customtkinter as ctk
from TTS.api import TTS
from pypdf import PdfReader

class ConvertToAudioBook:
    def __init__(self, file, output_name, model, device="cpu"):
        self.file = file
        self.output_name = output_name
        self.model = model
        self.device = device

    def extract_text(self):
        reader = PdfReader(self.file)  # Read the PDF file
        number_of_pages = len(reader.pages)  # Get the number of pages
        text = []  # Use a list to accumulate text for better performance
        for page_number in range(number_of_pages):  # Iterate through pages
            page = reader.pages[page_number]
            text.append(page.extract_text())  # Extract text and add to the list
        return "".join(text)  # Combine the text into a single string

    def generate_audio(self):
        tts = TTS(model_name=self.model, progress_bar=True)
        tts.to(self.device)
        if self.file.endswith(".pdf"):
            text = self.extract_text()
            text = text.translate(str.maketrans('', '', "\u201c\u201d"))  # Remove special quotes
        else:
            text = self.file
        tts.tts_to_file(text=text, file_path=f"{self.output_name}.wav")

# GUI Implementation
class AudioBookApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("PDF to Audiobook Converter")
        self.geometry("600x430")
        self.file_path = None

        # Configure grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create a frame for better organization
        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)

        # Title Label
        self.label_title = ctk.CTkLabel(
            self.main_frame, 
            text="PDF to Audiobook Converter", 
            font=("Arial", 24, "bold"),
            text_color="#3b8ed0"
        )
        self.label_title.grid(row=0, column=0, pady=20, sticky="n")

        # Select File Button
        self.button_select_file = ctk.CTkButton(
            self.main_frame, 
            text="Select PDF File", 
            command=self.select_file, 
            corner_radius=8
        )
        self.button_select_file.grid(row=1, column=0, pady=10, sticky="ew", padx=50)

        # Selected File Label
        self.label_file = ctk.CTkLabel(
            self.main_frame, 
            text="No file selected", 
            wraplength=600, 
            font=("Arial", 12)
        )
        self.label_file.grid(row=2, column=0, pady=5, sticky="n")

        # Output File Name Entry
        self.entry_output_name = ctk.CTkEntry(
            self.main_frame, 
            placeholder_text="Output file name", 
            width=400, 
            height=40,
            corner_radius=8
        )
        self.entry_output_name.grid(row=3, column=0, pady=20, sticky="n")

        # TTS Model Selection Label and dropdown - Removed for now
        """ 
       self.label_model = ctk.CTkLabel(
            self.main_frame, 
            text="Select TTS Model", 
            font=("Arial", 14, "bold")
        )
        self.label_model.grid(row=4, column=0, pady=10, sticky="n")

        # TTS Model Dropdown 
         self.model_var = ctk.StringVar(value="tts_models/en/jenny/jenny")
        self.option_model = ctk.CTkOptionMenu(
            self.main_frame, 
            variable=self.model_var,
            values=[
                "tts_models/en/jenny/jenny",
                "tts_models/en/ljspeech/tacotron2-DCA",
                "tts_models/en/ljspeech/glow-tts"
            ],
            width=400,
            height=40,
            corner_radius=8
        )
        self.option_model.grid(row=5, column=0, pady=10, sticky="n") 
        """

        # Convert Button
        self.button_convert = ctk.CTkButton(
            self.main_frame, 
            text="Convert to Audiobook", 
            command=self.convert_to_audio, 
            height=50, 
            corner_radius=8,
            fg_color="#3b8ed0", 
            hover_color="#2a6caf"
        )
        self.button_convert.grid(row=6, column=0, pady=30, sticky="ew", padx=50)

        # Status Label
        self.label_status = ctk.CTkLabel(
            self.main_frame, 
            text="", 
            wraplength=600, 
            font=("Arial", 12),
            text_color="#3b8ed0"
        )
        self.label_status.grid(row=7, column=0, pady=0, sticky="n")

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            self.file_path = file_path
            self.label_file.configure(text=f"Selected file: {os.path.basename(file_path)}")
        else:
            self.label_file.configure(text="No file selected")

    def convert_to_audio(self):
        if not self.file_path:
            self.label_status.configure(text="Error: No file selected!", text_color="red")
            return

        output_name = self.entry_output_name.get()
        if output_name == "":
            self.label_status.configure(text="Error: Select a name for the output file!", text_color="red")
            return
            
        model_name = self.model_var.get()
        try:
            self.label_status.configure(text="Processing...", text_color="blue")
            self.update()

            converter = ConvertToAudioBook(
                file=self.file_path, output_name=output_name, model=model_name
            )
            converter.generate_audio()

            self.label_status.configure(text="Conversion complete! File saved.", text_color="green")
        except Exception as e:
            self.label_status.configure(text=f"Error: {str(e)}", text_color="red")

# Run the application
if __name__ == "__main__":
    ctk.set_appearance_mode("Dark")  # Set appearance mode
    ctk.set_default_color_theme("blue")  # Set color theme
    app = AudioBookApp()
    app.resizable(False, False)
    app.mainloop()