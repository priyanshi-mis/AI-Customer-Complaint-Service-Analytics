# import pandas as pd

# df = pd.read_excel("enhanced_customer_support_data.csv.xlsx")

# print("Dataset Shape:", df.shape)

# print("\nColumns:")
# print(df.columns.tolist())

# print("\nFirst 5 Rows:")
# print(df.head())

# print("\nMissing Values:")
# print(df.isnull().sum())

# print("\nDuplicate Rows:")
# print(df.duplicated().sum())

# print("\nIssue Categories:")
# print(df["Issue_Category"].value_counts())

# print("\nPriority Levels:")
# print(df["Priority_Level"].value_counts())

# print("\nTicket Channels:")
# print(df["Ticket_Channel"].value_counts())

# print("\nSatisfaction Scores:")
# print(df["Satisfaction_Score"].value_counts())

# print("\nResolution Time Statistics:")
# print(df["Resolution_Time_Hours"].describe())

# print("\nDate Range:")
# print("From:", df["Submission_Date"].min())
# print("To:", df["Submission_Date"].max())

# import matplotlib.pyplot as plt

# # 1. Complaints by Category
# df["Issue_Category"].value_counts().plot(kind="bar")
# plt.title("Complaints by Issue Category")
# plt.xlabel("Issue Category")
# plt.ylabel("Number of Complaints")
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()


# # 2. Complaints by Priority
# df["Priority_Level"].value_counts().plot(kind="bar")
# plt.title("Complaints by Priority Level")
# plt.xlabel("Priority")
# plt.ylabel("Number of Complaints")
# plt.tight_layout()
# plt.show()


# # 3. Complaints by Channel
# df["Ticket_Channel"].value_counts().plot(kind="bar")
# plt.title("Complaints by Ticket Channel")
# plt.xlabel("Channel")
# plt.ylabel("Number of Complaints")
# plt.tight_layout()
# plt.show()


# # 4. Satisfaction Score
# df["Satisfaction_Score"].value_counts().sort_index().plot(kind="bar")
# plt.title("Customer Satisfaction Score Distribution")
# plt.xlabel("Satisfaction Score")
# plt.ylabel("Number of Customers")
# plt.tight_layout()
# plt.show()


# # 5. Resolution Time
# df["Resolution_Time_Hours"].plot(kind="hist", bins=20)
# plt.title("Resolution Time Distribution")
# plt.xlabel("Resolution Time (Hours)")
# plt.ylabel("Number of Tickets")
# plt.tight_layout()
# plt.show()


# # 6. Monthly Complaint Trend
# df["Submission_Date"] = pd.to_datetime(df["Submission_Date"])

# monthly_complaints = df.groupby(
#     df["Submission_Date"].dt.to_period("M")
# ).size()

# monthly_complaints.plot(kind="line", marker="o")
# plt.title("Monthly Complaint Trend")
# plt.xlabel("Month")
# plt.ylabel("Number of Complaints")
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# print("\nSample Ticket Descriptions:")
# print(df[["Ticket_Subject", "Ticket_Description"]].head(10).to_string(index=False))

# import nltk
# from nltk.sentiment import SentimentIntensityAnalyzer

# nltk.download("vader_lexicon")

# # Clean complaint text
# df["Clean_Complaint"] = (
#     df["Ticket_Description"]
#     .astype(str)
#     .str.split(".")
#     .str[0]
#     .str.strip()
# )

# # Sentiment analyzer
# sia = SentimentIntensityAnalyzer()

# def get_sentiment(text):
#     score = sia.polarity_scores(text)["compound"]

#     if score >= 0.05:
#         return "Positive"
#     elif score <= -0.05:
#         return "Negative"
#     else:
#         return "Neutral"

# df["AI_Sentiment"] = df["Clean_Complaint"].apply(get_sentiment)

# print("\nSentiment Distribution:")
# print(df["AI_Sentiment"].value_counts())

# print("\nSample AI Sentiment Results:")
# print(
#     df[
#         ["Ticket_Subject", "Clean_Complaint", "AI_Sentiment"]
#     ].head(10).to_string(index=False)
# )

# import re

# def clean_complaint(text):
#     text = str(text)
#     text = re.split(r"[.!?]", text)[0]
#     return text.strip()

# df["Clean_Complaint"] = df["Ticket_Description"].apply(clean_complaint)

# print("\nClean Complaint Samples:")
# print(
#     df[["Ticket_Subject", "Clean_Complaint"]]
#     .head(10)
#     .to_string(index=False)
# )

# from transformers import pipeline

# ai = pipeline(
#     "sentiment-analysis",
#     model="distilbert-base-uncased-finetuned-sst-2-english"
# )

# texts = df["Clean_Complaint"].head(30).tolist()

# results = ai(texts)

# for text, result in zip(texts, results):
#     print("\nComplaint:", text)
#     print("Sentiment:", result["label"])
#     print("Confidence:", round(result["score"], 3))

# from transformers import pipeline

# ai = pipeline(
#     "sentiment-analysis",
#     model="distilbert-base-uncased-finetuned-sst-2-english"
# )

# texts = df["Clean_Complaint"].str.replace(
#     "Hi Support, ", "", regex=False
# ).tolist()

# results = ai(texts, batch_size=16)

# df["AI_Sentiment"] = [r["label"] for r in results]

# print("\nAI Sentiment Distribution:")
# print(df["AI_Sentiment"].value_counts())

# test = ai("My payment is failing")

# print("\nTEST RESULT:")
# print(test)


import pandas as pd
import matplotlib.pyplot as plt
import re
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# ==========================================
# 1. LOAD DATA
# ==========================================

df = pd.read_excel("enhanced_customer_support_data.csv.xlsx")

print("Dataset Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())

# ==========================================
# 2. DATA QUALITY CHECK
# ==========================================

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nDuplicate Ticket IDs:")
print(df["Ticket_ID"].duplicated().sum())

# ==========================================
# 3. BASIC EDA
# ==========================================

print("\nIssue Categories:")
print(df["Issue_Category"].value_counts())

print("\nPriority Levels:")
print(df["Priority_Level"].value_counts())

print("\nTicket Channels:")
print(df["Ticket_Channel"].value_counts())

print("\nSatisfaction Scores:")
print(df["Satisfaction_Score"].value_counts())

print("\nResolution Time Statistics:")
print(df["Resolution_Time_Hours"].describe())

# ==========================================
# 4. DATE ANALYSIS
# ==========================================

df["Submission_Date"] = pd.to_datetime(df["Submission_Date"])

print("\nDate Range:")
print("From:", df["Submission_Date"].min())
print("To:", df["Submission_Date"].max())

# ==========================================
# 5. VISUALIZATIONS
# ==========================================

# Complaints by Category
df["Issue_Category"].value_counts().plot(kind="bar")
plt.title("Complaints by Issue Category")
plt.xlabel("Issue Category")
plt.ylabel("Number of Complaints")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Complaints by Priority
df["Priority_Level"].value_counts().plot(kind="bar")
plt.title("Complaints by Priority Level")
plt.xlabel("Priority")
plt.ylabel("Number of Complaints")
plt.tight_layout()
plt.show()

# Complaints by Channel
df["Ticket_Channel"].value_counts().plot(kind="bar")
plt.title("Complaints by Ticket Channel")
plt.xlabel("Channel")
plt.ylabel("Number of Complaints")
plt.tight_layout()
plt.show()

# Satisfaction Score
df["Satisfaction_Score"].value_counts().sort_index().plot(kind="bar")
plt.title("Customer Satisfaction Score Distribution")
plt.xlabel("Satisfaction Score")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()

# Resolution Time
df["Resolution_Time_Hours"].plot(kind="hist", bins=20)
plt.title("Resolution Time Distribution")
plt.xlabel("Resolution Time (Hours)")
plt.ylabel("Number of Tickets")
plt.tight_layout()
plt.show()

# Monthly Complaint Trend
monthly_complaints = df.groupby(
    df["Submission_Date"].dt.to_period("M")
).size()

monthly_complaints.plot(kind="line", marker="o")
plt.title("Monthly Complaint Trend")
plt.xlabel("Month")
plt.ylabel("Number of Complaints")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ==========================================
# 6. COMPLAINT TEXT CLEANING
# ==========================================

def clean_complaint(text):
    text = str(text)
    text = re.split(r"[.!?]", text)[0]
    text = text.replace("Hi Support,", "").strip()
    return text

df["Clean_Complaint"] = df["Ticket_Description"].apply(clean_complaint)

print("\nClean Complaint Samples:")
print(
    df[["Ticket_Subject", "Clean_Complaint"]]
    .head(10)
    .to_string(index=False)
)

# ==========================================
# 7. NLP SENTIMENT ANALYSIS
# ==========================================

nltk.download("vader_lexicon")

sia = SentimentIntensityAnalyzer()

def get_sentiment(text):
    score = sia.polarity_scores(text)["compound"]

    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

df["NLP_Sentiment"] = df["Clean_Complaint"].apply(get_sentiment)

# ==========================================
# 8. SENTIMENT RESULTS
# ==========================================

print("\nNLP Sentiment Distribution:")
print(df["NLP_Sentiment"].value_counts())

print("\nSample NLP Sentiment Results:")
print(
    df[
        ["Ticket_Subject", "Clean_Complaint", "NLP_Sentiment"]
    ].head(10).to_string(index=False)
)

# ==========================================
# 9. SENTIMENT VISUALIZATION
# ==========================================

df["NLP_Sentiment"].value_counts().plot(kind="bar")
plt.title("Customer Complaint Sentiment")
plt.xlabel("Sentiment")
plt.ylabel("Number of Complaints")
plt.tight_layout()
plt.show()

# ==========================================
# 10. SAVE PROCESSED DATA
# ==========================================

df.to_csv(
    "customer_complaint_processed.csv",
    index=False
)

print("\nProcessed dataset saved successfully!")
print("File: customer_complaint_processed.csv")