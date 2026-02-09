"""
Constants configuration for ImageToPDF application.
"""

# Application Configuration
APP_NAME = "ImageToPDF"
APP_VERSION = "2.0.0"
APP_AUTHOR = "WAEL SAHLI"

# GUI Configuration
MAX_IMAGE_BUTTONS = 12
BUTTON_TEXT_COLOR = "#007399"
BUTTON_SELECTED_COLOR = "#B2D17C"
BUTTON_TEXT_COLOR_SELECTED = "#000000"
WINDOW_MINIMIZE_FLAG = 0x08000000

# File Configuration
IMAGE_EXTENSIONS = {'.jpeg', '.jpg', '.png'}
PDF_EXTENSIONS = {'.pdf'}
DEFAULT_OUTPUT_DIR = "output"

# PDF Configuration
PDF_MERGER_APPEND_MODE = 'a'
PDF_MERGER_WRITE_MODE = 'wb'

# Image Configuration
IMAGE_FORMAT_RGB = 'RGB'
IMAGE_FORMAT_PNG = 'PNG'
IMAGE_FORMAT_JPEG = 'JPEG'

# Naming Configuration
TIMESTAMP_FORMAT = "%Y%m%d%H%M%S"
PDF_TIMESTAMP_FORMAT = "%d-%m-%Y_%H-%M-%S-%f"
PDF_OUTPUT_PREFIX = "Merged_PDF_"
PDF_OUTPUT_SUFFIX = ".pdf"
JPEG_OUTPUT_PREFIX = "Converted-PDF-page"
JPEG_OUTPUT_SUFFIX = ".jpeg"

# File Size Limits (in bytes)
MAX_FILE_SIZE = 100 * 1024 * 1024  # 100MB
MAX_IMAGE_SIZE = 50 * 1024 * 1024  # 50MB

# Logging Configuration
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_FILE = "image_to_pdf.log"

# Error Messages
ERROR_INVALID_FILE = "Invalid file format. Please select a valid image or PDF file."
ERROR_FILE_TOO_LARGE = "File is too large. Maximum size is {max_size}."
ERROR_NO_FILES_SELECTED = "Please select at least one image to convert to PDF."
ERROR_PDF_CONVERSION_FAILED = "Failed to convert PDF to JPEG."
ERROR_IMAGE_CONVERSION_FAILED = "Failed to convert images to PDF."
ERROR_UNKNOWN = "An unknown error occurred."

# Success Messages
SUCCESS_IMAGE_TO_PDF = "Images converted to PDF successfully.\nAll images are available in the output folder."
SUCCESS_PDF_TO_JPEG = "PDF file converted successfully.\nAll images are available in the output folder."

# UI Messages
TITLE_INFO = "Info"
TITLE_WARNING = "Warning"
TITLE_ERROR = "Error"
TITLE_DONE = "Done"