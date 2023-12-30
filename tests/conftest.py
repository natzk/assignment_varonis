# conftest.py
import pytest
from mocks.MockSalesforce import MockSalesforce
from mocks.MockNetSuite import MockNetSuite
from mocks.MockDatabase import MockDatabase
from mocks.MockEmailSystem import MockEmailSystem

@pytest.fixture
def mock_salesforce():
    return MockSalesforce()

@pytest.fixture
def mock_email_system():
    return MockEmailSystem()

@pytest.fixture
def mock_netsuite(mock_salesforce, mock_email_system):
    return MockNetSuite(mock_salesforce, mock_email_system)

@pytest.fixture
def mock_database():
    return MockDatabase()
