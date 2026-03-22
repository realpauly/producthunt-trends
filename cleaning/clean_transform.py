import json
import pandas as pd
import os

# Load raw JSON
with open("data/raw/ai_startups.json", "r") as f:
    raw_data = json.load(f)

# Normalize into a DataFrame
df = pd.DataFrame(raw_data)

# Convert date
df["launch_date"] = pd.to_datetime(df["launch_date"])

# Feature engineering
df["description_length"] = df["description"].apply(len)
df["tag_count"] = df["tags"].apply(len)
df["month_launched"] = df["launch_date"].dt.to_period("M")
df["upvotes_per_word"] = df["upvotes"] / df["description_length"]

# Reorder columns
columns_order = [
    "name", "description", "description_length", "upvotes", "upvotes_per_word", "launch_date", "month_launched", "tag_count",
    "tags", "url"
]
df = df[columns_order]

# Save cleaned data
os.makedirs("data/processed", exist_ok=True)
df.to_csv("data/processed/ai_startups_cleaned.csv", index=False)

print(f"✅ Cleaned data saved: {len(df)} startups → data/processed/ai_startups_cleaned.csv")
