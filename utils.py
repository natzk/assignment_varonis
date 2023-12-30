def login_to_systems(mock_salesforce, mock_netsuite):
    assert mock_salesforce.login("sales_ops_user", "sales_ops_password")["status"] == "success"
    assert mock_netsuite.login("valid_user", "correct_password")["status"] == "success"

def create_credit_order(mock_salesforce):
    order_data = mock_salesforce.create_credit_order()
    assert order_data["status"] in ["created", "pending","failed"], "Order creation failed"
    return order_data

def create_and_approve_credit_order(mock_salesforce, mock_netsuite, send_email=False):
    order_data = create_credit_order(mock_salesforce)
    order_id = order_data["order_id"]
    mock_salesforce.orders[order_id]["status"] = "TL Credit Review"
    approval_result = mock_netsuite.approve_credit_order(order_id, send_email=send_email)
    return order_id, approval_result