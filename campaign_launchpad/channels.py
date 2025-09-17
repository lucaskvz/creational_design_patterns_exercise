
from abc import ABC, abstractmethod
from uuid import uuid4
from .budget import GlobalBudget
from .campaign import Campaign


class ChannelClient(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def create_campaign(self, campaign: Campaign) -> str:
        # TODO: Create a campaign on this channel and return an external id.
        pass

    @abstractmethod
    def pause_campaign(self, campaign_id: str) -> None:
        pass


class GoogleAdsClient(ChannelClient):
  # TODO: Implement the Google Ads specific logic here.
  pass

class FacebookAdsClient(ChannelClient):
  # TODO: Implement the Facebook Ads specific logic here.
  pass

class ChannelClientFactory:
    @staticmethod
    def create(channel: str) -> ChannelClient:
      # TODO: Return the appropriate client based on the channel.
      pass
