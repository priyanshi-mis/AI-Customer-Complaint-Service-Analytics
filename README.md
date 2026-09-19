# AI-Powered Customer Complaint & Service Analytics

An end-to-end data analytics project focused on analyzing customer complaints,
service performance, resolution time, satisfaction, and NLP-based sentiment.

## 📊 Project Overview

This project analyzes 20,000 customer complaint records to identify complaint
patterns, service performance, customer satisfaction, and sentiment trends.

The project uses Excel, SQLite, Python, NLP and Power BI to transform raw
complaint data into meaningful business insights.

## 🛠️ Tools & Technologies

- Excel – Data Cleaning
- SQLite – Database & SQL Analysis
- Python – Exploratory Data Analysis
- NLP – Sentiment Analysis
- Power BI – Interactive Dashboard

## 📁 Dataset

- Records: 20,000
- Columns: 12
- Complaint Categories: Technical, Billing, Account, General Inquiry, Fraud
- Priority Levels: Low, Medium, High, Critical
- Channels: Chat, Email, Web Form

## 🔄 Project Workflow

Raw Data
→ Data Cleaning
→ SQLite Database
→ SQL Analysis
→ Python EDA
→ NLP Sentiment Analysis
→ Power BI Dashboard
→ Business Insights

## 📌 Key Analysis

- Complaint volume by issue category
- Complaint distribution by priority
- Ticket channels analysis
- Resolution time analysis
- Customer satisfaction analysis
- Sentiment distribution
- Sentiment across complaint categories
- Agent-wise service performance

## 🤖 NLP Sentiment Analysis

Sentiment analysis was performed using a DistilBERT-based NLP pipeline
to classify complaint text into Positive, Neutral and Negative sentiment.

## 📊 Power BI Dashboard

The dashboard contains three pages:

### 1. Overview
Provides a high-level view of complaint volume, resolution time,
satisfaction, issue categories, channels and priority levels.

### 2. Customer Insights
Analyzes customer complaints using issue category, ticket channel
and NLP sentiment.

### 3. Service Performance
Focuses on resolution time, satisfaction score, priority level,
issue category and agent-wise performance.

## 📷 Dashboard Preview

### Overview
![Overview](screenshots/overview.png)

### Customer Insights
![Customer Insights](screenshots/customer-insights.png)

### Service Performance
![Service Performance](screenshots/service-performance.png)

## 📈 Key Metrics

- Total Complaints: 20,000
- Average Resolution Time: 39.23 hours
- Average Satisfaction Score: 3.72 / 5

## 💡 Business Insights

- Technical complaints represent the largest complaint category.
- Low and Medium priority tickets form the majority of complaints.
- Chat, Email and Web Form contribute significantly to ticket volume.
- Sentiment analysis helps identify the nature of customer experiences.
- Resolution time and satisfaction can be analyzed together to understand
  service performance.

## 👩‍💻 Project Skills Demonstrated

SQL | Excel | Python | Pandas | NLP | Sentiment Analysis | Power BI |
Data Visualization | Exploratory Data Analysis | Business Analytics

## 📌 Future Improvements

- Add automated complaint summarization
- Add more NLP-based insights
- Build an interactive complaint-level drill-through
- Add automated dashboard refresh
