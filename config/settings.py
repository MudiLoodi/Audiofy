"""
Global configuration and constants.
"""

# TTS Model configurations
DEFAULT_MODEL = "tts_models/en/jenny/jenny"  # Default TTS model for voice synthesis
DEFAULT_DEVICE = "cpu"  # Device to run TTS on (cpu/cuda)

# GUI configurations
WINDOW_WIDTH = 600  # Main window width in pixels
WINDOW_HEIGHT = 430  # Main window height in pixels
PADDING = 20  # Standard padding for widgets
BUTTON_HEIGHT = 50  # Height for main action buttons
ENTRY_HEIGHT = 40  # Height for text entry fields
ENTRY_WIDTH = 400  # Width for text entry fields

# Color scheme
PRIMARY_COLOR = "#3b8ed0"  # Main theme color
HOVER_COLOR = "#2a6caf"  # Button hover state color
ERROR_COLOR = "red"  # Used for error messages
SUCCESS_COLOR = "green"  # Used for success messages
PROCESSING_COLOR = "blue"  # Used for processing status
