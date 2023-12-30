# Mocking NetSuite interactions
import logging
logger = logging.getLogger('test_logger')

class MockNetSuite:
    def __init__(self, mock_salesforce, mock_email_system):
        self.mock_salesforce = mock_salesforce
        self.mock_email_system = mock_email_system
        logger.info("MockNetSuite initialized")


    def __repr__(self):
        return "<MockNetSuite Object>"

    def login(self, user, password):
        if user == "valid_user" and password == "correct_password":
            return {"status": "success", "message": "Logged in successfully"}
        else:
            return {"status": "failure", "message": "Invalid credentials"}


    def get_order_request(self, order_id):
        order = self.mock_salesforce.orders.get(order_id)
        if not order:
            raise ValueError("Order not found")

        # Return order details with NetSuite-specific status
        return {"order_id": order_id, "status": "TL Credit Review"}
    
    def search_order(self, order_id):

        return {"order_id": order_id, "status": "TL Credit Review"}
    

    def approve_credit_order(self, order_id, send_email=False):
        order = self.mock_salesforce.orders.get(order_id)
        if not order:
            raise ValueError("Order not found")

        if order["status"] != "TL Credit Review":
            logger.error(f"Order ID: {order_id} is not in a state where it can be approved")
            return {"order_id": order_id, "status": order["status"]}

        # Approve the order
        logger.info(f"Approving order ID: {order_id}")
        order["status"] = "Approved by TL"
        if send_email:
            self.mock_email_system.send_email(order_id, "Approved by TL")
        return {"order_id": order_id, "status": "Approved by TL"}

