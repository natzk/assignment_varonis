import pytest

import logging
logger = logging.getLogger('test_logger')


class TestDataIntegrity:

    def test_di_credit_memo_db_verification(self, mock_salesforce, mock_netsuite, mock_database):
        logger.info("Starting Data Integrity Credit Memo DB Verification Test")
        mock_salesforce.set_failure_simulation(False)

        assert mock_salesforce.login("sales_ops_user", "sales_ops_password")["status"] == "success"
        assert mock_netsuite.login("valid_user", "correct_password")["status"] == "success"

        # Test Steps
        order_data = mock_salesforce.create_credit_order()
        if order_data["status"] == "failed":
            assert order_data["status"] == "failed", "Request wasn't created"
        if order_data["status"] == "pending":
            assert order_data["status"] == "pending", "Request hasn't been created yet (pending)"
        order_id = order_data["order_id"]

        mock_database.insert_data(order_id, "TL Credit Review")

        _ = mock_netsuite.get_order_request(order_id)
        logger.info("Order ID: %s", order_id)

        db_or_number = mock_database.query(f"SELECT OR_Number from YourDataBaseTable WHERE OR_Number = '{order_id}'")
        assert db_or_number == order_id, "Database OR Number mismatch"
        db_credit_status = mock_database.query("SELECT credit_approval_state from YourDataBaseTable WHERE credit_approval_state = 'TL Credit Review'")
        assert db_credit_status == "TL Credit Review", "Database Credit Approval State mismatch"

   
if __name__ == "__main__":
    pytest.main()
