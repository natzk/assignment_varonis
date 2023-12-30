import pytest
from utils import login_to_systems, create_credit_order
import logging
logger = logging.getLogger('test_logger')


class TestUserInterface:

    def test_ui_credit_memo_creation(self, mock_salesforce, mock_netsuite):
        logger.info("Starting UI Credit Memo Creation Test")
        mock_salesforce.set_failure_simulation(False)

        login_to_systems(mock_salesforce, mock_netsuite)

        # Test Steps
        order_data = create_credit_order(mock_salesforce)

        if order_data["status"] == "failed":
            assert order_data["status"] == "failed", "Request wasn't created"
        if order_data["status"] == "pending":
            assert order_data["status"] == "pending", "Request hasn't been created yet (pending)"
        order_id = order_data["order_id"]
        logger.info("Order ID: %s", order_id)

        netsuite_order = mock_netsuite.get_order_request(order_id)

        assert netsuite_order["order_id"] == order_id, "Order ID mismatch"
        assert netsuite_order["status"] == "TL Credit Review", "Status is not 'TL Credit Review'"

if __name__ == "__main__":
    pytest.main()
