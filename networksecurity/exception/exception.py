import sys
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details: sys):
        self.error_message = error_message

        # Extract traceback details
        _, _, exc_tb = error_details.exc_info()
        if exc_tb is not None:  # Ensure traceback is available
            self.lineno = exc_tb.tb_lineno
            self.file_name = exc_tb.tb_frame.f_code.co_filename
        else:
            self.lineno = None
            self.file_name = None

    def __str__(self):
        return "Error occurred in Python script name [{0}] line number [{1}] error message [{2}]".format(
            self.file_name, self.lineno, str(self.error_message)
        )


# Main block
if __name__ == '__main__':
    try:
        logger.logging.info("Enter the try block")
        a = 1 / 0  # Triggering an error
        print("This will not be printed", a)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
