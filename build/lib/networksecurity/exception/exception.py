import sys
from networksecurity.logger import logger1


class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details: sys): # type: ignore
        self.error_message = error_message
        _, _, exc_tb = error_details.exc_info()

        if exc_tb:
            self.lineno = exc_tb.tb_lineno
            self.file_name = exc_tb.tb_frame.f_code.co_filename
        else:
            self.lineno = "Unknown"
            self.file_name = "Unknown"

    def __str__(self):
        return (
            f"Error Occurred in python script name "
            f"[{self.file_name}] "
            f"line number [{self.lineno}] "
            f"error message [{self.error_message}]"
        )


if __name__ == "__main__":
    try:
        logger1.info("Enter the Try Block")
        a = 1 / 0
        print("This will not printed", a)

    except Exception as e:
        logger1.error("Zero division Error", exc_info=True)
        raise NetworkSecurityException(e, sys) from e
