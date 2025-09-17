# Campaign Launchpad

You’re building a tiny backend service for a marketing team that launches online ad campaigns across multiple channels (e.g., Google Ads, Facebook Ads).

## Business requirements

- The company wants to keep track of the global budget when launching different campaigns.
- Marketers choose a channel and the system must create the right client to talk to that channel.
- Campaigns have many optional pieces (budget caps, audiences, creatives, tracking parameters). We need a safe way to assemble a valid campaign.

## Architecture

- **Builder**: `CampaignBuilder` assembles validated `Campaign` objects with a fluent API.
- **Singleton**: `GlobalBudget` — one shared marketing wallet for all campaigns.
- **Factory Method**: `ChannelClientFactory` creates channel-specific clients (Google, Facebook).

## Project layout

```dir_tree
root_dir
├─ campaign_launchpad/
│  ├─ __init__.py
│  ├─ budget.py
│  ├─ campaign.py
│  └─ channels.py
├─ tests/
│  ├─ test_budget.py
│  ├─ test_campaign.py
│  └─ test_channels.py
└─ README.md
```

## Quickstart

```bash
# 1) Create a virtual environment (optional)
# Unix
python -m venv .venv && source .venv/bin/activate

# Windows: 
python -m venv .venv
.venv\Scripts\activate

# 2) Install test dependency
pip install pytest

# 3) Testing
# Run all tests
python -m pytest -q
# Run budget tests
python -m pytest ./tests/test_budget.py

# 4) Run the demo app
python -m campaign_launchpad.app
```

## Exercises

### 1. Implement campaign builder

Functional requirements:

- A campaign must have a name.
- A campaign must have a channel.
- The daily budget must be provided and must be positive.
- The start date is required.
- If an end date is provided, the start date must be before or equal to the end date.
- At least one creative (headline and image URL) is required.

To test this part:

```python
python -m pytest ./tests/test_campaign.py
```

Goal --> Pass campaign tests

### 2. Implement budget

Functional requirements:

- Ensure there is only a single bugdet
- Ensure bugdet cannot go below zero
- Allow no negative allocations

To test this part:

```python
python -m pytest ./tests/test_budget.py
```

Goal --> Pass budget tests

### 3. Implement channel client factory

Functional requirements:

- Campaigns should allocate their daily budget to the global budget.
- When a campaign is created, a external id should be returned. This id should have a prefix with the initial of the channel i.e. For facebook ads --> "f_<some_id>"
- Two clients are needed: FacebookAds and GoogleAds
- If different channel client is created, and error should arise.

To test this part:

```python
python -m pytest ./tests/test_channels.py
```

Goal --> Pass channels tests
