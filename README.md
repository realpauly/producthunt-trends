
# 🚀 Startups & Signals: AI Trends on Product Hunt

![dashboard](https://github.com/user-attachments/assets/0d2782af-1cb6-4afe-bba1-6299f81a9875)

This project explores recent AI-related product launches on **Product Hunt** to uncover patterns in upvotes, tags, pitch length, and overall AI momentum in the startup ecosystem.

Using a fully serverless AWS pipeline, the project demonstrates how to extract, clean, analyze, and visualize real-world product data with business-ready insights.

---

## 🎯 Project Goals

- Identify emerging **AI startup trends**
- Analyze **tags**, **description styles**, and **upvote behavior**
- Quantify **AI adoption** among recent Product Hunt launches
- Showcase a cloud-based data pipeline using AWS services

---

## 🔧 Tech Stack

| Layer         | Tools Used |
|---------------|------------|
| Scraping      | Python, GraphQL, Product Hunt API |
| Data Cleaning | Pandas |
| Storage       | AWS S3 |
| ETL & Catalog | AWS Glue |
| Query         | Amazon Athena |
| Visualization | Amazon QuickSight |

---

## 📊 Key Insights

- 📦 **101 AI startups scraped** from a total of **201 Product Hunt launches**
- 🚀 Top upvoted AI startup: *Talk To Your Computer* with **113 upvotes**
- 🏷️ Most common tags: *Productivity*, *Artificial Intelligence*, *Developer Tools*
- 📈 Gauge shows **AI represented 50.25%** of recent launches
- ✂️ Concise product descriptions correlated with higher upvotes per word

---

## 📈 Dashboard Highlights

![dashboard](https://github.com/user-attachments/assets/d7c959d8-b5cc-451d-937e-3e3567a540d9)


📌 Visuals include:
- AI Startups Gauge vs Total
- Top 10 AI Startups by Upvotes
- Word Cloud of Common Tags
- Upvotes vs Description Length
- Tag Count vs Average Upvotes
- Top Startup Summary

---

## 📂 Project Structure

```
ai-pulse-producthunt-trends/
├── scraper/                  # Python script for GraphQL scraping
├── cleaning/                 # Data transformation with Pandas
├── data/                     # Raw & cleaned JSON/CSV data
├── dashboard/                # PDF or PNG of final dashboard
├── README.md
└── index.md                  # GitHub Pages landing version
```

---

## 🛠 How It Works

1. **Scrape:** Query Product Hunt API for recent posts  
2. **Filter:** Extract only AI-related tools using keyword and tag matching  
3. **Clean:** Normalize, enrich, and engineer fields (e.g., upvotes per word)  
4. **Store:** Upload cleaned data to AWS S3  
5. **Catalog & Query:** Use AWS Glue + Athena to make the data SQL-accessible  
6. **Visualize:** Build an interactive dashboard in QuickSight

---

## 🔗 Live Dashboard

🔒 Due to AWS permissions, QuickSight dashboards are private.  
Screenshots and insights are included above.

---

## 👤 About Me

**David Fafure**  
🎓 MSc Big Data Analytics @ Trent University  
📍 Toronto, Canada  

🔗 [LinkedIn](https://www.linkedin.com/in/david-fafure-58776823a/)  
🔗 [Portfolio](https://datascienceportfol.io/davidfafure)  
🔗 [GitHub](https://github.com/DavidFaf)
