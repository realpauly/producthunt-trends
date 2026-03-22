import requests
import json
import os
from dotenv import load_dotenv

# Load API token from .env
load_dotenv()
API_TOKEN = os.getenv("PRODUCT_HUNT_DEVELOPER_TOKEN")

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

# AI-related keyword list
ai_keywords = ["AI", "Artificial", "Machine Learning", "LLM", "Chatbot", "Neural", "Vision", "Generative", "NLP"]

# Pagination variables
cursor = None
has_next_page = True
all_posts = []
max_pages = 10  # scrape up to 5 pages (500 posts)

page_count = 0

while has_next_page and page_count < max_pages:
    graphql_query = f"""
query {{
  posts(order: NEWEST, first: 50{f', after: "{cursor}"' if cursor else ""}) {{
    edges {{
      node {{
        name
        tagline
        createdAt
        url
        votesCount
        topics {{
          edges {{
            node {{
              name
            }}
          }}
        }}
      }}
    }}
    pageInfo {{
      endCursor
      hasNextPage
    }}
  }}
}}
"""


    response = requests.post(
        "https://api.producthunt.com/v2/api/graphql",
        json={"query": graphql_query},
        headers=headers
    )

    data = response.json()

    # Error handling
    if response.status_code != 200 or "data" not in data:
        print("❌ Error: Bad response or missing data.")
        print("Status Code:", response.status_code)
        print("Response:", json.dumps(data, indent=2))
        break

    posts = data["data"]["posts"]["edges"]
    page_info = data["data"]["posts"]["pageInfo"]
    cursor = page_info["endCursor"]
    has_next_page = page_info["hasNextPage"]
    page_count += 1

    all_posts.extend(posts)

print(f"📦 Retrieved {len(all_posts)} total posts from Product Hunt")

# Filter for AI-related posts
ai_posts = []
for edge in all_posts:
    post = edge["node"]
    tags = [t["node"]["name"] for t in post["topics"]["edges"]]
    if (
    any(any(k.lower() in t.lower() for k in ai_keywords) for t in tags)
    or any(k.lower() in post["name"].lower() for k in ai_keywords)
    or any(k.lower() in post["tagline"].lower() for k in ai_keywords)
    ):
        ai_posts.append({
            "name": post["name"],
            "description": post["tagline"],
            "launch_date": post["createdAt"],
            "upvotes": post["votesCount"],
            "tags": tags,
            "url": post["url"],
        })

print(f"✅ Scraped {len(ai_posts)} AI-related startups.")

# Save to JSON
os.makedirs("data/raw", exist_ok=True)
with open("data/raw/ai_startups.json", "w") as f:
    json.dump(ai_posts, f, indent=2)
