
# 🚀 AI Pulse – Tracking AI Startup Trends on Product Hunt

Welcome to **AI Pulse**, a cloud-native project that scrapes, processes, analyzes, and visualizes AI startup launches on Product Hunt using AWS and modern data tools.

![dashboard](https://github.com/user-attachments/assets/d95524e3-2229-46bf-9162-39cb620df327)

---

## 📦 Project Overview

This project tracks and analyzes **AI-related product launches** on Product Hunt by:
- Scraping data using Python + GraphQL
- Cleaning and transforming data using Pandas
- Hosting on AWS S3
- Cataloging with Glue and querying with Athena
- Visualizing trends using Amazon QuickSight

---

## 🎯 Goals

- Explore the **share and popularity** of AI startups in recent tech launches
- Identify **trending tags**, **top startups**, and **efficient pitches**
- Showcase a complete **end-to-end data pipeline** using AWS

---

## ⚙️ Tech Stack

| Component     | Tools |
|---------------|-------|
| Scraping      | Python, GraphQL API (Product Hunt) |
| Storage       | AWS S3 |
| Cleaning      | Pandas |
| Cataloging    | AWS Glue |
| Querying      | AWS Athena |
| Visualization | Amazon QuickSight |
| Hosting       | GitHub Pages |

---

## 🔍 Data Pipeline Architecture

```
Python Scraper → Cleaned CSV → S3 → AWS Glue → Athena → QuickSight → GitHub Pages
```

---

## 🧪 Scraping Logic

- Used the Product Hunt **GraphQL API** to fetch startup posts
- Filtered results based on **AI-related tags and description keywords**
- Extracted fields: `name`, `tagline`, `tags`, `upvotes`, `launch_date`

---

## 🧼 Data Cleaning

Cleaned and enriched data using Pandas:
- Extracted `upvotes per word`, `description length`, `tag count`
- Normalized tag lists and exploded them for analysis
- Saved final CSV: `ai_startups_cleaned.csv`

---

## 🗃️ AWS Integration

| Step | Service | Purpose |
|------|---------|---------|
| 1 | **S3** | Store cleaned CSV |
| 2 | **Glue Crawler** | Create metadata table |
| 3 | **Athena** | Run SQL analysis queries |
| 4 | **QuickSight** | Create dashboards & KPIs |

---

## 📊 Key Insights

| Insight | Value |
|--------|-------|
| Total Startups Scraped | 201 |
| AI Startups Identified | 101 |
| Most Upvoted | Talk To Your Computer (113 upvotes) |
| Top Tags | Productivity, AI, Chrome Extensions |
| Short descriptions outperform long ones (upvotes/word) |

---

## 📈 Dashboard Preview

![dashboard](https://github.com/user-attachments/assets/d95524e3-2229-46bf-9162-39cb620df327)


---

## 📁 Repo Highlights

```
├── scraper/              # GraphQL scraping script
├── cleaning/             # Pandas transformation script
├── data/                 # Raw & cleaned datasets
├── dashboard/            # Final screenshots & PDF
├── docs/index.md         # GitHub Pages
└── README.md             # Project overview on GitHub
```

---

## 🔒 QuickSight Access

Due to AWS limitations, this dashboard is private.  
📎 However, you can view screenshots and metrics above.

---

## 🙋‍♂️ About Me

**David Fafure**  
🎓 MSc Big Data Analytics @ Trent University  
🔗 [LinkedIn](https://www.linkedin.com/in/david-fafure-58776823a/)  
🔗 [Portfolio](https://datascienceportfol.io/davidfafure)  
🔗 [GitHub](https://github.com/DavidFaf)

---

> ⚡ *This project demonstrates end-to-end ownership of a cloud-based data product, from raw scraping to insight delivery.*
