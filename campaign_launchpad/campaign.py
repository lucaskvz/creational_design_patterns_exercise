from dataclasses import dataclass
from datetime import date
from typing import Optional, Dict, Any, List


@dataclass(frozen=True)
class Campaign:
    # I use a frozen dataclass so once a campaign is created, it's immutable.
    # This guarantees tests can't mutate fields they should raise on assignment.
    name: str
    channel: str
    daily_budget: float
    start_date: date
    end_date: Optional[date]
    target_audience: Dict[str, Any]
    creatives: List[Dict[str, str]]
    tracking: Dict[str, str]


class CampaignBuilder:
    # I keep all parts of the campaign as private fields until build-time.
    def __init__(self):
        self._name: Optional[str] = None
        self._channel: Optional[str] = None
        self._daily_budget: Optional[float] = None
        self._start_date: Optional[date] = None
        self._end_date: Optional[date] = None
        self._audience: Dict[str, Any] = {}
        self._creatives: List[Dict[str, str]] = []
        self._tracking: Dict[str, str] = {}

    def with_name(self, name: str):
        # I return self from each with_* method to enable fluent chaining.
        self._name = name
        return self

    def with_channel(self, channel: str):
        self._channel = channel
        return self

    def with_budget(self, daily_budget: float):
        self._daily_budget = daily_budget
        return self

    def with_dates(self, start_date, end_date=None):
        self._start_date = start_date
        self._end_date = end_date
        return self

    def with_audience(self, **kwargs):
        # I allow arbitrary audience attributes (e.g., countries, ages).
        self._audience.update(kwargs)
        return self

    def add_creative(self, headline: str, image_url: str):
        # I collect creatives as a list of dicts; at least one is required.
        self._creatives.append({"headline": headline, "image_url": image_url})
        return self

    def with_tracking(self, **kwargs):
        # I coerce tracking values to strings to keep them uniform.
        self._tracking.update({k: str(v) for k, v in kwargs.items()})
        return self

    def build(self) -> Campaign:
        # I validate all required fields before constructing the immutable Campaign.
        if not self._name:
            raise ValueError("Campaign name is required.")
        if not self._channel:
            raise ValueError("Campaign channel is required.")
        if self._daily_budget is None or self._daily_budget <= 0:
            raise ValueError("Budget must be positive.")
        if not self._start_date:
            raise ValueError("Start date is required.")
        if self._end_date is not None and self._start_date > self._end_date:
            raise ValueError("Start date must be before or equal to end date.")
        if not self._creatives:
            raise ValueError("At least one creative is required.")

        # I return a new frozen Campaign instance with all the accumulated data.
        return Campaign(
            name=self._name,
            channel=self._channel,
            daily_budget=float(self._daily_budget),
            start_date=self._start_date,
            end_date=self._end_date,
            target_audience=dict(self._audience),
            creatives=list(self._creatives),
            tracking=dict(self._tracking),
        )