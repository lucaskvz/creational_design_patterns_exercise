from datetime import date
from .budget import GlobalBudget
from .channels import ChannelClientFactory
from .campaign import CampaignBuilder

def main():
    budget = GlobalBudget(1000.0)
    print("Initial global marketing budget:", budget.remaining())

    campaign1 = (
        CampaignBuilder()
        .with_name("Autumn Promo")
        .with_channel("google")
        .with_budget(300.0)
        .with_dates(date(2025, 9, 20), date(2025, 10, 5))
        .add_creative("Promo -20%", "https://fake.com/img1.png")
        .with_tracking(source="google", campaign="autumn_promo")
        .build()
    )

    client1 = ChannelClientFactory.create(campaign1.channel)
    client1.create_campaign(campaign1)

    campaign2 = (
        CampaignBuilder()
        .with_name("Black Friday Push")
        .with_channel("facebook")
        .with_budget(800.0)
        .with_dates(date(2025, 11, 20), date(2025, 11, 30))
        .add_creative("Black Friday 50% OFF", "https://fake.com/img2.png")
        .with_tracking(source="facebook", campaign="bf_push")
        .build()
    )

    client2 = ChannelClientFactory.create(campaign2.channel)
    try:
        client2.create_campaign(campaign2)
    except ValueError as e:
        print("Could not create FB campaign:", e)

    print("Final remaining budget:", budget.remaining())

if __name__ == "__main__":
    main()
