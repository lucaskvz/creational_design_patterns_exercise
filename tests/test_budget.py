import pytest
from campaign_launchpad.budget import GlobalBudget

def test_singleton_identity_and_initial_balance():
    b1 = GlobalBudget(500.0)
    b2 = GlobalBudget(9999.0)
    assert b1 is b2
    assert b1.remaining() == 500.0

def test_allocate_and_remaining():
    b = GlobalBudget(300.0)
    b.allocate(120.0)
    assert b.remaining() == 180.0
    b.allocate(80.0)
    assert b.remaining() == 100.0

def test_insufficient_funds_raises():
    b = GlobalBudget(100.0)
    with pytest.raises(ValueError):
        b.allocate(101.0)

def test_non_positive_allocation_raises():
    b = GlobalBudget(100.0)
    with pytest.raises(ValueError):
        b.allocate(0)
