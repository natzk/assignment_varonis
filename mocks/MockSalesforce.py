# Mocking Salesforce interactions
import random

import logging
logger = logging.getLogger('test_logger')


class MockSalesforce:
    order_id_counter = 12344

    def __init__(self):
        # self.order_id_counter = 12345
        self.simulate_failure = True
        self.orders = {} # Dictionary to store order details
        logger.info("MockSalesforce initialized")


    def set_failure_simulation(self, simulate_failure):
        self.simulate_failure = simulate_failure
    
    def login(self, user, password):
        valid_credentials = {
            "sales_ops_user": "sales_ops_password",
            "other_user": "other_password"
        }
        if valid_credentials.get(user) == password:
            # logger.info(f"Login attempt for user: {user}")
            return {"status": "success", "message": "Logged in successfully"}
        else:
            logger.info(f"Login attempt failed")
            return {"status": "failure", "message": "Invalid credentials"}
    
    def create_credit_order(self):
        logger.info(f"Creating credit order.")
        if self.simulate_failure:
            return {"status": "failure", "message": "Network error"}

        MockSalesforce.order_id_counter += 1  # Increment for a new order ID
        order_status = random.choice(["created", "pending", "failed"])
        order_id = str(self.order_id_counter)
        order = {"order_id": order_id, "status": order_status}
        self.orders[order_id] = order  # Store the order details
        return order
