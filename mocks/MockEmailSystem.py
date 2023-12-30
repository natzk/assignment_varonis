import logging
logger = logging.getLogger('test_logger')


class MockEmailSystem:
    def __init__(self):
        self.sent_emails = []
        logger.info("MockEmailSystem initialized")

    def send_email(self, order_id, status):
        email_info = {"order_id": order_id, "status": status}
        self.sent_emails.append(email_info)
        logger.info(f"Email sent for order ID: {order_id} with status: {status}")
