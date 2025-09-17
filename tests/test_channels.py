import pytest
from datetime import date
from campaign_launchpad.budget import GlobalBudget
from campaign_launchpad.channels import ChannelClientFactory, GoogleAdsClient, FacebookAdsClient
from campaign_launchpad.campaign import CampaignBuilder

def test_factory_returns_correct_client_types():
    assert isinstance(ChannelClientFactory.create("google"), GoogleAdsClient)
    assert isinstance(ChannelClientFactory.create("facebook"), FacebookAdsClient)
    with pytest.raises(ValueError):
        ChannelClientFactory.create("unknown")

def test_clients_allocate_from_same_global_budget():
    budget = GlobalBudget(500.0)

    campaign_google = (
        CampaignBuilder()
        .with_name("G-Alpha")
        .with_channel("google")
        .with_budget(200.0)
        .with_dates(date(2025, 9, 20), date(2025, 9, 25))
        .add_creative("H1", "u1")
        .build()
    )
    campaign_facebook = (
        CampaignBuilder()
        .with_name("F-Beta")
        .with_channel("facebook")
        .with_budget(250.0)
        .with_dates(date(2025, 9, 26), date(2025, 10, 1))
        .add_creative("H2", "u2")
        .build()
    )

    g_client = ChannelClientFactory.create(campaign_google.channel)
    f_client = ChannelClientFactory.create(campaign_facebook.channel)

    google_campaign_id = g_client.create_campaign(campaign_google)
    assert google_campaign_id.startswith("g-")
    assert budget.remaining() == 300.0

    facebook_campaign_id = f_client.create_campaign(campaign_facebook)
    assert facebook_campaign_id.startswith("f-")
    assert budget.remaining() == 50.0

def test_client_creation_fails_when_budget_insufficient():
    GlobalBudget(100.0)
    campaign_too_big = (
        CampaignBuilder()
        .with_name("Too Big")
        .with_channel("google")
        .with_budget(200.0)
        .with_dates(date(2025, 9, 20), date(2025, 9, 21))
        .add_creative("H", "u")
        .build()
    )
    client = ChannelClientFactory.create(campaign_too_big.channel)
    with pytest.raises(ValueError):
        client.create_campaign(campaign_too_big)
