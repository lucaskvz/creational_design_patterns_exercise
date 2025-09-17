import pytest
from datetime import date
from campaign_launchpad.campaign import CampaignBuilder, Campaign

def test_builder_success_and_immutability():
    c = (
        CampaignBuilder()
        .with_name("Launch ES")
        .with_channel("google")
        .with_budget(150.0)
        .with_dates(date(2025, 9, 20), date(2025, 9, 30))
        .with_audience(countries=["ES"], ages=(25, 55))
        .add_creative("Nuevo plan -20%", "https://fake/img.png")
        .with_tracking(utm_source="google", utm_campaign="launch_es")
        .build()
    )
    assert isinstance(c, Campaign)
    with pytest.raises(Exception):
        c.name = "Oops"  # type: ignore

@pytest.mark.parametrize(
    "kwargs, err_msg",
    [
        (dict(name=None), "name"),
        (dict(channel=None), "channel"),
        (dict(budget=-1), "Budget"),
        (dict(start=date(2025, 9, 30), end=date(2025, 9, 1)), "Start date"),
        (dict(no_creatives=True), "creative"),
    ],
)
def test_builder_validations(kwargs, err_msg):
    b = CampaignBuilder()
    if kwargs.get("name", "ok") is None:
        pass
    else:
        b.with_name("X")

    if kwargs.get("channel", "ok") is None:
        pass
    else:
        b.with_channel("google")

    budget_val = kwargs.get("budget", 10.0)
    b.with_budget(budget_val)

    start = kwargs.get("start", date(2025, 1, 1))
    end = kwargs.get("end", date(2025, 1, 2))
    b.with_dates(start, end)

    if not kwargs.get("no_creatives", False):
        b.add_creative("h", "u")

    with pytest.raises(ValueError) as e:
        b.build()
    assert err_msg.lower() in str(e.value).lower()
