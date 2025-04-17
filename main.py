import customtkinter as ctk
from gui.app import AudioBookApp

if __name__ == "__main__":
    ctk.set_appearance_mode("Dark")  # Set dark mode for better visibility
    ctk.set_default_color_theme("blue")  # Use blue theme for consistency
    app = AudioBookApp()
    app.mainloop()
