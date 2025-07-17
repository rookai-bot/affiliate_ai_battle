import datetime

def track_performance(agent_name):
    print(f"[Analytics] Tracking performance for {agent_name}...")

    # Simulate click or engagement tracking
    fake_clicks = 100
    fake_signups = 12
    fake_sales = 3
    revenue = fake_sales * 39.99  # Example product value

    today = datetime.date.today().isoformat()

    report = (
        f"📊 InstaPrime Performance Report ({today})\n"
        f"👀 Clicks: {fake_clicks}\n"
        f"📝 Signups: {fake_signups}\n"
        f"💰 Sales: {fake_sales}\n"
        f"💵 Revenue: ${revenue:.2f}"
    )

    print(report)
