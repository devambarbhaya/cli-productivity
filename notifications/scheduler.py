import logging
from notifications import check_and_notify

logging.basicConfig(filename="notifications.log", level=logging.DEBUG)

if __name__ == "__main__":
    logging.info("Starting notification check...")
    try:
        check_and_notify()
    except Exception as e:
        logging.error(f"Error during notification check: {str(e)}")
    logging.info("Notification check complete.")
