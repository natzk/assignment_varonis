import pytest
from utils import login_to_systems, create_and_approve_credit_order

import logging
logger = logging.getLogger('test_logger')


class TestIntegration:

    def test_tl_approval_functionality(self, mock_salesforce, mock_netsuite):
        logger.info("Starting TL Approval Functionality Test")
        mock_salesforce.set_failure_simulation(False)
        # assert mock_salesforce.login("sales_ops_user", "sales_ops_password")["status"] == "success"
        login_to_systems(mock_salesforce, mock_netsuite)

        # order_data = mock_salesforce.create_credit_order()
        # order_id = order_data["order_id"]
        # mock_salesforce.orders[order_id]["status"] = "TL Credit Review"  # Simulate order review by TL

        # approval_result = mock_netsuite.approve_credit_order(order_id)

        _, approval_result = create_and_approve_credit_order(mock_salesforce, mock_netsuite)

        assert approval_result["status"] == "Approved by TL", "Order was not approved correctly"

    def test_email_notification_system_integration(self, mock_salesforce, mock_netsuite, mock_email_system):
        logger.info("Starting Email Notification System Integration Test")
        mock_salesforce.set_failure_simulation(False)
 
        login_to_systems(mock_salesforce, mock_netsuite)

        order_id, _ = create_and_approve_credit_order(mock_salesforce, mock_netsuite, send_email=True)
        
        assert any(email["order_id"] == order_id for email in mock_email_system.sent_emails), "Email not sent"
        assert mock_email_system.sent_emails[-1]["status"] == "Approved by TL", "Incorrect email status"

if __name__ == "__main__":
    pytest.main()
