
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

# 3) Run the demo app
python -m campaign_launchpad.app

# 4) Run tests
python -m pytest -q
```
