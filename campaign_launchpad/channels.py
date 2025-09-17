
from abc import ABC, abstractmethod
from uuid import uuid4
from .budget import GlobalBudget
from .campaign import Campaign


class ChannelClient(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def create_campaign(self, campaign: Campaign) -> str:
        """Create a campaign on this channel and return an external id."""
        pass

    @abstractmethod
    def pause_campaign(self, campaign_id: str) -> None:
        pass


class GoogleAdsClient(ChannelClient):
    def __init__(self):
        super().__init__("Google Ads")

    def create_campaign(self, campaign: Campaign) -> str:
        budget = GlobalBudget()
        budget.allocate(campaign.daily_budget)
        print(f"[GoogleAds] Created campaign '{campaign.name}' "
              f"(Allocated {campaign.daily_budget}, Remaining {budget.remaining()})")
        return f"g-{uuid4().hex[:8]}"

    def pause_campaign(self, campaign_id: str) -> None:
        print(f"[GoogleAds] Paused campaign {campaign_id}")


class FacebookAdsClient(ChannelClient):
    def __init__(self):
        super().__init__("Facebook Ads")

    def create_campaign(self, campaign: Campaign) -> str:
        budget = GlobalBudget()
        budget.allocate(campaign.daily_budget)
        print(f"[FacebookAds] Created campaign '{campaign.name}' "
              f"(Allocated {campaign.daily_budget}, Remaining {budget.remaining()})")
        return f"f-{uuid4().hex[:8]}"

    def pause_campaign(self, campaign_id: str) -> None:
        print(f"[FacebookAds] Paused campaign {campaign_id}")


class ChannelClientFactory:
    @staticmethod
    def create(channel: str) -> ChannelClient:
        channel = channel.lower().strip()
        if channel == "google":
            return GoogleAdsClient()
        if channel == "facebook":
            return FacebookAdsClient()
        raise ValueError(f"Unsupported channel: {channel}")
