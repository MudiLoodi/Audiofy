"""
Core functionality for converting PDF documents to audio files.
Handles text extraction, cleaning, and TTS conversion.
"""

from TTS.api import TTS
from pypdf import PdfReader

class AudioConverter:
    """
    Handles the conversion of PDF documents to audio files using TTS.
    
    Attributes:
        file (str): Path to the input PDF file
        output_name (str): Desired name for the output audio file
        model (str): Name of the TTS model to use
        device (str): Device to run TTS on (cpu/cuda)
    """

    def __init__(self, file, output_name, model, device):
        self.file = file
        self.output_name = output_name
        self.model = model
        self.device = device

    def _extract_text(self):
        """
        Extracts text from PDF file.
        
        Returns:
            str: Concatenated text from all pages
        """
        reader = PdfReader(self.file)
        return "".join(page.extract_text() for page in reader.pages)

    def _clean_text(self, text):
        """
        Removes special characters that might interfere with TTS.
        
        Args:
            text (str): Raw text from PDF
            
        Returns:
            str: Cleaned text ready for TTS
        """
        return text.translate(str.maketrans('', '', "\u201c\u201d"))

    def convert(self):
        """
        Converts the PDF text to audio using the specified TTS model.
        Saves the result as a WAV file.
        
        Raises:
            Exception: If TTS conversion fails
        """
        tts = TTS(model_name=self.model, progress_bar=True)
        tts.to(self.device)
        
        if self.file.endswith(".pdf"):
            text = self._clean_text(self._extract_text())
        else:
            text = self.file
            
        tts.tts_to_file(text=text, file_path=f"{self.output_name}.wav")
