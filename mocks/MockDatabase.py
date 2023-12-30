class MockDatabase:
    def __init__(self):
        self.data = {}
    
    def insert_data(self, order_id, state):
        self.data["OR_Number"] = order_id
        self.data["credit_approval_state"] = state

    def query(self, sql_command):
        if "OR_Number" in sql_command:
            order_id = sql_command.split("'")[1]
            return self.data.get("OR_Number")
        elif "credit_approval_state" in sql_command:
            return self.data.get("credit_approval_state")
        else:
            return None
