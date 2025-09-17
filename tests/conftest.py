import pytest
from campaign_launchpad.budget import GlobalBudget

@pytest.fixture(autouse=True)
def reset_global_budget_singleton():
    GlobalBudget._instance = None
    yield
    GlobalBudget._instance = None
