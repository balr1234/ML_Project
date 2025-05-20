import sys  # Provides access to system-specific parameters and functions
from src.logger import logging

# Function to generate a detailed error message
def error_message_detail(error, error_detail: sys):
    """
    error: The original exception object
    error_detail: sys module used to extract traceback details
    """
    # Get traceback information (type, value, traceback)
    _, _, exc_tb = error_detail.exc_info()

    # Get the file name where the exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Format the custom error message
    error_message = "Error occurred in Python script: [{0}], line number: [{1}], error message: [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message

# Custom exception class that inherits from Python's base Exception
class CustomException(Exception):
    def __init__(self, error_message, error_details: sys):
        """
        error_message: The actual error message or exception
        error_details: sys module used to get traceback info
        """
        super().__init__(error_message)  # Initialize the base Exception class
        # Create a formatted error message with file name, line number, and error
        self.error_message = error_message_detail(error_message, error_detail=error_details)

    def __str__(self):
        # This method defines how the error message will be printed
        return self.error_message

