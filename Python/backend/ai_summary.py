import os, anthropic


from .analytics import kpis


def generate_summary(filtered_df):
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY is not set")

    stats = kpis.compute_kpis(filtered_df)
    dominant_make = filtered_df["make"].mode()[0]
    prompt = (
        f"Dataset: {stats['count']} vehicles, average highway MPG {stats['avg_mpg']}, "
        f"average horsepower {stats['avg_hp']}, most common make {dominant_make}, "
        f"model years {filtered_df['year'].min()}-{filtered_df['year'].max()}. "
        "Write one friendly, conversational paragraph summarizing this filtered "
        "car dataset for someone browsing a dashboard, e.g. \"You're looking at "
        '42 SUVs from 2005-2012 averaging 22 MPG..."'
    )

    client = anthropic.Anthropic(api_key=api_key)
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=300,
        thinking={"type": "disabled"},
        output_config={"effort": "low"},
        messages=[{"role": "user", "content": prompt}],
    )
    return next((b.text for b in response.content if b.type == "text"), "")
