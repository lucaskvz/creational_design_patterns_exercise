
from dataclasses import dataclass
from datetime import date
from typing import Optional, Dict, Any, List


@dataclass(frozen=True)
class Campaign:
    name: str
    channel: str
    daily_budget: float
    start_date: date
    end_date: Optional[date]
    target_audience: Dict[str, Any]
    creatives: List[Dict[str, str]]
    tracking: Dict[str, str]


class CampaignBuilder:
    def __init__(self):
      # TODO
      pass

    def with_name(self, name: str):
      # TODO
      pass

    def with_channel(self, channel: str):
      # TODO
      pass

    def with_budget(self, daily_budget: float):
      # TODO
      pass

    def with_dates(self, start_date, end_date=None):
      # TODO
      pass

    def with_audience(self, **kwargs):
      # TODO
      pass

    def add_creative(self, headline: str, image_url: str):
      # TODO
      pass

    def with_tracking(self, **kwargs):
      # TODO
      pass

    def build(self) -> Campaign:
      # TODO: Validations and return Campaign instance
      pass
