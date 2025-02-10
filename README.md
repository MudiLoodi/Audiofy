# Audiofy - PDF to Audiobook Converter

A simple desktop application that converts PDF documents to audiobooks using Text-to-Speech technology.

## Features

- User-friendly GUI interface
- Good-quality text-to-speech conversion

## Installation

1. Clone the repository:
```bash
git clone https://github.com/MudiLoodi/Audiofy
cd Audiofy
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
# For Windows
venv\Scripts\activate
# For Unix/MacOS
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
python main.py
```

2. Using the application:
   - Click "Select PDF File" to choose your PDF document
   - Enter a name for your output audio file
   - Click "Convert to Audiobook" to start the conversion
   - Wait for the process to complete
   - Find your audio file in the same directory as the PDF

## Project Structure

```
Audiofy/
├── config/
│   └── settings.py      # Application configuration
├── gui/
│   └── app.py          # GUI implementation
├── utils/
│   └── converter.py    # PDF to Audio conversion logic
├── main.py             # Application entry point
├── requirements.txt    # Project dependencies
└── README.md          # This file
```

## Requirements

- Python 3.8 or higher
- Dependencies listed in requirements.txt

## Technical Details

- Uses `customtkinter` for modern GUI elements
- `TTS` (Text-to-Speech) for audio conversion
- `pypdf` for PDF text extraction
- Default TTS model: "tts_models/en/jenny/jenny"

## Credits
Special thanks to [coqui-ai-TTS](https://github.com/idiap/coqui-ai-TTS) for providing the pretrained TTS models used in this project.
